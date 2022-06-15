"""Model-specific logic for the Flask sample app.

William Ellison
<waellison@gmail.com>
October 2021.
"""
from flask_sqlalchemy import SQLAlchemy

"""Connection to the backing store."""
db = SQLAlchemy()
