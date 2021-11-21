import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("news for today")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=4fc089f4e6864161be12ada5c362ab2b"
    news = requests.get(url).text
    newsDict = json.loads(news)
    # print(newsDict["articles"])
    arts = newsDict["articles"]
    count = 1
    for articles in arts:
        speak(f"Our {count} news is ")
        speak(articles["title"])
        count += 1