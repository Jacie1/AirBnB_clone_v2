#!/usr/bin/python3
"""
Starts a Flask web application and displays a list of all cities of a State
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Displays a list of all cities of a State"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
