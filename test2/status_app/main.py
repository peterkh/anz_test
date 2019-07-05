"""
Simple flask app that returns a /status end point.
"""
import os
from flask import Flask
from flask import render_template
APP = Flask(__name__)

@APP.route("/status")
def status():
    """
    Return app status when /status requested.
    """
    app_version = os.environ['APP_VERSION']
    commit_sha = os.environ['COMMIT_SHA']
    return render_template('status.j2', app_version=app_version, commit_sha=commit_sha)
