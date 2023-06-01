from flask import Flask, request, jsonify
from predictSymptom import predictSymptom

# Initialize Flask
app = Flask(__name__)

# Initialize Flask server (file prediction.py)
@app.route("/", methods=["POST"])
def welcome():
    return "Welcome to our API"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    return predictSymptom(data)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True) #uncomment if you want to run on GCP
    app.run(port=8080, debug=True) #uncomment if you want to run on local