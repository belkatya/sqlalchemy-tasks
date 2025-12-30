from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Movie
from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, future=True)
session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session = session_maker()


# BEGIN (write your solution here)
async def get_all_movies(session):
    query = select(Movie).options(selectinload(Movie.director)).order_by(Movie.title)
    result = await session.execute(query)
    movies = result.scalars().all()
    
    formatted_movies = []
    for movie in movies:
        release_date_str = movie.release_date.strftime('%Y-%m-%d')
        
        movie_info = (
            f"{movie.title} by {movie.director.name}, "
            f"released on {release_date_str}, "
            f"duration: {movie.duration} min, "
            f"genre: {movie.genre}, "
            f"rating: {movie.rating}"
        )
        formatted_movies.append(movie_info)
    
    return formatted_movies
# END
