import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/<path:rest>")
def main(rest=None):
    headers = flask.request.headers
    query_params = flask.request.args
    path = flask.request.path

    out = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Request Inspection</title>
    </head>
    <style>
    body {
        background-color: #282828;
        font-family: "Courier New", Courier, monospace;
    }
    table {
        width: auto;
    }
    th {
        text-align: left;
        color: #ffb000;
    }
    td {
        color: #ffb000;
    }
    tr:hover {
        background-color: rgba(28, 21, 6, 0.85);
    }
    tr {
        border-bottom: 1px solid #000000;
        padding-right: 5px;
    }
    </style>
    <body>
        <h1>Request Inspection</h1>
        <h2>URL Path: {}</h2>
        <h2>Query Parameters:</h2>
        <ul>
    """.format(path)

    for param, value in query_params.items():
        out += "<li>{}: {}</li>".format(param, value)

    out += """
        </ul>
        <h2>Headers:</h2>
        <table>
            <tr>
                <th>Header Name</th>
                <th>Header Value</th>
            </tr>
    """

    for name, value in headers.items():
        out += "<tr><td>{}</td><td>{}</td></tr>".format(name, value)

    out += """
        </table>
    </body>
    </html>
    """

    return out

if __name__ == "__main__":
    app.run()
