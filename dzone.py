from flask import Flask

from flask import jsonify

from flask import request

import urllib2,json
app = Flask(__name__)

@app.route('/',methods=['GET'])

def getAllEmp():
    url="https://api.coinsecure.in/v1/exchange/ticker"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    price = data['message']['lastPrice']
    price = str(price/100)
    engati_format = {
"data": {
"type": "text",
"text": "The last traded price of bitcoin is " + price
}
}
    return json.dumps(engati_format)


if __name__ == '__main__':

 app.run()
