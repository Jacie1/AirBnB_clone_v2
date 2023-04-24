#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays an HTML page like 8-index.html.
    """
    states = sorted(storage.all('State').values(), key=lambda x: x.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda x: x.name)
    cities = sorted(storage.all('City').values(), key=lambda x: x.name)
    places = sorted(storage.all('Place').values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           cities=cities, places=places)


@app.teardown_appcontext
def close_session(exception=None):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
