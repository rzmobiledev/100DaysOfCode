import requests

params = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}
api = "https://opentdb.com/api.php"

response = requests.get(url=api, params=params)
response.raise_for_status()
question_data = response.json()['results']
