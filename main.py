import flask
import random
from flask import request, jsonify

companyData = [
    {'id': 0, 'reference': 'AM1002', 'companyName': 'Testing', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 1, 'reference': 'AM1003', 'companyName': 'Testing1', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 2, 'reference': 'AM1004', 'companyName': 'Testing2', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 3, 'reference': 'AM1005', 'companyName': 'Testing3', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 4, 'reference': 'AM1006', 'companyName': 'Testing4', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 5, 'reference': 'AM1007', 'companyName': 'Testing5', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 6, 'reference': 'AM1008', 'companyName': 'Testing6', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 7, 'reference': 'AM1009', 'companyName': 'Testing7', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 8, 'reference': 'AM1010', 'companyName': 'Testing8', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 9, 'reference': 'AM1011', 'companyName': 'Testing9', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 10, 'reference': 'AM1012', 'companyName': 'Testing10', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 11, 'reference': 'AM1013', 'companyName': 'Testing11', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 12, 'reference': 'AM1014', 'companyName': 'Testing12', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 13, 'reference': 'AM1015', 'companyName': 'Testing13', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 14, 'reference': 'AM1016', 'companyName': 'Testing14', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 15, 'reference': 'AM1017', 'companyName': 'Testing15', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'},
    {'id': 16, 'reference': 'AM1018', 'companyName': 'Testing16', 'director': 'AA', 'tradingStatus': 'Trading', 'taxPlanning': 'Yes'}
]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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

@app.route('/getcompanylist', methods=['GET'])
def getCompanyList(skip = None, take = None):
    if 'skip' in request.args:
        skip = int(request.args['skip'])

    if 'take' in request.args:
        take = int(request.args['take'])
    
    if (skip != None):
        end = skip + take
        return jsonify(companyData[skip:end])

    return jsonify(companyData)

def firstByField(field, value):
    for company in companyData:
        if company[field] == value:
            return company

def errorResponse(errorCode, errorMessage):
    errorJson = {
        'error': errorCode,
        'message': errorMessage 
    }

    return jsonify(errorJson)

app.run()