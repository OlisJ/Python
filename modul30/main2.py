import requests
uri ="https://wikipedia.org/"

try:
    response = requests.get(uri)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as con_err:
    print(f"Connection error occurred: {con_err}")