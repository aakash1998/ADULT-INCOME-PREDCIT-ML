#Reference from Corey Schafer Youtube
# importing all the libraries
import os
from flask import Flask, render_template, request
from flask_cors import cross_origin
from forms import InputForm
import pickle
from joblib import load

app = Flask(__name__)  # initializing a flask app
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/" , methods=['GET' , 'POST'])
@cross_origin()
def inputform():
    form = InputForm()
    return render_template("index.html" , form=form)

if __name__ == "__main__":
    app.run(debug=True)
