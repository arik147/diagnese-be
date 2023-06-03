import os

# import library 
from flask import Flask, request
import predictSymptom
from flask_restx import Api, Resource, fields

# Initialize Flask
app = Flask(__name__)
api = Api(app, title='Diagnese API', description='This is Diagnese API Documentation')

ns = api.namespace('diagnese', description='main route of this API')

input_model = api.model('/diagnese/predict', {
    'symptom_1': fields.Integer(),
    'symptom_2': fields.Integer(),
    'symptom_3': fields.Integer()
})


# Initialize Flask server (file prediction.py)
@app.route("/", methods=["GET"])
def welcome():
    return 'Welcome to our API'


@ns.route("/predict")
class Prediction(Resource):
    @ns.doc(description='diagnose by symptom')
    @api.expect(input_model)  # Add this line
    def post(self):
        data = request.get_json()

        return predictSymptom.predictSymptom(data)
    
    def get(self):  
        return predictSymptom.getAllDignosis()

# Run app
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080, debug=True) #uncomment if you want to run on GCP
    # app.run(port=8080, debug=True) #uncomment if you want to run on local
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


@api.route("/swagger")
class Swagger(Resource):
    def get(self):
        return api.__schema__
