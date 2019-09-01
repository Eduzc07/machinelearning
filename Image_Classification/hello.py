# Flask utils
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
