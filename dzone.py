from flask import Flask

from flask import jsonify

from flask import request

import urllib2,json,random
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

@app.route('/funfacts', methods=['GET'])

def getFunFact():
    list=["Satoshi Nakamoto Bitcoin created in the 2008th year. It is believed that Satoshi Nakamoto - a pseudonym bitcoin creator. The whole world is trying to solve the mystery of his true identity.","Every day produces about 3,600 new Bitcoins. Coins are blocks in a process called 'mining'.",
    "The first transfer Bitcoin transaction took place on January 21, 2009. Satoshi himself translated 100 BTC Hal Finney - another tsiferpanku and cryptography (Hal Finney)",
    "So far, attempts to reveal the identity of the mysterious Satoshi Nakamoto, but to no avail. The latest version of the results Satoshi - Dorian caused a great stir, but it was quickly disproved.",
    "For the first 5 years, the price cryptocurrency - Bitcoin, grew from $ 0 to $ 1,000.","The first million bitcoins was namaynen by Satoshi Nakamoto, and is likely to still belongs to him. Journalists and curious still trying to find wallets Satoshi Nakamoto, to get on his trail, but the creator of Bitcoin remains calm.","The maximum amount of Bitcoins that will be produced - 21 million coins. Today already produced about 12 million bitcoins. extraction algorithm is complicated and reduces the number of coins found in 2 times every few years, so the process of mining uneven.","The 2140 will produce (namaynyat) last Bitcoin.",
    "Attempts to create the physical equivalent of Bitcoin (in the form of coins). In fact Casascius- is none other than the 'cool wallets' printed on them holographic access code key only cast in the form factor of the coin. That coin Casascius we see all these beautiful photos with 'coins' Bitcoin.",
    "Small island jurisdiction of Alderney, also announced plans for the country's coinage physical equivalents of Bitcoin.",
    "Only 36% of the total volume of coins produced have been observed in any transaction. The remaining 64% of the coins after his appearance were never used.",
    "Unlike fiatnyh physical money, all transactions - the story moving any funds from one account to another, forever written inside Blockchain - global and distributed completely open database containing details of all Bitcoin-wallets worldwide.",
    "In our time, in the code Bitcoin 77 thousand lines of code, of which 70 thousand are written in C ++. And in the very first working version numbered 0.1.0 it was only a 14-thousand. Lines of code in C ++. Bitcoin began as a small project by today's standards. For comparison, in the Linux kernel code has more than 15 million lines of code.",
    "Bloomberg journalist who is not familiar with the safety regulations Bitcoin, inadvertently revealed the private key (in the form of a QR-code) your Bitcoin wallet-live. For that immediately paid the price - his money was stolen by one of the audience, but then, according to rumors, the money was returned to the journalist.",
    "A resident of the UK named James Houels inadvertently threw a hard drive with a key from the wallet, which was (and probably still is) 7500 Bitcoins. It is about 5 million dollars at the current rate."]

    engati_format = {
    "data": {
    "type": "text",
    "text": list[random.randint(0,len(list)-1)]}
    }
    return json.dumps(engati_format)

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
