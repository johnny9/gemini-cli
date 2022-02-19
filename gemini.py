import argparse
import yaml
import datetime
import requests


CONFIG_PATH = '~/.gemini.yaml'
GEMINI_BASE_URL = 'https://api.gemini.com'


def parse_configuration():
    with open(CONFIG_PATH, 'r') as file:
        return yaml.safe_load(file)

def new_order(type, )
    endpoint = "/v1/order/new"
    url = GEMINI_BASE_URL + endpoint

    gemini_api_key = "mykey"
    gemini_api_secret = "1234abcd".encode()

    t = datetime.datetime.now()
    payload_nonce =  str(int(time.mktime(t.timetuple())*1000))

    payload = {
        "request": "/v1/order/new",
        "nonce": payload_nonce,
        "symbol": "btcusd",
        "amount": "5",
        "price": "3633.00",
        "side": "buy",
        "type": "exchange limit",
        "options": ["maker-or-cancel"]
    }

    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

    request_headers = { 'Content-Type': "text/plain",
                        'Content-Length': "0",
                        'X-GEMINI-APIKEY': gemini_api_key,
                        'X-GEMINI-PAYLOAD': b64,
                        'X-GEMINI-SIGNATURE': signature,
                        'Cache-Control': "no-cache" }

    response = requests.post(url,
                             data=None,
                             headers=request_headers)

new_order = response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers()
    order_command = commands.add_parser('order')
    order_command.add_argument('direction')
    order_command.add_argument('type')

    args = parser.parse_args()
