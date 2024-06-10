from flask import Flask
from routes.home import home_route
from routes.programa import programa_route
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(programa_route)

app.run(debug=True)