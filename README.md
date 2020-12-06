# Chel's Blog
An Open-Source Web Blogging platform.




## Table of contents
* [General info](#general-info)
* [Django Package or App](#django-package-or-app)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info
A mini blogging platform  built with Python and Django.




## Features

* Account Verification
* Author Login
* Author Password Reset
* API for Clients
* Category List
* Category Articles List
* New Category Submission
* Related Articles
* Comments
* Responsive on all devices
* Pagination
* Clean Code


## Technologies
* Python 3
* Django 3
* HTML5
* CSS3 
* Bootstrap 4
* PostgreSQL


## Setup

To run this app, you will need to follow these 3 steps:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (eg. vscode, PyCharm)

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your Laptop.


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/Williano/Bona-Blog.git

  # Move into project folder
  $ cd Bona-Blog

  # Install from Pipfile
  $ pipenv install

  # Activate the Pipenv shell
  $ pipenv shell

  # Create database tables
  (Bona-Blog-XXXX) $ python manage.py migrate
  
  # Create superuser account
  (Bona-Blog-XXXX) $ python manage.py createsuperuser

  # Start server
  (Bona-Blog-XXXX) $ python manage.py runserver
  
  # Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
  
  # Open the address in the browser
  >>> http://127.0.0.1:XXXX
  
  # Login into Dashboard and write articles
  >>> http://127.0.0.1:8000/author/dashboard/home/
  
  # Django Admin
  >>> http://127.0.0.1:XXXX/admin/
  
  # Run Tests
  $ python manage.py test blog.tests
  ```


## Status
Project is: _in progress_

## Inspiration
This project is based on the goal of improving my skills as a Software Engineer and the best way to improve is by building projects. I wanted to gain a deeper understanding of Django and Object-oriented programming in Python



