import MySQLdb
import sys

reset_color = '\033[0m'
bold = '\033[1m'
red_color = '\033[91m'
green_color = '\033[92m'

def create_database(db_name, db_user, db_password, db_host='localhost'):
    try:
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password)
        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        print(f"{bold}{green_color}Database '{db_name}' created or already exists!{reset_color}")
        db.close()
    except MySQLdb.Error as e:
        print(f"{bold}{red_color}Error while creating database!{reset_color}\n{e}")
        sys.exit(1)

# parameters
db_user = 'root'
db_password = 'root'
db_name = 'vnergy'

# create the MySQL database
create_database(db_name, db_user, db_password)

import os
import sys
import django
from django.core.management import call_command

# configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vnergy.settings')
django.setup()

# make the migrations (via Django)
try:
    call_command('makemigrations')
    print(f"{bold}{green_color}Migrations created!{reset_color}")
except:
    print(f"{bold}{red_color}Error while applying migrations!{reset_color}")
    sys.exit(1)

# migrate (via Django)
try:
    call_command('migrate')
    print(f"{bold}{green_color}Migrations applied!{reset_color}")
except:
    print(f"{bold}{red_color}Error while applying migrations!{reset_color}")
    sys.exit(1)

# load the data (via a JSON file)
try:
    call_command('loaddata', 'fixtures')
    print(f"{bold}{green_color}Data loaded!{reset_color}")
except Exception as e:
    print(f"{bold}{red_color}Error while loading data! error: {e}{reset_color}")
    sys.exit(1)

# the setup is complete
print(f"{bold}Setup complete! You can now run the server with `python manage.py runserver`.{reset_color}")
