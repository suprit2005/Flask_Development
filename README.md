# Flask Development 🚀 — Employee Management System (EMS)

A full-featured Flask web application with SQLAlchemy ORM, Jinja2 templates, and Bootstrap 5 UI, built for managing employee records with advanced Search, Filtering, Sorting, and Pagination.

---

## ✨ Features Implemented

### 1. 🔍 Search
- Case-insensitive search across **Employee Name**, **Email**, and **Department** using `sqlalchemy.or_` and `.ilike()`.
- Search term retention and clear button.

### 2. 🔀 Whitelisted Sorting
- Sort employees by **Name**, **Email**, **Department**, **Salary**, or **ID**.
- Supports **Ascending** (`asc`) and **Descending** (`desc`) ordering.
- Clickable table column headers with dynamic sort direction indicators (`↑` / `↓`).
- Column parameters are strictly whitelisted to prevent invalid inputs.

### 3. 🎯 Filtering
- **Dynamic Department Selection**: Populates filter options directly from existing database records (`Employee.department.distinct()`).
- **Validated Salary Bounds**: Supports Minimum Salary (`min_salary`) and Maximum Salary (`max_salary`) range bounds with numeric type parsing and range validation.

### 4. 📄 Pagination & Parameter Preservation
- Configurable page limits (**5** or **10** records per page).
- **Previous** / **Next** controls, page numbers, current page indicator, and total record count badge.
- **Parameter Preservation**: All active search terms, filter selections, sort options, and page sizes remain attached to URL parameters while navigating between pages (e.g. `?search=dev&department=IT&min_salary=50000&sort_by=salary&order=desc&page=2&per_page=5`).

### 5. 🎨 Modern Bootstrap 5 UI
- Styled directory cards, filter control panels, responsive tables, badge highlights, and custom form cards.
- Dismissible Flask flash messages for **Add**, **Update**, and **Delete** actions.
- "No records found" fallback banner with filter reset action.

---

## 📁 Project Structure

```
Flask-Development/
├── app/
│   ├── models/
│   │   ├── __init__.py           # Instantiates db = SQLAlchemy(), imports Employee
│   │   └── employee.py           # Employee SQLAlchemy model schema
│   ├── routes/
│   │   ├── __init__.py           # Package marker
│   │   ├── auth.py               # Authentication routes
│   │   ├── department.py         # department_bp blueprint
│   │   ├── employee.py           # employee_bp blueprint with Search, Filter, Sort, Pagination & CRUD
│   │   └── home.py               # home_bp blueprint
│   ├── static/
│   │   ├── css/                  # Custom CSS styles
│   │   └── js/                   # Custom JavaScript scripts
│   ├── templates/
│   │   ├── add_employee.html     # Registration form template
│   │   ├── base.html             # Base layout with Bootstrap 5 CDN & flash alerts
│   │   ├── department.html       # Department page template
│   │   ├── employee.html         # Directory view with Search, Filter, Sort & Pagination
│   │   ├── employee_detail.html   # Employee detail view template
│   │   ├── home.html             # Landing page template
│   │   ├── navbar.html           # Bootstrap top navigation bar
│   │   └── update_employee.html  # Employee update form template
│   └── utils/
│       └── __init__.py           # Utility modules
├── app.py                        # Entry point starting create_app()
├── config.py                     # App configuration (database URI, SECRET_KEY)
├── requirements.txt              # Dependencies list
└── README.md                     # Project documentation
```


---

# 🛠 Prerequisites

- Python 3.11+
- Git
- VS Code (Recommended)

Check your Python version

```bash
python --version
```

or

```bash
python3 --version
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/suprit2005/Flask_Development.git
```

Move inside the project

```bash
cd Flask-Development
```

---

# 🐍 Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate

### Command Prompt

```cmd
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

Upgrade pip

```bash
python -m pip install --upgrade pip
```

Install required packages

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Flask Application

Run the application

```bash
python run.py
```

or

```bash
flask run
```

Application will start on

```
http://127.0.0.1:5000
```

---

# 🔄 Deactivate Virtual Environment

```bash
deactivate
```

---

# 📌 Install New Package

```bash
pip install package_name
```

Update requirements

```bash
pip freeze > requirements.txt
```

---

# 🗃 Database Setup

If using Flask SQLAlchemy

Initialize database

```python
from app.models import db

db.create_all()
```

Or using Flask Shell

```bash
flask shell
```

```python
from app.models import db
db.create_all()
```

---

# 📂 Environment Variables (Optional)

Create a `.env`

```
SECRET_KEY=your-secret-key
FLASK_ENV=development
FLASK_DEBUG=True
```

Install dotenv

```bash
pip install python-dotenv
```

---

# 📚 Topics will be Covered

- Flask Introduction
- Routing
- URL Parameters
- HTTP Methods
- Templates (Jinja2)
- Template Inheritance
- Static Files
- Forms
- WTForms
- Flash Messages
- Sessions
- Cookies
- Blueprints
- SQLAlchemy ORM
- CRUD Operations
- Authentication
- File Upload
- Configuration
- Error Handling
- Pagination
- Flask CLI
- REST API Basics

---

# 💻 Common Commands

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```cmd
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Run application

```bash
python run.py
```

Deactivate

```bash
deactivate
```

---

# 📦 Generate requirements.txt

```bash
pip freeze > requirements.txt
```

Install from requirements

```bash
pip install -r requirements.txt
```

---

# 🔍 Verify Installation

```bash
python
```

```python
import flask
print(flask.__version__)
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---
