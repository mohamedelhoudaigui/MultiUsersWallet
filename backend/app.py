from flask import Flask, request
import os

from scripts.entry import init
from scripts.route import route_handling


interactor = init()


app = Flask(__name__)

@app.route('/api/IsUser', methods=['GET'])
def IsUser():
    query = request.args.get('query')
    return route_handling(query, interactor.is_user)

@app.route('/api/AddUser', methods=['GET'])
def AddUser():
    query = request.args.get('query')
    return route_handling(query, interactor.add_user)

@app.route('/api/GetTr', methods=['GET'])
def GetTransaction():
    query = request.args.get('query')
    try:
        query = int(query)
    except:
        query = -1
    return route_handling(query, interactor.get_transaction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
