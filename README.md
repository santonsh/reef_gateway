# flask gateway server

# Workflow:
# Install python, pip
# Install flask: pip install flask



working with db and models

1. First run db_create.py to create a db file (should exist by now)
2. When you create/update models.py run db_migration.py this will craete the migration file to transform your present db file form to the updated models.py form
3. run db_upgrade.py to perform a db migration using latest migration file


to implement:

global parameters configuration/update mechanism
check command mechanism
calendar/program/scheduler mechanism



Global sever installation/start

1. Install python
2. Install virtualenv
3. Instal supervisor - sudo apt-get install -y supervisor
3. git clone reef_gateway
   reef_gateway already includes virtual environment with flask, sqlalchemy, Flask-SQLAlchemy and xmltodict along with flask server application 
4. Activate virtual enviroment - source venv/bin/activate
5. Start the server - run_server.sh

