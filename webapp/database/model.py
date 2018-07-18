# model for our postgres database

# to upgrade the db schema, run: 
#> python manage.py db migrate
#> python manage.py db upgrade
# in the virtualenv

from server import db

from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key=True); # unique id for the row
    username = db.Column( db.String() )
    password = db.Column( db.String() )
    email = db.Column( db.String() )

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        #representaiton of the object when we query for it.
        return self.id



