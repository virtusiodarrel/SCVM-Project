<div align='center'>

# Trend Micro SCVM Project
### Members
Eugene Labuac <br>
Darrel Virtusio <br><br>

<br><br>
  
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)<br>
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)

</div>

## Installation

At the command line:
```
pip3 install -r requirements.txt
```

## Running the website

At the command line, navigate to the directory of the application in your local machine.
```
C:\Users\ADMIN>cd Desktop\SCVMProject-TREND\SCVMWebsite

C:\Users\ADMIN\Desktop\SCVMProject-TREND\SCVMWebsite
```

#### Synchronizing the database

Synchronizing the database is Django's way to propagate changes made to the models into your database schema.
```
python manage.py makemigrations
python manage.py migrate
```

#### Creating the superuser

Creating a superuser will allow access to the Admin page (127.0.0.1:8000/admin or localhost:8000/admin)
```
python manage.py createsuperuser
```
Enter the username of your choice:
```
Username: SampleUsername
```
Enter the email address (It can be left blank):
```
Email address: example@gmail.com
```
Enter the password:
```
Password: ********
Password(again): ********
```

#### Starting the development server
```
python manage.py runserver
```
Enter the localhost in your browser
```
127:0:0:1/8000 or localhost:8000
```
