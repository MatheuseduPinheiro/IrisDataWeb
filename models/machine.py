import pandas as pd
import numpy as np
import pickle
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 1. Carregar os Dados
df = pd.read_csv('datasets/iris_data.csv')
#print(df.head())

# 2. Separar Características e Rótulos
# Selecionar colunas de características e rótulo
x = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = df['variety'].values


# 3. Codificar Rótulos Categóricos
le = LabelEncoder()
y = le.fit_transform(y)
print(y)


# 4. Dividir os Dados
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
sv = SVC(kernel='linear')
sv.fit(X_train, y_train)

# Salvar o modelo treinado
pickle.dump(sv, open('iris.pkl', 'wb'))

# Opcional: Exibir as primeiras linhas para verificar a preparação
print(df.head())
