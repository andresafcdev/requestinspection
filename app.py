import flask
import os.path

app = flask.Flask(__name__)

@app.route("/")
@app.route("/<path:rest>")
def main(rest=None):
    out = '''
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
                    <h2>Backend Server HTTP header print</h2>
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
    '''

    # Add request URI path
    out += f'\n\t\t\t<tr>\n\t\t\t\t<td>Request URI path</td>\n\t\t\t\t<td>{flask.request.path}</td>\n\t\t\t</tr>'

    # Add request query
    out += f'\n\t\t\t<tr>\n\t\t\t\t<td>Request query</td>\n\t\t\t\t<td>{flask.request.query_string.decode()}</td>\n\t\t\t</tr>'

    # Add headers
    for name, value in flask.request.headers.items():
        out += f'\n\t\t\t<tr>\n\t\t\t\t<td>{name}</td>\n\t\t\t\t<td>{value}</td>\n\t\t\t</tr>'

    out += '''
                </table>
            </div>
        </div>
    </body>
    </html>
    '''

    # Handle User-Agent and health probe requests
    if 'User-Agent' not in flask.request.headers or flask.request.headers['User-Agent'] == 'Edge Health Probe':
        with open('healthprobe.txt', 'w') as file:
            file.write(out)

    path = flask.request.path.split('/')
    if path[3].isdigit():
        status = int(path[3])
        if status >= 400:
            flask.abort(status)
        else:
            return out, status
    elif path[3] == 'healthprobe':
        if os.path.exists('healthprobe.txt'):
            try:
                with open('healthprobe.txt', 'r') as file:
                    out = file.read()
            except:
                pass
            return out
        else:
            return 'No Health Probe yet'
    else:
        return out
