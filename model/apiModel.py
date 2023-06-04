from flask_restx import Api, fields

def apiSwagger(app):
    return Api(app, title='Diagnese API', description='This is Diagnese Capstone Project API Documentation')

def namespaceApi(api, nameRoute):
    return api.namespace(nameRoute)

def predictModel(api):
    return api.model('predict', {
        'kaku_saat_ingin_bergerak': fields.Integer(1),
        'sensasi_berputar': fields.Integer(1),
        'kehilangan_keseimbangan': fields.Integer(1)
    })