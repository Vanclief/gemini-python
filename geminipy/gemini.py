from geminipy.markets import Market


class Gemini(object):

    def __init__(self, key=None, secret=None):
        self.api_key = key
        self.api_secret = secret
        self.api_base = 'https://api.gemini.com/v1/'
        self.name = 'Gemini'
        self.market = Market(self.api_base)

    def ticker(self, symbol):
        """
        Get a high level overview of the state of the market.
        Parameters
        ----------
        symbol : string
            Symbol of the market
        Returns
        -------
        dict
            {
                "mid":"244.755",
                "bid":"244.75",
                "ask":"244.76",
                "last_price":"244.82",
                "low":"244.2",
                "high":"248.19",
                "volume":"7842.11542563",
                "timestamp":"1444253422.348340958"
            }
        """

        return self.market.get_ticker(symbol)

    def orderbook(self, symbol):
        """
        Get the full order book.
        Parameters
        ----------
        symbol : string
            Symbol of the market
        Returns
        -------
        array
            {
            "bids":[{
                "price":"574.61",
                "amount":"0.1439327",
                "timestamp":"1472506127.0"
            }, ... ],
            "asks":[{
                "price":"574.62",
                "amount":"19.1334",
                "timestamp":"1472506126.0"
            }, ...]
        """

        return self.market.get_orderbook(symbol)

    def trades(self, symbol):
        """
        Get a list of the most recent trades for the given symbol.
        Parameters
        ----------
        symbol : string
            Symbol of the market
        Returns
        -------
        array
            [
            {
            "timestamp":1444266681,
            "tid":11988919,
            "price":"244.8",
            "amount":"0.03297384",
            "exchange":"Kraken",
            "type":"sell"
            },
            ...
         ]
        """

        return self.market.get_trades(symbol)

    def symbols(self):
        """
        A list of symbol names.
        Returns
        -------
        array
            ["btcusd","ltcusd", "ltcbtc", ...]
        """

        return self.market.get_symbols()
