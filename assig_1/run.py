import os
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname

from app import create_app , models

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')  # Address of your .env file
load_dotenv(dotenv_path)


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

dat = SQLAlchemy(app)

if __name__ == "__main__":
    dat.create_all()    
    app.run(host="0.0.0.0", debug=True)