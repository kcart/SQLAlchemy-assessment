"""Models and database functions for Ratings project."""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "models"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    founded =  Column(Integer)
    headquarters = Column(String(50))
    discontinued = Column(Integer)

    def __repr__(self):
        return "<Model id=%d name=%s founded=%d headquarters=%s discontinued=%d>" % (
            self.id, self.name, self.founded, self.headquarters, self.discontinued)


class Brand(db.Model):

    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    brand_name = Column(String(50), nullable=True)
    name = Column(String(50), nullable=False)
    
    def __repr__(self):
        return "<Brand id=%d year=%d brand_name=%s name=%s>" % (
            self.id, self.year, self.brand_name, self.name)

# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

   # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
