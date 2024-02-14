from flask_restx import Api, fields
from api import app

api = Api(app)

movie_model = api.model(
    'Movies',
    {
        'title': fields.String(),
        'Genre': fields.String(),
        'release_year': fields.Integer()
    }
)
