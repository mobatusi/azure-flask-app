from flask import Flask, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    #Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"

    # # Adding database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Adding routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    # Create Databse
    create_database(app)
    return app

def create_database(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print("Database Created")


app = create_app()
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000 , debug=False)