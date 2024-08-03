from flask import Flask
from controllers.home import home_route 
from controllers.program import program_route 
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(program_route)

app.run(debug=True)