from content import app

@app.route("/")
def main():
    return "<h1>test dayo</h1>"