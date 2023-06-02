from flask import Flask, request
import predictSymptom
from flask_restx import Api, Resource

# Initialize Flask
app = Flask(__name__)
api = Api(app, title='Diagnese API', description='This is Diagnese API Documentation')

ns = api.namespace('diagnese', description='Namespace description')


# Initialize Flask server (file prediction.py)
@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to our API"


@ns.route('/predict')
class Prediction(Resource):
    @ns.doc(description='diagnose by symptom')
    def post(self):
        data = request.get_json()

        return predictSymptom.predictSymptom(data)
    def get(self):
        
        return predictSymptom.getAllDignosis()


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True) #uncomment if you want to run on GCP
    app.run(port=8080, debug=True) #uncomment if you want to run on local


@api.route('/swagger')
class Swagger(Resource):
    def get(self):
        return api.__schema__
