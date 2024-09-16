import requests, json

API_URL = "https://us-east1-serverless-306422.cloudfunctions.net/spellchecker"

def is_misspelled(word: str) -> bool:
    PARAMS = {"word" : word}
    res = requests.get(url = API_URL + "/misspelled", params = PARAMS)

    if not res.status_code == 200:
        raise Exception("Get misspelled call failed!")

    try:
        data = res.json()
        return data.get('misspelled')

    except Exception as e:
        return e


print(is_misspelled('hello0'))
