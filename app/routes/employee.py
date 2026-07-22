from flask import Blueprint, request, redirect, url_for, render_template, flash
from sqlalchemy import or_

from app.models.employee import Employee
from app.models import db

employee_bp = Blueprint("employee", __name__)

SORT_COLUMNS = {
    "name": Employee.name,
    "email": Employee.email,
    "department": Employee.department,
    "salary": Employee.salary,
    "id": Employee.id
}

@employee_bp.route("/employee/list")
def employee_list():
    search = request.args.get("search", "", type=str).strip()
    sort_by = request.args.get("sort_by", "id", type=str).lower()
    order = request.args.get("order", "asc", type=str).lower()

    selected_department = request.args.get("department", "", type=str).strip()
    
    # Safely parse numeric query parameters
    min_salary = request.args.get("min_salary", None, type=float)
    max_salary = request.args.get("max_salary", None, type=float)

    # Validate salary parameters
    if min_salary is not None and min_salary < 0:
        min_salary = None
    if max_salary is not None and max_salary < 0:
        max_salary = None
    if min_salary is not None and max_salary is not None and min_salary > max_salary:
        min_salary, max_salary = max_salary, min_salary

    # Safely parse pagination parameters with type=int
    page = request.args.get("page", 1, type=int)
    if not page or page < 1:
        page = 1

    per_page = request.args.get("per_page", 5, type=int)
    if per_page not in [5, 10]:
        per_page = 5

    query = Employee.query

    # Search filter
    if search:
        query = query.filter(
            or_(
                Employee.name.ilike(f"%{search}%"),
                Employee.email.ilike(f"%{search}%"),
                Employee.department.ilike(f"%{search}%")
            )
        )

    # Department filter
    if selected_department:
        query = query.filter(Employee.department == selected_department)

    # Salary range filter
    if min_salary is not None:
        query = query.filter(Employee.salary >= min_salary)
    if max_salary is not None:
        query = query.filter(Employee.salary <= max_salary)

    # Apply whitelisted sorting
    sort_column = SORT_COLUMNS.get(sort_by, Employee.id)
    if order == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    # Dynamically populate departments from database
    distinct_depts = db.session.query(Employee.department.distinct()).order_by(Employee.department).all()
    departments = [d[0] for d in distinct_depts if d[0]]

    # Execute pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    employees = pagination.items

    return render_template(
        "employee.html",
        employees=employees,
        pagination=pagination,
        departments=departments,
        selected_department=selected_department,
        min_salary=min_salary,
        max_salary=max_salary,
        search=search,
        sort_by=sort_by,
        order=order,
        page=page,
        per_page=per_page
    )






from app.models import db

@employee_bp.route("/employee/add", methods=["POST", "GET"])
def employeeAdd():

    if request.method == "POST":

        employee = Employee(
            name = request.form["name"],
            email = request.form["email"],
            password = request.form["password"],
            salary = request.form["salary"],
            department = request.form["department"]
        )

        db.session.add(employee)
        db.session.commit()

        flash(f"Employee '{employee.name}' registered successfully!", "success")
        return redirect(url_for("employee.employee_list"))
    
    return render_template("add_employee.html")

#get specific employee
@employee_bp.route("/employee/employeeDetail/<int:id>", methods=["GET"])
def employeeDetail(id):

    employee = Employee.query.get_or_404(id)

    return render_template("employee_detail.html", employee = employee)


@employee_bp.route("/employee/employeeUpdate/<int:id>", methods=["POST", "GET"])
def employeeUpdate(id):

    employee = Employee.query.get_or_404(id)

    if request.method == "POST":

        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.password = request.form["password"]
        employee.salary = request.form["salary"]
        employee.department = request.form["department"]

        db.session.commit()

        flash(f"Employee '{employee.name}' updated successfully!", "info")
        return redirect(url_for("employee.employee_list"))

    return render_template("update_employee.html", employee=employee)


@employee_bp.route("/employee/employeeDelete/<int:id>")
def employeeDelete(id):

    employee = Employee.query.get_or_404(id)
    emp_name = employee.name

    db.session.delete(employee)
    db.session.commit()

    flash(f"Employee '{emp_name}' deleted successfully!", "danger")
    return redirect(url_for("employee.employee_list"))


#advance crud operation

#pagination
#sorting
#filtering
#searching
