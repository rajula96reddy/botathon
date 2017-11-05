from flask import Flask

from flask import jsonify

from flask import request

import urllib2,json
app = Flask(__name__)

@app.route('/currency', methods=['GET'])

def getCurrencies():
    cc1 = request.args.get('cryptocurrency')
    # cc ='BTC'
    if (cc1 == '1'):
        cc = 'BTC'
    elif (cc1 == '2'):
        cc = 'LTC'
    elif (cc1 == '3'):
        cc = 'ETH'
    elif (cc1 == '4'):
        cc = 'ZEC'
    elif (cc1 == '5'):
        cc = 'DASH'
    elif (cc1 == '6'):
        cc = 'XRP'
    elif (cc1 == '7'):
        cc = 'XMR'            
    c = request.args.get('currency')
    # c= 'USD'
    url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+str(cc)+"&tsyms="+str(c)
    print url
    # url="https://api.coinsecure.in/v1/exchange/ticker"
    cc = str(cc)
    c = str(c)
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    price = data['DISPLAY'][cc][c]['PRICE']
    open_day = data['DISPLAY'][cc][c]['OPENDAY']
    low_day = data['DISPLAY'][cc][c]['LOWDAY']
    high_day = data['DISPLAY'][cc][c]['HIGHDAY']
    # priceincurrency = str(data[0]["price_"+c]) + " " + str(c.upper())
    # dayvolume = str(data[0]["24h_volume_"+c]) + " " + str(c.upper())
    # marketcap = str(data[0]["market_cap_"+c]) + " " + str(c.upper())
    # totalsupply = data[0]["total_supply"]
    # availablesupply = data[0]["available_supply"]
    # percentchange_1h = data[0]["percent_change_1h"]
    # percentchange_24h = data[0]["percent_change_24h"]
    # percentchange_7d = data[0]["percent_change_7d"]
    # price = str(price/100)
    output_str = "The price of " + cc + " in " + c+ " is " + price + ", today's open day price is "+ open_day+ ", today's lowest price is "+ low_day+", today's highest price is "+high_day
    # print output_str
    engati_format = { "data": {
    "type": "text", "text": output_str
    }
    }
    # print json.dumps(engati_format)
    print output_str
    return json.dumps(engati_format, sort_keys=True, indent=4, ensure_ascii=False)

@app.route('/currencyCompare', methods=['GET'])

def compareCurrencies():
    cc1 = request.args.get('cryptocurrency1')
    # cc ='BTC'
    if (cc1 == '1'):
        cc = 'BTC'
    elif (cc1 == '2'):
        cc = 'LTC'
    elif (cc1 == '3'):
        cc = 'ETH'
    elif (cc1 == '4'):
        cc = 'ZEC'
    elif (cc1 == '5'):
        cc = 'DASH'
    elif (cc1 == '6'):
        cc = 'XRP'
    elif (cc1 == '7'):
        cc = 'XMR'       
    cc2 = request.args.get('cryptocurrency2')
    if (cc2 == '1'):
        cc0 = 'BTC'
    elif (cc2 == '2'):
        cc0 = 'LTC'
    elif (cc2 == '3'):
        cc0 = 'ETH'
    elif (cc2 == '4'):
        cc0 = 'ZEC'
    elif (cc2 == '5'):
        cc0 = 'DASH'
    elif (cc2 == '6'):
        cc0 = 'XRP'
    elif (cc2 == '7'):
        cc0 = 'XMR'   
    # c= 'USD'
    url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+str(cc)+","+str(cc0)+"&tsyms=USD"
    # print url
    # url="https://api.coinsecure.in/v1/exchange/ticker"
    # cc1 = str(cc1)
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    price1 = data['RAW'][cc]['USD']['PRICE']
    
    price2 = data['RAW'][cc0]['USD']['PRICE']


    if(price1 > price2):
        output_str = cc + " is leading " + cc0 + " by " + str(round(((price1-price2)/price1)*100,2)) + "%"
    elif(price2 > price1):
        output_str = cc0 + " is leading " + cc + " by " + str(round(((price2-price1)/price2)*100,2)) + "%"
    else:
        output_str = cc0 + " is equal to " + cc
    # print output_str
    engati_format = { "data": {
    "type": "text", "text": output_str
    }
    }
    # print json.dumps(engati_format)
    print output_str
    return json.dumps(engati_format, sort_keys=True, indent=4, ensure_ascii=False)

