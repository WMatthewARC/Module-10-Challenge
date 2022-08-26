## Matt's app.py
 
#from lib2to3.pytree import _Results
from unittest import result
from flask import Flask, jsonify

#bring in imports used in the notebook
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, select


app = Flask (__name__)

# conncted to database
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)
Base = automap_base()
Base.prepare(engine, reflect = True)

# refer to tables
Station = Base.classes.station
Measurement = Base.classes.measurement


#Create sesson (link) from Python to the DB
session = Session(engine)


# home route
@app.route("/")
def home():
    return(
        f"<center> <h2> Welcome to the Hawaii Climate Analysis Local API! </h2> </center>"
        f"<center> <h3> the following API's are available </h3> </center>"
        f"<center> /api/v1.0/precipitation </center>"
        f"<center> /api/v1.0/stations </center>"
        f"<center> /api/v1.0/tobs </center>"
        f"<center> /api/v1.0/<start/end> </center>"
        f"<center>  </center>"
        f"<center>  </center>"
        f"<center>  </center>" 
    )

# /api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precip():
        #Return the year of precipitation. From jnotebook
        year_ago = dt.date(2017,8,23) - dt.timedelta(days = 365)

        results = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= year_ago).all()

        session.close()
    #dictionary with the date as the key and the precipaitation as a the value
        precipitation = {date: prcp for date, prcp in results}  
    #convert tp a json
        return jsonify(precipitation)







## app launcher

if __name__ == '__main__':
        app.run(debug=True)

