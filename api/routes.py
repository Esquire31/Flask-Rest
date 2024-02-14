from .models import db
from .restx_model import api, movie_model
from flask import request, jsonify
from flask_restx import Resource
from .models import Movies
from sqlalchemy.exc import IntegrityError


@api.route('/movies')
class Movie(Resource):
    @api.expect(movie_model, code=200)
    @api.response(409, "Movie Already Exists!")
    @api.response(200, "Success!!!")
    def post(self):
        # Post a New Movie
        payload = request.get_json()
        title = payload["title"]
        genre = payload["genre"]
        release_year = payload["release_year"]

        new_movie = Movies(title=title, genre=genre, release_year=release_year)
        db.session.add(new_movie)

        try:
            db.session.commit()
            return jsonify(new_movie.to_dict)
        except IntegrityError:
            db.session.rollback()
            api.abort(409, "Movie with the Given Title already exists")

    @api.response(200, 'Success!!!')
    def get(self):
        # Get all movies
        movies = Movies.query.all()
        movies = [movie.to_dict for movie in movies]
        return jsonify({"count": len(movies), "movies": movies})


@api.route('/movies/<int:id>')
class MovieResource(Resource):
    @api.response(404, "Movie not Found")
    @api.response(200, "Success!!!", movie_model)
    def get(self, id):
        # Get a movie by ID
        movie = Movies.query.get(id)
        if movie:
            return jsonify(movie.to_dict)
        else:
            api.abort(404, message="The movie you are looking for is not in the List", type="error")

    @api.response(404, "Movie Not Found")
    @api.expect(movie_model, code=200)
    @api.response(200, "Success!!!")
    def put(self, id):
        movie = Movies.query.get(id)
        if movie:
            payload = request.get_json()
            movie.title = payload["title"]
            movie.genre = payload["genre"]
            movie.release_year = payload["release_year"]
            db.session.commit()
            return jsonify(movie.to_dict)
        else:
            api.abort(404, "Movie not Found :(", type="error")

    @api.response(404, "Movie Not Found")
    @api.response(200, "Success!!!")
    def delete(self, id):
        # Delete a given Movie
        movie_delete = Movies.query.get(id)
        if movie_delete:
            db.session.delete(movie_delete)
            db.session.commit()
            return f'movie with id {id} has been deleted Successfully'
        else:
            api.abort(404, "Movie not Found :(", type="error")


@api.route('/movies/from_year=<int:start_year>to_year=<int:end_year>')
class MovieRangeResource(Resource):
    @api.response(200, "Success!!!")
    def get(self, start_year, end_year):
        # Get movies in the Range
        movies = Movies.query.filter(Movies.release_year >= start_year, Movies.release <= end_year)
        movies = [movies.to_dict for movie in movies]
        return jsonify({"count": len(movies), "movies": movies})


@api.route('/movies/<string:title>')
class MovieResourceByTitle(Resource):
    @api.response(200, "Success!!!")
    def get(self, title):
        # Get a Movie by Title
        movie = Movies.query.filter(Movies.title == title).first()
        return jsonify(movie.to_dict)
