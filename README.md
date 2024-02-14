# Flask-Rest
This repository contains a Flask-based REST API for managing movie information.

### Key Features:

* Exposes endpoints for various movie operations:
    * Get all movies
    * Get a movie by ID
    * Get movies by release year range
    * Get movies by title
    * Post a new movie
    * Update an existing movie
    * Delete a movie
* Leverages Flask-RESTX for efficient API development and automatic Swagger UI documentation.
* Employs SQLAlchemy for smooth database interactions.

### Installation:

1. Clone this repository:
```bash
git clone https://github.com/Esquire31/Flask-Rest.git
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Configure database connection:
    * Create a `.env` file and set the following variables:
        * `DATABASE_URL`: Connection string for your database (e.g., PostgreSQL, MySQL)
    * Alternatively, create a configuration file with appropriate settings.

### Running the API:

```bash
flask run
```

This will start the development server. Access the API documentation at `http://localhost:5000/swagger/`.

### API Endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/movies` | GET | Get all movies |
| `/movies/<int:movie_id>` | GET | Get a movie by its ID |
| `/movies` | GET | Get movies by release year range (query parameters: `from_year`, `to_year`) |
| `/movies` | GET | Get movies by title (query parameter: `title`) |
| `/movies` | POST | Create a new movie |
| `/movies/<int:movie_id>` | PUT | Update an existing movie |
| `/movies/<int:movie_id>` | DELETE | Delete a movie |

For detailed information on request and response formats, please refer to the Swagger UI documentation.

### License:

This project is licensed under the MIT License. See the LICENSE file for details.

