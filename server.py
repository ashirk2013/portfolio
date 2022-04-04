from email.policy import default
from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder="build", static_url_path='/')

@app.route('/heartbeat')
def heartbeat():
    return jsonify({"status": "healthy"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file('index.html')