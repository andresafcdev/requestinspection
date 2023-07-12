import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    headers = flask.request.headers
    query_params = flask.request.args
    path = flask.request.path

    with open("template.html", "r") as file:
        template = file.read()

    return template.format(path=path, query_params=query_params, headers=format_headers(headers))

def format_headers(headers):
    formatted_headers = ""
    for name, value in headers.items():
        formatted_headers += "<p><strong>{}</strong>: {}</p>".format(name, value)
    return formatted_headers
