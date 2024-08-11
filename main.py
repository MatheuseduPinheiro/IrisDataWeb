from flask import Flask
from controllers.route import app_blueprint

app = Flask(__name__)

app.register_blueprint(app_blueprint)


app.run(debug=True)