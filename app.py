from flask import Flask, redirect, request, url_for

app = Flask(__name__)

GITHUB_INSTALL_URL = "https://github.com/apps/conveyor-webhook-proto/installations/new"

@app.route('/')
def index():
    r = url_for("auth_callback")
    return f"Hello World! <a href='{r}'>link</a>"

@app.route('/git-providers/1/')
def auth_callback():
    return redirect(GITHUB_INSTALL_URL)

@app.route('/git-providers/1/events/', methods=['POST'])
def events():
    json = request.get_json()
    print(json)
