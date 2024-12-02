import os

# Load secret key and database URI from environment variables
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY")
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
POSTGRES_DB=os.getenv("POSTGRES_DB")


# SECRET_KEY="HXdS8/Ny8qXgqKkG8IZkmgQL3wQT0D3M30n9RbHDOcC2iXGwLbBiWIpK"
# SQLALCHEMY_DATABASE_URI=f"postgresql://phinguyen:phinguyen@superset-postgres/superset"
SQLALCHEMY_DATABASE_URI=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}/{POSTGRES_DB}"
