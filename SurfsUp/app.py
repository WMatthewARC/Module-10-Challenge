## Matt's app.py
 
from flask import Flask, jsonify

#bring in imporats used in the notebook
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, select


app = Flask (__name__)

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









## app launcher

if __name__ == '__main__':
        app.run(debug=True)

