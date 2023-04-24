#!/usr/bin/env python3
"""
Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all State objects present in DBStorage"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
