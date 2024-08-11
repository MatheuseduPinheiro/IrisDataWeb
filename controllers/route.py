import pickle
from flask import redirect, request, url_for, Blueprint, render_template
import numpy as np

# Carregando o modelo
model = pickle.load(open('iris.pkl', 'rb'))

# Criando o Blueprint
app_blueprint = Blueprint('app', __name__)

# Rota raiz que redireciona para a página principal
@app_blueprint.route('/')
def root():
    return redirect(url_for('app.home'))

# Rota para a página principal
@app_blueprint.route('/home')
def home():
    return render_template('index.html')

# Rota para a página de entrada do programa
@app_blueprint.route('/program', methods=['GET'])
def program():
    return render_template('main.html')

# Rota para fazer a previsão usando o modelo
@app_blueprint.route('/predict', methods=['POST'])
def predict():
    try:
        # Coleta dos dados do formulário
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])

        # Criando o array de entrada para o modelo
        arr = np.array([[data1, data2, data3, data4]])

        # Fazendo a previsão
        pred = model.predict(arr)[0]

        # Renderizando a página com a previsão
        return render_template('main.html', data=pred)

    except Exception as e:
        # Em caso de erro, retornar a página com uma mensagem de erro
        return render_template('main.html', error=str(e))
