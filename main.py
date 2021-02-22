import flask
import random
import json
from flask import request, jsonify

with open('data.json') as json_data:
    apiData = json.load(json_data)

app = flask.Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/testone', methods=['GET'])
def testendpoint():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return errorResponse(400, 'No id was specified.')

    return jsonify(firstByField('companyId', id))

@app.route('/getillustrationlist', methods=['GET'])
def getIllustrationList(skip = None, take = None):
    if 'skip' in request.args:
        skip = int(request.args['skip'])

    if 'take' in request.args:
        take = int(request.args['take'])

    if (skip != None):
        end = skip + take
        return jsonify(apiData["illustList"][skip:end])

    return jsonify(apiData["illustList"])

@app.route('/getinvoicelist', methods=['GET'])
def getInvoiceList(skip = None, take = None):
    if 'skip' in request.args:
        skip = int(request.args['skip'])

    if 'take' in request.args:
        take = int(request.args['take'])

    if (skip != None):
        end = skip + take
        return jsonify(apiData["invoiceList"][skip:end])

    return jsonify(apiData["invoiceList"])

@app.route('/getemployeelist', methods=['GET'])
def getEmployeeList(skip = None, take = None):
    if 'skip' in request.args:
        skip = int(request.args['skip'])

    if 'take' in request.args:
        take = int(request.args['take'])

    if (skip != None):
        end = skip + take
        return jsonify(apiData["employeeList"][skip:end])

    return jsonify(apiData["employeeList"])

@app.route('/getcompanylist', methods=['GET'])
def getCompanyList(skip = None, take = None):
    if 'skip' in request.args:
        skip = int(request.args['skip'])

    if 'take' in request.args:
        take = int(request.args['take'])
    
    if (skip != None):
        end = skip + take
        return jsonify(apiData["companyList"][skip:end])

    return jsonify(apiData["companyList"])

def firstByField(field, value):
    for company in apiData["companyList"]:
        if company[field] == value:
            return company

def errorResponse(errorCode, errorMessage):
    errorJson = {
        'error': errorCode,
        'message': errorMessage 
    }

    return jsonify(errorJson)