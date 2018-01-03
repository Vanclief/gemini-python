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

        return status, helpers.dict_to_float(response)

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
