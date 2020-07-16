from flask import Flask, render_template, redirect, url_for, request,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import socket
import os

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


TEXT1=os.environ.get('TEXT1', "Hackfest")
TEXT2=os.environ.get('TEXT2', "Registration")
ORGANIZER=os.environ.get('ORGANIZER', "UVCE")

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # temporary route
    @app.route('/')
    def rsvp():
        db.session().commit() #Weird Line without which app is not going to work
        _items = Rsvp.query.all()
        items = [item for item in _items]
        count = len(items)
        hostname = socket.gethostname()
        #return items
        return render_template('profile.html', counter=count, hostname=hostname,items=items, TEXT1=TEXT1, TEXT2=TEXT2, ORGANIZER=ORGANIZER)


    @app.route('/new', methods=['POST'])
    def new():
        rsv = Rsvp(name=request.form['name'],email=request.form['email'])
        db.session.add(rsv)
        db.session.commit()
        return redirect('/')

    migrate = Migrate(app,db)

    from app import models 
    from models import Rsvp

    return app
