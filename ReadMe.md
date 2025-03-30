# Mysite

A Django-based mysite system with Telegram bot integration for client registration.

## Features

- Admin panel with DaisyUI theme
- Telegram bot for client registration
- PostgreSQL database integration
- Client management system

## Prerequisites

- Python 3.8+
- PostgreSQL
- Telegram Bot Token

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create PostgreSQL database:
```sql
CREATE DATABASE mysite;
```

5. Apply migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

## Configuration

1. Update database settings in `mysite/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Running the Application

1. Start Django development server:
```bash
python manage.py runserver
```

## Admin Panel

Access the admin panel at `http://localhost:8000/admin` with your superuser credentials.

## Project Structure

- `backend/` - Main application directory
  - `models.py` - Database models
  - `admin.py` - Admin panel configurations

## License

[MIT License](LICENSE)