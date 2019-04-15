
from flask import render_template
from application import app, news_catcher
import urllib.request, json, os
    

data = news_catcher.catch_news()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', data=data)

@app.route('/update')
def update_news():
    data = news_catcher.catch_news()
    return "Success"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
