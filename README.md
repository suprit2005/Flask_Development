# Flask Development 🚀 — Advanced Employee Management System (EMS)

A full-featured Flask web application built with **Flask**, **SQLAlchemy ORM**, **Flask-Migrate**, **MySQL**, **Jinja2 templates**, and **Bootstrap 5 UI**, implementing advanced Search, Filtering, Sorting, and Pagination.

---

## ✨ Features Implemented

### 1. 🔍 Searching
- Case-insensitive search across **Employee Name**, **Email**, and **Department** using `sqlalchemy.or_` and `.ilike()`.
- Search term retention and filter reset controls.

### 2. 🔀 Whitelisted Sorting
- Sort employees by **Name**, **Email**, **Department**, **Salary**, or **ID**.
- Supports **Ascending** (`asc`) and **Descending** (`desc`) ordering.
- Clickable table column headers with dynamic sort direction indicators (`↑` / `↓`).

### 3. 🎯 Advanced Filtering
- **Dynamic Department Selection**: Populates filter options directly from database records (`Employee.department.distinct()`).
- **Validated Salary Bounds**: Supports Minimum Salary (`min_salary`) and Maximum Salary (`max_salary`) range bounds.

### 4. 📄 Pagination & Parameter Preservation
- Configurable page limits (**5** or **10** records per page).
- **Previous** / **Next** controls, page numbers, current page indicator, and total record count badge.
- **Parameter Preservation**: All active search terms, filter selections, sort options, and page sizes remain attached to URL parameters while navigating between pages.

### 5. 🎨 Modern Bootstrap 5 UI
- Responsive layout with styled directory cards, filter control panels, tables, and badge highlights.
- Dismissible Flask flash messages for **Add**, **Update**, and **Delete** actions.
- Friendly alert messages for duplicate emails and empty records banner.

---

## 🗃️ Database Configuration (MySQL)

This project uses **MySQL** database via **PyMySQL** driver.

### 1. Create MySQL Database
Ensure MySQL Server is running on your machine, then execute:
```sql
CREATE DATABASE employee_db;
```

### 2. Environment Variables / `.env` File
Create a `.env` file in the project root directory to configure your MySQL credentials:
```env
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=employee_db
```

*(Note: If no `.env` file is present, credentials can also be set via terminal environment variables: `$env:MYSQL_PASSWORD="your_password"`).*

---

## 📁 Project Structure

```
Flask-Development/
├── app/
│   ├── models/
│   │   ├── __init__.py           # Instantiates db = SQLAlchemy()
│   │   └── employee.py           # Employee SQLAlchemy model schema
│   ├── routes/
│   │   ├── __init__.py           # Package marker
│   │   ├── department.py         # department_bp blueprint with aggregations
│   │   ├── employee.py           # employee_bp blueprint with Search, Filter, Sort, Pagination & CRUD
│   │   └── home.py               # home_bp blueprint with dashboard statistics
│   ├── static/
│   │   ├── css/                  # Custom CSS styles
│   │   └── js/                   # Custom JavaScript scripts
│   ├── templates/
│   │   ├── add_employee.html     # Registration form template
│   │   ├── base.html             # Base layout with Bootstrap 5 CDN & flash alerts
│   │   ├── department.html       # Department page template
│   │   ├── employee.html         # Directory view with Search, Filter, Sort & Pagination
│   │   ├── employee_detail.html  # Employee detail view template
│   │   ├── home.html             # Dashboard template
│   │   ├── navbar.html           # Bootstrap top navigation bar
│   │   └── update_employee.html  # Employee update form template
│   └── __init__.py               # App factory create_app(), DB & migration initialization
├── app.py                        # Main entry point starting app
├── config.py                     # App configuration (MySQL URI, URL-encoding, dotenv)
├── migrations/                   # Alembic database migration scripts
├── requirements.txt              # Dependencies list
└── README.md                     # Project documentation
```

---

## 🛠️ Setup & Execution Guide (For Evaluator / Clone Setup)

### 1. Clone Repository & Move inside Project
```bash
git clone https://github.com/suprit2005/Flask_Development.git
cd Flask_Development
```

### 2. Create & Activate Virtual Environment

* **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

* **Linux / macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL & Run Database Migrations
1. Create the database in MySQL:
   ```sql
   CREATE DATABASE employee_db;
   ```
2. Create a `.env` file with your MySQL credentials, or set your password in the terminal:
   ```powershell
   $env:MYSQL_PASSWORD="your_mysql_password"
   ```
3. Initialize database tables:
   ```bash
   flask db upgrade
   ```

### 5. Run the Application
```bash
python app.py
```

Application will start on:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📋 Submission Checklist Status

- [x] CRUD functionality working correctly
- [x] Pagination implemented (5 or 10 records/page, Prev/Next buttons, page indicators)
- [x] Search functionality implemented (Name, Email, Department)
- [x] Sorting implemented (Name, Email, Department, Salary - ASC/DESC)
- [x] Department filtering implemented
- [x] Salary range filtering implemented
- [x] Search, filtering, sorting, and pagination work together seamlessly
- [x] UI improved using Bootstrap 5
- [x] MySQL database support implemented via PyMySQL
- [x] README.md updated with complete setup & execution guide
