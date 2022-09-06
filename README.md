# Inventory Management System
# Introduction 
Stock Managment System is python based personal projected developed using django framework. This application can be basically used to keep track of all the inventory items that are issued to different departments within a firm/company.  
Different python packages were used to develop this project such as crispy-form, psycopg2,django-bootstrap-modal-forms, and others, which are all mentioned in requirements.txt file.

# Tech Stack
  1. [Python 3.9](https://www.python.org/)
  2. [Django 4.0.4](https://www.djangoproject.com/)
  3. [PostgreSQL](https://www.postgresql.org/)
  4. [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/)
  5. [Bootstrap](https://getbootstrap.com/)
  6. [Docker](https://www.docker.com/)
  
# Installation
**GIT clone from GitHub**

###### First step is to make a directory.
```
$ mkdir inv_manag
$ cd inv_mang
```

###### Then clone the [Inventory Management App Repo](https://github.com/Shuvam77/stock_management) from the GitHub.
```
inv_mang $ git clone https://github.com/Shuvam77/stock_management.git .
```

**Docker**
###### Docker Compose
Build Images and Run Docker Containers
```
inv_mang $ docker build .
inv_mang $ docker-compose up
```

###### Migrations
Propogate your models into database schema
```
inv_mang $ docker-compose exec web python manage.py makemigrations
inv_mang $ docker-compose exec web python manage.py showmigrations
inv_mang $ docker-compose exec web python manage.py migrate 
```

###### Create Django Superuser
For super access in application
```
inv_mang $ docker-compose exec web python manage.py createsuperuser

Username: admin
Email address: admin@email.com
Password: sudo@123

URL: http://YOUR_LOCALHOST_URL/admin/
```

###### Run docker containers
```
inv_mang $ docker-compose up
or
inv_mang $ docker-compose up -d (run in background)
```

###### Stop docker container
```
inv_mang $ docker-compose down
```

###### Run and build container
```
inv_mang $ docker-compose up --build
```
