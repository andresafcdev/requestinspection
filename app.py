import flask
import os.path

app = flask.Flask(__name__)

@app.route("/")
@app.route("/<path:rest>")
def main(rest=None):
    out = """
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Backend Server HTTP header print</title>
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
                background-color: #1c1506d8;
            }
            tr {
                border-bottom: 1cm solid #000000;
                padding-right: 5cm;
            }
        </style>
    </head>
    <body>
        <section style="background-color:#fff">
            <div class="container">
                <div class="row">
                    <br>
                    <h2> Backend Server HTTP header print</h2>
                    <br>
                </div>
            </div>
        </section>
        <div class="content">
            <div class="content-text">
                <table>
                    <tr>
                        <th>Header name</th>
                        <th>Header value</th>
                    </tr>
    """

    for value in flask.request.headers.keys():
        out += f"""
                    <tr>
                        <td>{value}</td>
                        <td>{flask.request.headers[value]}</td>
                    </tr>
        """

    out += """
                </table>
            </div>
        </div>
    </body>
    </html>
    """

    path = flask.request.path
    query = flask.request.query_string.decode("utf-8")

    return out.format(path=path, query=query)

if __name__ == "__main__":
    app.run()
