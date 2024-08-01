# IrisDataWeb

IrisDataWeb é um projeto que adapta a famosa base de dados Iris utilizando a biblioteca `sklearn` para a modelagem de dados e o framework Flask para criar uma interface web interativa. O objetivo é facilitar a exploração dos dados e a visualização dos resultados de diferentes modelos de Machine Learning.

![Tela Principal](https://github.com/user-attachments/assets/cac37b7c-8154-4308-bf87-158f72d6bd5b)

## Funcionalidades

- **Modelagem com `sklearn`**: Implementação de algoritmos de classificação para prever a espécie de flores Iris.
- **Interface Web com Flask**: Interface amigável para interação com o modelo, permitindo a inserção de dados e a visualização dos resultados.
- **Arquitetura MVC**: Estrutura de código clara e bem documentada, baseada no artigo [Minimal Flask Application using MVC design pattern](https://medium.com/@arslandevs/minimal-flask-application-using-mvc-design-pattern-842845cef703).
- **Aprendizado de Máquina**: Utiliza SVC (Support Vector Classification) para previsões.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no projeto.
- **Flask**: Framework web utilizado para criar a interface do usuário.

![Imagem Flask](https://github.com/user-attachments/assets/011adcf3-c3c7-4ef8-949a-885232acb4d2)

- **scikit-learn (`sklearn`)**: Biblioteca utilizada para a modelagem dos dados e implementação dos algoritmos de Machine Learning.
- **HTML/CSS**: Para a criação da interface web.

![Imagem sklearn](https://github.com/user-attachments/assets/77e46e4e-4cf7-423c-a7b7-e18e1a132811)

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/SeuUsuario/IrisDataWeb.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd IrisDataWeb
    ```
3. Instale as dependências:
    ```bash
    pip install flask pandas pickle-mixin scikit-learn
    ```

4. Inicie o servidor Flask:
    ```bash
    flask run
    ```
5. Acesse o aplicativo no navegador:
    ```bash
    http://127.0.0.1:5000
    ```
