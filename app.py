import flask

app = flask.Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello(path):
    headers = flask.request.headers
    query_params = flask.request.args

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Request Information</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                padding: 20px;
                margin: 0;
            }
            h1 {
                color: #333333;
                margin-bottom: 20px;
            }
            p {
                color: #555555;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Request Information:</h1>
        <p>URI Path: {path}</p>
        <p>Query Parameters: {query_params}</p>
        <h1>Request Headers:</h1>
        {headers}
    </body>
    </html>
    """.format(path=path, query_params=query_params, headers=format_headers(headers))

def format_headers(headers):
    formatted_headers = ""
    for name, value in headers.items():
        formatted_headers += "<p><strong>{}</strong>: {}</p>".format(name, value)
    return formatted_headers
