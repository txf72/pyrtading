import requests
import json
import hmac
import hashlib
import time
from datetime import datetime

import logging
import sys
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class Balance():
    def __init__(self, currency, available):
        self.currency = currency
        self.available = available


class Ticker():
    def __init__(self, symbol, bid, ask, volume, timestamp):

        self.symbol = symbol
        self.bid = bid
        self.ask = ask
        self.volume = volume
        self.timestamp = timestamp

class Order():
    def __init__(self, symbol, side, size, ececutionType="MARKET"):
        self.symbol = symbol
        self.side = side
        self.ececutionType = ececutionType
        self.size = size



class APIClient():
    def __init__(self, access_token, account_id, symbol):
        self.access_token = access_token
        self.account_id = account_id
        self.symbol = symbol

    def get_balance(self) -> Balance:
        apiKey = self.access_token
        secretKey = self.account_id
        symbol = self.symbol
        timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
        method = 'GET'
        endPoint = 'https://api.coin.z.com/private'
        path = '/v1/account/assets'

        text = timestamp + method + path
        sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(
            text.encode('ascii')), hashlib.sha256).hexdigest()

        headers = {
            "API-KEY": apiKey,
            "API-TIMESTAMP": timestamp,
            "API-SIGN": sign
        }
        try:
            res = requests.get(endPoint + path, headers=headers)
            data = res.json()["data"][symbol]
        except V20Error as e:
            logger.error(f"action=get_balance error={e}")
            raise

        currency = data["symbol"]
        available = data["available"]

        return Balance(currency, available)

    def get_ticker(self, callback) -> Ticker:
        symbol = self.symbol
        symbol = self.coin(symbol)
        endPoint = 'https://api.coin.z.com/public'
        path = ('/v1/ticker?symbol=' + symbol)

        try:
            while True:
                res = requests.get(endPoint + path)
                req = res.json()["data"][0]
                time.sleep(5)

                symbol = req["symbol"]
                bid = float(req["bid"])
                ask = float(req["ask"])
                volume = float(req["volume"])
                timestamp = req["timestamp"]

                ticker = Ticker(symbol, bid, ask, volume, timestamp)
                callback(ticker)
        except V20Error as e:
            logger.error(f"action=get_realtime_ticker error={e}")
            raise

    def send_order (self, order:Order):

        apiKey = self.access_token
        secretKey = self.account_id

        timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
        method = 'POST'
        endPoint = 'https://api.coin.z.com/private'
        path = '/v1/order'
        reqBody = {
            "symbol": order.symbol,
            "side": order.side,
            "executionType": order.ececutionType,
            "size": order.size
        }

        text = timestamp + method + path + json.dumps(reqBody)
        sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()

        headers = {
            "API-KEY": apiKey,
            "API-TIMESTAMP": timestamp,
            "API-SIGN": sign
        }
        try:
            res = requests.post(endPoint + path, headers=headers, data=json.dumps(reqBody))
            print(json.dumps(res.json(), indent=2))
        except V20Error as e:
            logger.error(f"actionsend_order error={e}")
            raise





    def coin(self,module):
        if module == 0:
            return "JPY"
        if module == 1:
            return "BTC"
        if module == 2:
            return "ETH"
        if module == 3:
            return "BCH"
        if module == 4:
            return "LTC"
        if module == 5:
            return "XRP"
        if module == 6:
            return "XEM"
        if module == 7:
            return "XLM"
        if module == 8:
            return "BAT"
        if module == 9:
            return "OMG"
        if module == 10:
            return "XTZ"
        if module == 11:
            return "QTUM"
