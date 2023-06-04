# import library
from flask import jsonify
import json

def getGlosarium():
    try:
        # Load JSON from file
        with open("glosarium.json", "r") as file:
            data = json.load(file)

        # Return the prediction result
        return jsonify({
            'status': 'success',
            'code': 200,
            'message': 'fetch glosarium successful!',
            'data': data
        })

    except Exception as e:
        print(str(e))
        return jsonify({
            'status': 'failed',
            'code': 400,
            'message': 'Error fetching glosarium!'
        })
    