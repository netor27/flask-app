import os
from datetime import datetime
import socket
from flask import Blueprint

timeApi = Blueprint('timeApi', __name__, url_prefix="/time")

@timeApi.route("/")
def index():
    hostname = socket.gethostname()
    html = "<h1>Hello world!</h1>" \
           "<h3>This is a test view to show the current time</h3>" \
           "<b>host:</b> {hostname}<br/>" \
           "<b>time:{time}<br/>"
    time = str(datetime.now())
    return html.format(hostname=hostname, time=time)
