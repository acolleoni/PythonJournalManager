# pyjm
Python Journal Manager

## Installation instruction (MS Windows version)
Create a DB called `pyjm` in your Mysql DB and run the following commands:
* `py -m venv venv`
* `venv\Scripts\activate.bat` (CMD) or `venv\Scripts\activate.ps1` (PowerShell)
* `pip install Django`
* `pip install django-cors-headers`
* `pip install djangorestframework`
* `pip install djangorestframework-simplejwt`
* `pip install mysqlclient`
* `python manage.py migrate`
* `python manage.py runserver`