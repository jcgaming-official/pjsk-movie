from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Root route to serve the index.html from the 'templates' folder
@app.route('/')
def index():
    return render_template('index.html')  # Flask will automatically look for 'index.html' in the 'templates' folder

@app.route('/getbranches', methods=['POST'])
def get_branches():
    url = "https://www.robinsonsmovieworld.com/webservice/getbranchesbymovienewadvance"
    movie_name = request.json.get("movieName")

    headers = {
        "sec-ch-ua-platform": "\"Android\"",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0",
        "accept": "application/json"
    }

    params = {
        "movieName": movie_name
    }

    res = requests.post(url, headers=headers, params=params)
    return jsonify(res.json())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
