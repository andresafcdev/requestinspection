import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    out = '<h1>Request Information:</h1>'
    out += '<p>URI Path: ' + flask.request.path + '</p>'
    out += '<p>Query: ' + str(flask.request.args) + '</p>'
    out += '<h1>Request Headers:</h1>'
    for line in flask.request.headers:
        out += '<p>' + str(line) + '</p>'
    return out
