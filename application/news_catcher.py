from application import config
import urllib.request, json, time, datetime

def catch_news():
    print("Calling news_catch")
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=" + config.newsapi_key

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
                    
    return data;
