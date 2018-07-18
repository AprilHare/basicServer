# initializes the application

from flask import Flask
from config import Config



app = Flask(__name__)
app.config.from_object(Config)
#db = SQLAlchemy( app ) # to do <<<---

import routes


