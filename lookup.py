import requests

lan = "en"


def getDefination(word_id):
    api = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id
    res = requests.get(api).json()
    result = f"{res[0]['word']} - {res[0]['phonetic']}"
    for m in res[0]['meanings']:
        result += f"\n\n{m['partOfSpeech']}"
        for d in m['definitions']:
            result += f"\n{d['definition']}"
    return result


def getAudio(word_id):
    api = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word_id
    res = requests.get(api).json()
    voice = res[0]['phonetics'][0]['audio']
    print(voice)
    return voice


if __name__ == "__main__":
    print(getDefination("apple"))
