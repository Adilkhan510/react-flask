from flask import Flask, request, jsonify, make_response
from sklearn.externals import joblib
import numpy as np 
import sys

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello Gender Classifier App"

if __name__ == "__main__":
    app.run(debug=True)