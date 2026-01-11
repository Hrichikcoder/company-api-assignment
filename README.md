# Company API - Employee Management System

## Project Overview
This is a Django REST API project that performs complete CRUD (Create, Read, Update, Delete) operations for managing employee records. [cite_start]It uses **PostgreSQL** as the database and follows the Model-Serializer-View architecture provided by the **Django REST Framework**[cite: 3].

## Tech Stack
* [cite_start]**Language:** Python [cite: 5]
* [cite_start]**Framework:** Django [cite: 6]
* [cite_start]**API Toolkit:** Django REST Framework [cite: 7]
* [cite_start]**Database:** PostgreSQL [cite: 8]
* **Database Adapter:** psycopg2-binary

## Prerequisites
* Python (3.8 or higher)
* PostgreSQL installed and running
* pgAdmin 4 (optional, for database management)

## Setup Instructions

### 1. Environment Setup
Navigate to the project folder and create a virtual environment:
```bash
python -m venv venv

Activate the virtual environment:Windows:Bash.\venv\Scripts\activate
Mac/Linux:Bashsource venv/bin/activate

2. Install DependenciesInstall the required libraries listed in requirements.txt:Bashpip install -r requirements.txt

3. Database ConfigurationOpen pgAdmin or your terminal and create a new database named company_db2.Open company_api/settings.py.Update the DATABASES section with your PostgreSQL password:PythonDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'company_db',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_PASSWORD_HERE',  # <--- Update this
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
4. Run MigrationsCreate the database tables for the Employee model:Bashpython manage.py migrate

5. Start the ServerRun the development server:Bashpython manage.py runserver

The API will be available at: http://127.0.0.1:8000/api/employees/API Endpoints DocumentationThe API supports the following CRUD operations3:MethodEndpointDescriptionPOST/api/employees/Create: Add a new employee record.GET/api/employees/Read: Retrieve a list of all employees.GET/api/employees/<id>/Read: Retrieve details of a single employee by ID.PUT/api/employees/<id>/Update: Modify an existing employee's details.DELETE/api/employees/<id>/Delete: Remove an employee record permanently.Example JSON Payload (Create/Update)JSON{
    "name": "Amit",
    "email": "amit@test.com",
    "department": "IT",
    "salary": 50000.00
}