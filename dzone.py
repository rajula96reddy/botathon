from flask import Flask

from flask import jsonify

from flask import request

import urllib2,json
app = Flask(__name__)

@app.route('/',methods=['GET'])

def getAllEmp():
    url="http://www.json-generator.com/api/json/get/ckgOiCWLfS?indent=2" 
    response = urllib2.urlopen(url)
    data= json.loads(response.read())
    return jsonify(data)


if __name__ == '__main__':

 app.run()
