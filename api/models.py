import os
from api import app
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(os.path.realpath(__file__))
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'movies.db')

# Create Database Instance
db = SQLAlchemy(app)
app.app_context().push()


class Movies(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(length=20), nullable=False, unique = True)
    genre = db.Column(db.String(length=10), nullable=False)
    release_year = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return self.title

    @property
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table.columns}