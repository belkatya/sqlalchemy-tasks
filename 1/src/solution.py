import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# BEGIN (write your solution here)
db_url = os.getenv("DATABASE_URL")
def create_db_engine(db_url, echo=False, pool_size=5, max_overflow=10):
    return create_engine(db_url, echo=echo, pool_size=pool_size, max_overflow=max_overflow)
# END
