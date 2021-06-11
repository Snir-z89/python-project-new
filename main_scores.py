from flask import Flask, request
from utils import scores_file_name, bad_return_code

app = Flask(__name__)


@app.route('/score', methods=['GET'])
def score_server():
    bad_code = str(bad_return_code)
    user_score = open(scores_file_name, "r")
    print_score = str(user_score.read())

    html = """<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body><h1>The score is <div id="score"> """ + print_score + """</div></h1></body>
    </html>"""

    bad_html = """<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body><h1><div id="score" style="color:red"> """ + bad_code + """</div></h1></body>
    </html>"""

    if request.method == 'GET':
        return html
    else:
        return bad_html


app.run(host="127.0.0.1", port=5001, debug=True)
