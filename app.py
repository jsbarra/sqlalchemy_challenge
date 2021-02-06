import numpy as np 
import sqlalchemy
import sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as datetime

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.Measurement
Station = Base.classes.Station

session = Session(engine)

app = Flask(__name__)

@app.rout("/")
def welcome():
    return(
        f"Available API routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/&lt;start> <br/>"
        f"/api/v1.0/&lt;start>/&lt;end> <br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    precip = session.query(measurement.date, measurement.prcp).filter(measrement.date >= year_ago).order_by(measurement.date).all()
    prcp_list = list(np.ravel(precip))
    return jsonify(prcp_list)

    session.close()