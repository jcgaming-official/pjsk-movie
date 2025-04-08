from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    app.run(host="0.0.0.0", port=5000)
