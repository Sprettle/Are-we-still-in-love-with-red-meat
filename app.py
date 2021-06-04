# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql' + os.environ.get('DATABASE_URL', '')[8:]  or "sqlite:///db.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

meat = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inlove.html")
def page1():
    return render_template("inlove.html")

@app.route("/out-of-love.html")
def page2():
    return render_template("out-of-love.html")

@app.route("/the-future.html")
def page3():
    return render_template("the-future.html")   

#Meat API page
@app.route("/api/v1.0/meat")
def meat():
  

    """Return a list of all meat info"""
    # Query all meat data
    results = db.session.query(meat.year, meat.beef, meat.lamb, meat.pork, meat.chicken).all()

     # Create a dictionary from the row data and append to a list of all_meat
    all_meat = []
    for year, beef, lamb, pork, chicken in results:
        meat_dict = {}
        meat_dict["year"] = year
        meat_dict["beef"] = beef
        meat_dict["lamb"] = lamb
        meat_dict["pork"] = pork
        meat_dict["chicken"] = chicken
        meat.append(meat_dict)

    return jsonify({"data":all_meat})

if __name__ == "__main__":
    app.run()
