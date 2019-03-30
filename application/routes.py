
from flask import render_template
from application import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Doug'}
    return render_template('index.html', user=user)

@app.route('/about')
def about():
    return 'About Page!'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
