from flask import Blueprint, render_template, request
import pandas as pd
import pickle
import numpy as np

preprocessor = pickle.load(open("models/pipeline.pkl", 'rb'))
model = pickle.load(open("models/linreg.pkl", 'rb'))

app = Blueprint("app", __name__, static_folder='static', template_folder='templates')

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == "POST":
        user_input = {
            'seller_type': request.form.get('seller_type'),
            'layout_type': request.form.get('layout_type'),
            'furnish_type': request.form.get('furnish_type'),
            'property_type': request.form.get('property_type'),
            'city': request.form.get('city'),
            'bedroom': request.form.get('bedroom'),
            'area': request.form.get('area'),
            'bathroom': request.form.get('bathroom')
            }
        print(user_input)
        x = pd.DataFrame(user_input, index=[1])
        pred = np.expm1(model.predict(preprocessor.transform(x))[0])
    return render_template("index.html", proba=int(pred))