#!/usr/bin/python3
""" Flask: rendering template """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def lists_route():
    """ displays a HTML page """
    objs_ = [obj for obj in storage.all(State).values()]
    return render_template('7-states_list.html', objs_=objs_)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
