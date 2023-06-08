import os

# import library 
from flask import Flask, request
from flask_restx import Resource
from handler import predictHandler, glosariumHandler
import model.apiModel as apiModel

# Initialize Flask
app = Flask(__name__)

# API init
api = apiModel.apiSwagger(app)
nsPredict = apiModel.namespaceApi(api, 'predict')
nsGlosarium = apiModel.namespaceApi(api, 'glosarium')
predictModel = apiModel.predictModel(api)

# ========= PREDICT route ============
@nsPredict.route("/")
class Prediction(Resource):
    @nsPredict.doc(description='Route Diagnose by symptom')
    @api.expect(predictModel)
    def post(self):
        data = request.get_json()
        return predictHandler.predictSymptom(data)

    def get(self):  
        return predictHandler.getSymptoms()

# ========= GLOSARIUM route ============  
@nsGlosarium.route("/")
class Glosarium(Resource):
    @nsGlosarium.doc(description='Route glosarium')
    
    def get(self):  
        return glosariumHandler.getGlosarium()
    
# Run app
if __name__ == "__main__":
    # app.run(port=8080, debug=True) #uncomment if you want to run on local
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))