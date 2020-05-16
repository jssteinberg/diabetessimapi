from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from hovorka_simulator import run_simulation
import random

app = Flask(__name__)
CORS(app)

# Path for our main Svelte page
@app.route("/", methods=['GET'])
def base():
    # return send_from_directory('client/public', 'index.html')
    return jsonify(run_simulation())

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>", methods=['GET'])
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand", methods=['GET'])
def hello():
    
    return str(random.randint(0, 100))


@app.route('/query-example', methods=['GET'])
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)


@app.route("/diabetes", methods=['GET'])
def diabetes_sim():
    meal_1 = request.args.get('m1') #if key doesn't exist, returns None
    meal_2 = request.args.get('m2') #if key doesn't exist, returns None
    meal_3 = request.args.get('m3') #if key doesn't exist, returns None
    meal_4 = request.args.get('m4') #if key doesn't exist, returns None

    return jsonify(run_simulation(meal_1, meal_2, meal_3, meal_4))


if __name__ == "__main__":
    app.run(debug=True, port=4500)
