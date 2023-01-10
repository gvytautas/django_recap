#!/usr/bin/env python
"""
-Install Django (pip install django)
-Create Project (django-admin startproject <name> (.))
-Create migrations (python manage.py makemigrations)
-Execute migrations (python manage.py migrate)
-Run application (python manage.py runserver)
-Create application (python manage.py startapp <name> (.))
-Create superuser (python manage.py createsuperuser)
-Create model
-Model relationships
-Create view
-Configure urls
-Create form (delete, create)
-Create templates
-Create requirements.txt
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_recap.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
