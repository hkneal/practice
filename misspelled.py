import requests, json

api_url = "https://us-east1-serverless-306422.cloudfunctions.net/spellchecker"

def is_misspelled(word: str) -> bool:
    PARAMS = {"word" : word}
    res = requests.get(url = api_url + "/misspelled", params = PARAMS)
    print(res)
    if res.status_code == 200:
        try:
            data = res.json()
            print(data)
            return data['misspelled']

        except Exception as e:
            return e

    raise Exception("Get misspelled call failed!")

print(is_misspelled('helloo'))