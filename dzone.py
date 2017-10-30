from flask import Flask

from flask import jsonify

from flask import request

import urllib2,json
app = Flask(__name__)

@app.route('/currency', methods=['GET'])

def getAllEmp():
    cc = request.args.get('cryptocurrency')
    c = request.args.get('currency')
    url = "https://api.coinmarketcap.com/v1/ticker/" + cc + "/?convert=" +c
    # url="https://api.coinsecure.in/v1/exchange/ticker"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    price = str(data[0]["last_updated"]) + " " + str(c.upper())
    priceincurrency = str(data[0]["price_"+c]) + " " + str(c.upper())
    dayvolume = str(data[0]["24h_volume_"+c]) + " " + str(c.upper())
    marketcap = str(data[0]["market_cap_"+c]) + " " + str(c.upper())
    totalsupply = data[0]["total_supply"]
    availablesupply = data[0]["available_supply"]
    percentchange_1h = data[0]["percent_change_1h"]
    percentchange_24h = data[0]["percent_change_24h"]
    percentchange_7d = data[0]["percent_change_7d"]
    # price = str(price/100)
    output_str = "The last updated price of " + cc + " is " + price + " ," + "The price in the given currency is " + priceincurrency + " ," + "The day volume is " + dayvolume +" ," + "The market cap is " + marketcap +" ," + "The total supply is " + totalsupply +" ," + "The available supply is " + availablesupply +" ," + "The percentage change in last 1 hour is "  + percentchange_1h + " ," "The percentage change in last 24 hours is "  + percentchange_24h + " &" "The percentage change in last 7 days is " + percentchange_7d
    print output_str
    engati_format = {
"data": {
"type": "text",
"text": output_str
}
}
    # print json.dumps(engati_format)
    print output_str
    return json.dumps(engati_format, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.run()
