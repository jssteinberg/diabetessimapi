from flask import Flask, send_from_directory, jsonify
from hovorka_simulator import run_simulation
import random

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/", methods=['GET'])
def base():
    # return send_from_directory('client/public', 'index.html')
    return str(run_simulation())

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>", methods=['GET'])
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand", methods=['GET'])
def hello():
    return str(random.randint(0, 100))


@app.route("/diabetes", methods=['GET'])
def diabetes_sim():
    return jsonify(run_simulation())


if __name__ == "__main__":
    app.run(debug=True)
