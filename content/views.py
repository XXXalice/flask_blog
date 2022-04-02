from content import app

config_path = "/config/{}"

@app.route("/")
def main():
    return "<h1>test dayo</h1>"

@app.route(config_path.format("debug"))
def show_debug_status():
    return "test"