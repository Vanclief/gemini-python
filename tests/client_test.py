from geminipy.gemini import Gemini
import httpretty

client = Gemini()

TICKER_URL = 'https://api.gemini.com/v1/pubticker/'
ORDERS_URL = 'https://api.gemini.com/v1/book/'
TRADES_URL = 'https://api.gemini.com/v1/trades/'
SYMBOLS_URL = 'https://api.gemini.com/v1/symbols'


def test_should_have_correct_url():
    g = Gemini()
    assert g.api_base == 'https://api.gemini.com/v1/'


def test_should_have_api_key():
    g = Gemini('974554aed089', '2976be9e189d')
    assert g.api_key == '974554aed089'


def test_should_have_secret_key():
    g = Gemini('974554aed089', '2976be9e189d')
    assert g.api_secret == '2976be9e189d'


@httpretty.activate
def test_should_return_ticker():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"ask": "977.59","bid": "977.35","last": "977.65",' +
            '"volume": {"BTC": "2210.505328803",' +
            '"USD": "2135477.463379586263","timestamp": 1483018200000}}'
            )
    mock_url = TICKER_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = {
            "mid": 977.47,
            "bid": 977.35,
            "ask": 977.59,
            "last_price": 977.65,
            "low": 0.0,
            "high": 0.0,
            "volume": 2210.505328803,
            "timestamp": 1483018200.0
            }

    response = client.ticker(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_orderbook():

    mock_symbol = 'btcusd'
    mock_body = (
            '{"bids":[{"price":"15177.04","amount":"16.90585",' +
            '"timestamp":"1514996460"}],"asks":[{"price":"15177.05",' +
            '"amount":"2.36048769","timestamp":"1514996460"}]}'
            )
    mock_url = ORDERS_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = {
            "bids": [
                {
                    "price": 15177.04,
                    "amount": 16.90585,
                    "timestamp": 1514996460.0
                    }
                ],
            "asks": [
                {
                    "price": 15177.05,
                    "amount": 2.36048769,
                    "timestamp": 1514996460.0
                    }
                ]
            }

    response = client.orderbook(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_trades():

    mock_symbol = 'btcusd'
    mock_body = (
            '[{"timestamp": 1420088400,"timestampms": 1420088400122,' +
            '"tid": 155814,"price": "822.12","amount": "12.10",' +
            '"exchange": "gemini","type": "buy"}]'
            )
    mock_url = TRADES_URL + mock_symbol
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = [
            {"timestamp": 1420088400, "tid": 155814, "price": 822.12,
                "amount": 12.10, "exchange": "gemini", "type": "buy"}
            ]

    response = client.trades(mock_symbol)
    assert expected_response == response[1]


@httpretty.activate
def test_should_return_symbols():

    mock_body = '["btcusd","ethusd","ethbtc" ]'
    mock_url = SYMBOLS_URL
    mock_status = 200

    httpretty.register_uri(
            httpretty.GET, mock_url, body=mock_body, status=mock_status
            )

    expected_response = ["btcusd", "ethusd", "ethbtc"]

    response = client.symbols()
    assert expected_response == response[1]


