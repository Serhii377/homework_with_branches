movies_db = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "duration": 148},
    {"id": 2, "title": "Interstellar", "genre": "Sci-Fi", "duration": 169}
]

def get_all_movies():
    return movies_db

def add_movie(title, genre, duration):
    new_id = max([m["id"] for m in movies_db], default=0) + 1
    new_movie = {"id": new_id, "title": title, "genre": genre, "duration": duration}
    movies_db.append(new_movie)
    return new_movie

def get_movie_by_id(movie_id):
    for movie in movies_db:
        if movie["id"] == movie_id:
            return movie
    return None

def search_movies_by_title(query):
    return [m for m in movies_db if query.lower() in m["title"].lower()]