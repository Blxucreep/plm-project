# PLM - project

Here the repository of the project of PLM course.

You will find the following directories/files:
- `captures/`: contains the captures of the application;
- `vnergy/`: contains the Django project;
- `data_to_fixtures/`: contains the script to convert the data to fixtures;
- `data.json`: the original data, not yet converted to fixtures;
- `demo.mkv`: a video showing the application in action;
- `diagram.mdj`: contains the diagram of the database;
- `init.sql`: contains the SQL script to create the database and the tables;
- `load.sql`: contains the SQL script to load the data into the database;
- `prez.pptx`: the presentation of the project.

## How the database is structured

The database is structured in the following way:
![database](captures/database.png)

## Setup

To setup the project, you need to have MySQL installed. You also need basic libraries for python and in particular **django** and **mysqlclient**.

## How to run the application

To run the application, you need to run the following commands, **in the first `vnergy` directory (the one containing `manage.py`)**:
- `python setup.py` (to create the database, make the migrations and apply them, and load the data)
- `python manage.py runserver` (to run the server)

Then, you can access the application at the following address: `http://127.0.0.1:8000/` (in function of the port used by the server).
