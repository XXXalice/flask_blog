from content import app
from content.config import UmemiyaConfig

from flask import render_template

config_path = "/config/{}"

@app.route("/")
def main():
    return "<h1>test dayo</h1>"

@app.route(config_path.format("debug"))
def show_debug_status():
    app.config.from_object(UmemiyaConfig)
    return render_template("index.html", config=app.config.items())