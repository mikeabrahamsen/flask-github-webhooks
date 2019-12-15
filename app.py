from flask import Flask, request, jsonify

app = Flask(__name__)

GITHUB_INSTALL_URL = "https://github.com/apps/conveyor-dev-webhook-demo/installations/new"

@app.route('/')
def index():
    return f"<h1>Github Apps with Flask</h1></br> <a href='{GITHUB_INSTALL_URL}'>Install app</a>"

@app.route('/git-providers/1/events/', methods=['POST'])
def events():
    json = request.get_json()
    print(json)
    return jsonify({'message': 'success'}), 200


if __name__ == "__main__":
    app.run()
