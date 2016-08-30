from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'counter.db')))


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.route("/request-counter", methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'HEAD', 'TRACE', 'CONNECT', 'PUT'])
def request_counter():
    print(request.method)
    return render_template("request_counter.html")


if __name__ == "__main__":
    app.run(debug=True)