@app.route('/movie', methods=['GET'])

def getMovies():
    a = request.args.get('type')
    key = "11a50d9e0d4e6e2f636e6af1cf440919"
    if(a == "movie"):
        url = "https://api.themoviedb.org/3/movie/popular"+"?language=en-US&api_key="+key
        # payload = "{}"
        response = urllib2.urlopen(url)
        # url="https://api.coinsecure.in/v1/exchange/ticker"
        # response = urllib2.urlopen(url)
        data = json.loads(response.read())
        textdata=""
        for i in range(len(data["results"])):
            textdata = textdata +", "+ str(data["results"][i]["title"])
        engati_format = {
    "data": {
    "type": "text",
    "text": "The list of popular movies are: " + textdata}
    }
        return json.dumps(engati_format)

    elif(a == "tvshow"):
        key = "11a50d9e0d4e6e2f636e6af1cf440919"
        url = "https://api.themoviedb.org/3/tv/popular"+"?language=en-US&api_key="+key
        # payload = "{}"
        response = urllib2.urlopen(url)
        # url="https://api.coinsecure.in/v1/exchange/ticker"
        # response = urllib2.urlopen(url)
        data = json.loads(response.read())
        textdata=""
        for i in range(len(data["results"])):
            textdata = textdata +", "+ str(data["results"][i]["name"])
        engati_format = {
    "data": {
    "type": "text",
    "text": "The list of popular movies are: " + textdata}
    }
        return json.dumps(engati_format)

@app.route('/search', methods=['GET'])

def getDetails():
    a = request.args.get('type')
    query = str(request.args.get('search'))
    key = "11a50d9e0d4e6e2f636e6af1cf440919"
    if(a == "movie"):
        url = "https://api.themoviedb.org/3/search/movie"+"?language=en-US&query="+query+"&api_key="+key
        print url
        # payload = "{}"
        response = urllib2.urlopen(url)
        # url="https://api.coinsecure.in/v1/exchange/ticker"
        # response = urllib2.urlopen(url)
        data = json.loads(response.read())
        title = str(data['results'][0]['title'])
        vote_average = str(data['results'][0]['vote_average'])
        release_date = str(data['results'][0]['release_date'])
        overview = data['results'][0]['overview']
        engati_format = {
    "data": {
    "type": "text",
    "text": "The details of the movie with the nearest match are Title: "+ title + " Release Date: " + release_date + " Vote Average: " + vote_average + " Overview: " + overview}
    }
        return json.dumps(engati_format)

    # elif(a == "tvshow"):
    #     key = "11a50d9e0d4e6e2f636e6af1cf440919"
    #     url = "https://api.themoviedb.org/3/search/tv"+"?language=en-US&query="+query+"&api_key="+key
    #     # payload = "{}"
    #     response = urllib2.urlopen(url)
    #     # url="https://api.coinsecure.in/v1/exchange/ticker"
    #     # response = urllib2.urlopen(url)
    #     data = json.loads(response.read())
    #     title = data['results'][0]['name']
    #     vote_average = data['results'][0]['vote_average']
    #     first_air_date = data['results'][0]['first_air_date']
    #     overview = data['results'][0]['overview']
    #     engati_format = {
    # "data": {
    # "type": "text",
    # "text": "The details of the movie with the nearest match are Title: "+ title + " First Air Date: " + first_air_date + " Vote Average: " + vote_average + " Overview: " + overview}
    # }
    #     return json.dumps(engati_format)

if __name__ == '__main__':
    app.run()
