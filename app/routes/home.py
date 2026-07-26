from flask import Blueprint, render_template
from sqlalchemy import func
from app.models.employee import Employee
from app.models import db

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
@home_bp.route("/home")
def home():
    total_employees = Employee.query.count()
    total_departments = db.session.query(func.count(Employee.department.distinct())).scalar() or 0
    return render_template(
        "home.html",
        total_employees=total_employees,
        total_departments=total_departments
    )
