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
@app_blueprint.route('/IrisDataWeb/home')
def home():
    return render_template('index.html')

# Rota para a página de entrada do programa
@app_blueprint.route('/IrisDataWeb/home/program', methods=['GET'])
def program():
    return render_template('main.html')

# Rota para fazer a previsão usando o modelo
@app_blueprint.route('/IrisDataWeb/home/program/predict', methods=['POST'])
def predict():
    try:
        # Coleta dos dados do formulário com validação
        data1 = request.form.get('a', type=float)
        data2 = request.form.get('b', type=float)
        data3 = request.form.get('c', type=float)
        data4 = request.form.get('d', type=float)

        # Verificando se todos os dados foram fornecidos e são válidos
        if None in [data1, data2, data3, data4]:
            raise ValueError("Todos os dados do formulário devem ser fornecidos e devem ser números.")

        # Criando o array de entrada para o modelo
        arr = np.array([[data1, data2, data3, data4]])

        # Fazendo a previsão
        pred = model.predict(arr)[0]

        # Renderizando a página com a previsão
        return render_template('main.html', data=pred)

    except ValueError as ve:
        # Em caso de erro de valor, retornar a página com uma mensagem de erro específica
        return render_template('main.html', error=str(ve))
    except Exception as e:
        # Capturando outros tipos de exceções
        return render_template('main.html', error="Ocorreu um erro durante o processamento: " + str(e))
