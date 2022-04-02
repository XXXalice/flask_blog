import flask

app = flask.Flask(__name__)
app.config.from_object("content.config")

import content.views