import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('front.html')

@app.route('predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('front.html')

if __name__ == "--main__":
    app.run(port=500, debug=True)
