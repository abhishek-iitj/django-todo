# Django ToDo [![Build Status](https://travis-ci.org/abhishek-iitj/django-todo.svg?branch=master)](https://travis-ci.org/abhishek-iitj/django-todo)
A ToDo REST API app developed in Python(Django)


### Installation:
Requirements:
- Python 3.5 runtime
- Django 2.1.3

Procedure (Ubuntu 16.04):
- Create a new virtual environment(djangodev) and activate it
    ```
    $ python3 -m venv ~/.virtualenvs/djangodev
    $ source ~/.virtualenvs/djangodev/bin/activate
    ```
- Clone and navigate to the repository
    ```
    $ git clone https://github.com/abhishek-iitj/django-todo.git
    $ cd django-todo     
    ```
- Use pip to install other dependencies from `requirements.txt`
    ```
    $ pip install -r requirements.txt
    ```
- Run tests
    ```
    $ ./manage.py test -v 2
    ```
- Run server
    ```
    $ python manage.py runserver
    ```
