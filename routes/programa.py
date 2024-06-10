from flask import Blueprint, render_template

programa_route = Blueprint('programa', __name__)


@programa_route.route('/programa')

def programa():
    return render_template('main.html')