from flask import Flask

from flask import jsonify

from flask import request

import urllib2,json
app = Flask(__name__)

empDB=[

 {

 'id':'101',

 'name':'Saravanan S',

 'title':'Technical Leader'

 },

 {

 'id':'201',

 'name':'Rajkumar P',

 'title':'Sr Software Engineer'

 }

 ]

@app.route('/',methods=['GET'])

def getAllEmp():
    url="http://www.json-generator.com/api/json/get/bUHsUMIFNK?indent=2"
    response = urllib2.urlopen(url)
    data= json.loads(response.read())
    return jsonify(data)


if __name__ == '__main__':

 app.run()
