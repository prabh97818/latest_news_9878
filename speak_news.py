from win32com.client import Dispatch
import requests
import json

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

url = f"http://newsapi.org/v2/top-headlines?country=in&apiKey={input('Please enter your API Key(without spaces): ')}"
re = requests.get(url)
data = re.text
parsed = json.loads(data)
news_dict = parsed["articles"]
speak("Hello, Here are top ten news of the day...")
count = 1
for article in news_dict:
    speak(f"{count}...{article['title']}")
    if count ==  10:
        break
    count += 1
speak("Thanks For listening")