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
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred:{timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred {req_err}")
