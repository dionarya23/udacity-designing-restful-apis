from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST', 'PUT', 'DELETE'])
def homeFunction():
    if request.method == 'GET':
        return 'Hello With Method GET'
    elif request.method == 'POST':
        return 'Hello With Method POST'
    elif request.method == 'PUT':
        return 'Hello With Method PUT'
    else:
        return 'Hello With Method Delete'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)