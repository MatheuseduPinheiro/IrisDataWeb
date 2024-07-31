
from flask import Blueprint, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iris.pkl', 'rb'))

program_route = Blueprint('program', __name__)


@program_route.route('/program', methods=['GET'])
def program():
    return render_template('main.html')


@program_route.route('/predict', methods=['POST'])
def predict():
   data1 = float(request.form['a'])
   data2 = float(request.form['b'])
   data3 = float(request.form['c'])
   data4 = float(request.form['d'])
   arr = np.array([[data1, data2, data3, data4]])
   pred = model.predict(arr)
   return render_template('main.html',data=pred)