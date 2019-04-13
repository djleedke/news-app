
from flask import render_template
from application import app, news_catcher
import json, os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', data=read_news())

@app.route('/news-catch')
def news-catch():
    news_catcher.catch_news()
    return "News Caught!"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

def read_news():
    print("Reading News")
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'data.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    return data
    
