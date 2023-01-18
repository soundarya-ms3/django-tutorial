# Django Ecommerce Website
An ecommerce website built using Django framework.The website displays products like Laptop,Smartphones,Earphones etc. Users can add and remove products to/from their cart while also specifying the quantity of each item.

## Installation
Python and Django need to be installed

``` pip install django ```

It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

``` pip install virtualenv ```

## Steps to Create the Django Project

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project.

### Creating a virtual environment

A virtual environment can be created and activated by executibg the following commands
```
    virtualenv envname
    cd envname
    cd Scripts
    activate 
```
### Creating a django project
``` django-admin startproject <PROJECT_NAME> ```
### Move into the Project
```  cd <PROJECT_NAME> ```

### Create a Django App in your project
``` python manage.py startapp <APP_NAME> ```
### Make migrations
``` 
  python manage.py makemigrations
  python manage.py migrate
```
### Run Django Server
```  python manage.py runserver ```
### Open the IP adress in Your Browser
Open the given URL in your browser.  http://127.0.0.1:8000/ 

## Demo link
https://drive.google.com/file/d/1X_rrA6iOUF7clx307spHpEgQ-q-tUz3g/view?usp=share_link

Software used for screen recording - Clipchamp
