"""
Application initialization logic.

Copyright (c) 2022 by William Ellison.  This program is licensed under
the terms of the MIT License.

William Ellison
<waellison@gmail.com>
October 2021
"""
import os
import dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .models import db
from .views import sample_view


def create_app(test_config=True):
    """Create and return a new Flask app."""
    dotenv.load_dotenv("..")
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    if test_config:
        app.config.from_mapping(
            SECRET_KEY=os.getenv("secret_key"),
            SQLALCHEMY_DATABASE_URI="postgresql://postgres:hunter2@localhost:5432/willpress",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO=False,
        )
    else:
        app.config.from_mapping(
            SECRET_KEY=os.getenv("secret_key"),
            SQLALCHEMY_DATABASE_URI="postgresql://postgres@pg:5432/willpress",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO=True,
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.app = app
    db.init_app(app)
    db.create_all()
    _ = Migrate(app, db)

    app.register_blueprint(sample_view.bp)

    return app
