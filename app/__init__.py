from flask import Flask ,render_template
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html") 

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
     
    return app