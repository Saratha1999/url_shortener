# URL Shortener

A simple Django-based URL shortener that generates 6-character short codes for long URLs.

## Features

- Shorten long URLs into 6-character codes
- Automatic generation of unique short codes using letters and digits
- Django ORM integration for data persistence
- Duplicate URL handling with unique constraints

## Model Structure

The application uses a single Django model `Shortened_URL` with the following fields:

- `original_url`: The original long URL (URLField with unique constraint)
- `short_code`: A 6-character unique identifier (auto-generated)

## Installation

1. Make sure you have Django installed:
```bash
pip install django
```

2. Add this app to your Django project's `INSTALLED_APPS` in `settings.py`

3. Run migrations to create the database table:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Future Enhancements

- Add click tracking and analytics
- Implement custom short codes
- Add expiration dates for URLs
- Create web interface for URL shortening
- Add URL validation and security checks

## Requirements

- Python 3.6+
- Django 3.0+
