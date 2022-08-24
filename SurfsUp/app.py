## Matt's app.py
 
from flask import Flask, jsonify

app = Flask (__name__)

# home route
@app.route("/")
def home():
    return("<center> <h2>Welcome to the Hawaii Climate Analysis Local API!</h2> </center>")






## app launcher

if __name__ == '__main__':
        app.run(debug=True)

