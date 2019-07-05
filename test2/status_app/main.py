import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def status():
    app_version = os.environ['APP_VERSION']
    commit_sha = os.environ['COMMIT_SHA']
    return render_template('status.j2', app_version=app_version, commit_sha=commit_sha)
