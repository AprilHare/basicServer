#! /usr/bin/env python
# Sets up db management scripts to run on the app
# eg: python manage.py db init
# !!! only runs in the virtualenv !!!

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from server import app, db
from config import config
app.config.from_object(config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

