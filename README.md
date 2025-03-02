# Shark Project

A Django REST framework based project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- PostgreSQL 12 or higher

## PostgreSQL Setup

1. Install PostgreSQL on your system:
   - macOS (using Homebrew): `brew install postgresql`
   - Ubuntu/Debian: `sudo apt-get install postgresql postgresql-contrib`
   - Windows: Download installer from https://www.postgresql.org/download/windows/

2. Start PostgreSQL service:
   - macOS: `brew services start postgresql`
   - Ubuntu/Debian: `sudo service postgresql start`
   - Windows: PostgreSQL is automatically started as a service

3. Create database:
```bash
# Connect to PostgreSQL
psql -U postgres

# Create database (in PostgreSQL shell)
CREATE DATABASE shark_db;

# Exit PostgreSQL shell
\q
```

## Setup

1. Clone the repository
```bash
git clone <repository-url>
cd shark
```

2. Create a virtual environment
```bash
python -m venv .venv
```

3. Activate the virtual environment

On macOS/Linux:
```bash
source .venv/bin/activate
```

On Windows:
```bash
.venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Configure database:
   - Open `shark/settings.py`
   - Update database settings if needed:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'shark_db',
             'USER': 'postgres',
             'PASSWORD': 'postgres',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

6. Run database migrations
```bash
python manage.py migrate
```

7. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

## Running the Project

1. Ensure PostgreSQL is running
2. Start the development server
```bash
python manage.py runserver
```

3. Access the project at:
- Main application: http://localhost:8000
- Admin interface: http://localhost:8000/admin
- API authentication: http://localhost:8000/api-auth/login

## API Documentation

The API is protected with authentication. To access the API endpoints:

1. Log in using the API authentication URL
2. Use your superuser credentials created during setup
3. Include authentication credentials in your API requests

## Development

- The project uses Django REST framework for API development
- CORS is enabled for development (configured in settings.py)
- PostgreSQL is used as the database backend

## Security Notes

- Debug mode is enabled by default (disable it in production)
- CORS is set to allow all origins (configure appropriately for production)
- Make sure to change the SECRET_KEY in settings.py for production use
- Use strong passwords for database users in production 