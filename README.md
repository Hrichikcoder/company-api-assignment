
# Company API - Employee Management System

A robust RESTful API built with **Django** and **Django REST Framework** to manage employee records. This project uses **PostgreSQL** for data persistence and implements a complete CRUD (Create, Read, Update, Delete) architecture.

## 📌 Features
* **Create** new employee records with validation.
* **Read** a list of all employees or retrieve specific details by ID.
* **Update** existing employee information (salary, department, etc.).
* **Delete** employee records from the database.
* **Database Integration:** Fully connected to a PostgreSQL backend.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** Django 5.x / 6.x
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Adapter:** psycopg2-binary

---

## 🚀 Setup & Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/company-api-assignment.git](https://github.com/YOUR_USERNAME/company-api-assignment.git)
cd company-api-assignment
2. Create Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install all required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
🗄️ Database Configuration
1. Create the Database
Ensure PostgreSQL is running, then create a new database named company_db.

Using Terminal:

SQL

CREATE DATABASE company_db;
Using pgAdmin: Right-click Databases > Create > Database... > Name it company_db.

2. Configure Settings
Open company_api/settings.py and update the DATABASES section with your PostgreSQL credentials:

Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'company_db',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_PASSWORD_HERE',  # <--- REPLACE THIS
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
3. Run Migrations
Apply the database migrations to create the necessary tables.

Bash

python manage.py migrate
⚡ Running the Application
Start the development server:

Bash

python manage.py runserver
The API will be accessible at: http://127.0.0.1:8000/api/employees/

📖 API Endpoints
Method	Endpoint	Description
GET	/api/employees/	Retrieve a list of all employees.
POST	/api/employees/	Create a new employee.
GET	/api/employees/<id>/	Retrieve details of a specific employee.
PUT	/api/employees/<id>/	Update an existing employees details.
DELETE	/api/employees/<id>/	Delete an employee record.

Export to Sheets

Example JSON Payload (POST/PUT)
JSON

{
    "name": "Amit Sharma",
    "email": "amit@test.com",
    "department": "IT",
    "salary": 60000.00
}
🧪 Testing
You can test the API using Postman or cURL.

Create Employee: Send a POST request to /api/employees/ with the JSON payload above.

List Employees: Send a GET request to /api/employees/.

Update Employee: Send a PUT request to /api/employees/1/ with updated JSON data.

Delete Employee: Send a DELETE request to /api/employees/1/.

📂 Project Structure
Plaintext

Django_Assignment/
│
├── company_api/        # Project Configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── employees/          # App Logic
│   ├── models.py       # Employee Database Model
│   ├── serializers.py  # Data Conversion Logic
│   ├── views.py        # API Views (CRUD)
│   ├── urls.py         # App URL Routing
│   └── ...
│
├── manage.py           # Django Command Line Utility
├── requirements.txt    # Project Dependencies
└── README.md           # Project Documentation
👤 Author
Name: Hrichik Khandait

Role: Computer Science Undergrad (B.Tech)
