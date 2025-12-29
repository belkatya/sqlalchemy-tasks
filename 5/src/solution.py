from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def format_movie_with_director(movie_obj, director_name):
    movie = movie_obj if hasattr(movie_obj, 'title') else movie_obj[0]
    director = director_name if isinstance(director_name, str) else movie_obj[1]
    
    return (f"{movie.title} by {director}, "
            f"released on {movie.release_date.strftime('%Y-%m-%d') if movie.release_date else 'N/A'}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}")

def get_movies_with_directors(session):
    query = select(Movie, Director.name).join(Movie.director).order_by(Movie.title)
    result = session.execute(query).all()
    return [
        format_movie_with_director(movie, director_name)
        for movie, director_name in result
    ]
# END
