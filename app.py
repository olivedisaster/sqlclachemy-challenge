# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func  engine = create_engine("sqlite:///Resources/hawaii.sqlite")  # reflect an existing database into a new model

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables  

# reflect an existing database into a new model

# We can view all of the classes that automap found

# Save references to each table

# Create our session (link) from Python to the DB