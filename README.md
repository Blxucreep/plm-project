# PLM - project

Here the reposiroty of the project of PLM course.

You will find the following directories/files:
- 

## Setup

To setup the project, you need to have MySQL installed. You also need basic libraries for python and in particular **django** and **mysqlclient**.

## How to run the application

To run the application, you need to run the following commands, **in the first `fruiticart` directory (the one containing `manage.py`)**:
- `python create_database.py` (to create the database)
- `python manage.py migrate` (to create the tables in the database)
- `python manage.py load_data` (to load the data in the database)
- `python manage.py runserver` (to run the server)

Here an image of the commands to run, with the expected output:
![commands](captures/how_to_run.png)

Then, you can access the application at the following address: `http://127.0.0.1:8000/` (in function of the port used by the server).

## How to use the application



## Some specifications

