import os

# import library 
from flask import Flask, request
from flask_restx import Resource
import predictSymptom
import apiModel

# Initialize Flask
app = Flask(__name__)

api = apiModel.apiSwagger(app)
ns = apiModel.namespaceApi(api)
predictModel = apiModel.predictModel(api)

@ns.route("/")
class Prediction(Resource):
    @ns.doc(description='Route Diagnose by symptom')
    @api.expect(predictModel)
    def post(self):
        data = request.get_json()
        return predictSymptom.predictSymptom(data)
    
    def get(self):  
        return predictSymptom.getAllDignosis()
    
# Run app
if __name__ == "__main__":
    # app.run(port=8080, debug=True) #uncomment if you want to run on local
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))