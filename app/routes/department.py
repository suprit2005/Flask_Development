from flask import Blueprint, render_template
from sqlalchemy import func
from app.models.employee import Employee
from app.models import db

department_bp = Blueprint("department", __name__)

@department_bp.route("/department")
def departmentHome():
    # Query department stats: department name, employee count, and average salary
    dept_stats = (
        db.session.query(
            Employee.department,
            func.count(Employee.id).label("total_employees"),
            func.avg(Employee.salary).label("avg_salary")
        )
        .group_by(Employee.department)
        .order_by(Employee.department)
        .all()
    )

    return render_template("department.html", dept_stats=dept_stats)