import requests

def get_all_languages():
    return "English", "Russian", "German", "Chinese", "Japanese"

def translate(text, to_language):
    url = " "
    headers = {
        "X-RapidAPI-Key": " ",
        "X-RapidAPI-Host": " "
    }
    response = requests.request(url, str(headers))
    json_data = response.json()
    print(json_data['data']['translations'][0]['translatedText'])

    while True:
        translate(input(f'Text in {requests}:'))

def translate_file(path, to_language):
    with open(path, 'r') as file:
        text = file.read()
        return translate(text, to_language)

