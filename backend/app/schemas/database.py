"""
database.py
-------------
This file is responsible for:
- Creating the database connection with MySQL
- Creating a SQLAlchemy session
- Providing a Base class for ORM models
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# MySQL connection URL
# Format: mysql+pymysql://username:password@host/database_name
DATABASE_URL="postgresql://db_7mails_user:xWBH1mtCUOLuIKOJhMEcinCBF8DkdiXF@dpg-d90vlje8bjmc739ik2gg-a.ohio-postgres.render.com/db_7mails"

# Create database engine
engine=create_engine(DATABASE_URL)
# Create session factory
sessionLocal=sessionmaker(bind=engine)
# Base class for all ORM models
Base=declarative_base()