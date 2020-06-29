# web_app/__init__.py

import os

from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes

load_dotenv()

def create_app():
    app_env = os.environ.get("FLASK_ENV", "development") # set to "production" in the production environment
    secret_key = os.environ.get("SECRET_KEY", "super secret") # overwrite this in the production environment
    testing = False # True if app_env == "test" else False
    
    app = Flask(__name__)
    app.config.from_mapping(ENV=app_env, SECRET_KEY=secret_key, TESTING=testing)
    app.register_blueprint(home_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)