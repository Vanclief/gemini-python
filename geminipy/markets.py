from geminipy.requester import Requester
import geminipy.helpers as helpers

TICKER_URL = "pubticker/"
ORDERS_URL = "book/"
TRADES_URL = "trades/"
SYMBOLS_URL = "symbols"


class Market(object):

    def __init__(self, api_base):
        self.r = Requester(api_base)

    def get_ticker(self, symbol):
        endpoint = TICKER_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        s = (symbol[:3].upper())

        parsed_response = {}

        parsed_response['bid'] = float(response['bid'])
        parsed_response['ask'] = float(response['ask'])
        parsed_response['mid'] = ((parsed_response['bid'] +
                                  parsed_response['ask']) / 2)
        parsed_response['last_price'] = float(response['last'])
        parsed_response['low'] = float(0)
        parsed_response['high'] = float(0)
        parsed_response['volume'] = float(
                response['volume'][s])
        parsed_response['timestamp'] = float(
                response['volume']['timestamp'])/1000

        return status, parsed_response

    def get_orderbook(self, symbol):

        endpoint = ORDERS_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        for order_type in response.keys():
            for order in response[order_type]:
                for key, value in order.items():
                    order[key] = float(value)

        return status, response

    def get_trades(self, symbol):

        endpoint = TRADES_URL + symbol
        status, response = self.r.get(endpoint)

        if status != 200:
            return status, response

        return status, helpers.list_dict_to_float(response)

    def get_symbols(self):
        endpoint = SYMBOLS_URL
        return self.r.get(endpoint)
