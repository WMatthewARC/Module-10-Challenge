## Matt's app.py
 
from flask import Flask, jsonify

app = Flask (__name__)

# home route
@app.route("/")
def home():
    return("Welcome to the Hawaii Climate Analysis Local API!")
    





## app launcher

if __name__ == '__main__':
        app.run()

