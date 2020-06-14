from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler




import sys


db = SQLAlchemy()
migrate = Migrate()
scheduler = APScheduler()

# migrate = Migrate(app, db)
# ma = Marshmallow(app)


def create_app():

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')
    # scheduler.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # scheduler.start() 
    
    
    with app.app_context():
        from . import routes  # Import routes
    #    from . import models
    #    
    #    db.create_all()
         # Create database tables for our data models
        # schedule.every().day.at("05:00").do(routes.autostock)
        return app


app = create_app()