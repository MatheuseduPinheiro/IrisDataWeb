
from flask import Blueprint, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

program_route = Blueprint('program', __name__)


@program_route.route('/program')

def predict():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('main.html',data=pred)