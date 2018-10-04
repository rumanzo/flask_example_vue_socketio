#!/usr/bin/env python3.6
import json
import os
import sys
import asyncio
import psutil
import time
import concurrent.futures
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_socketio import emit
from flask_socketio import SocketIO


sys.path.append(os.path.dirname(__name__))
app = Flask(__name__)
Bootstrap(app)
socketio = SocketIO(app)
thread = None
NS = "/test"


def uploadspeed(): 
    bytesc = psutil.net_io_counters(pernic=True)['eth0'].bytes_recv
    while True:
        socketio.sleep(1)
        bytescn =  psutil.net_io_counters(pernic=True)['eth0'].bytes_recv
        socketio.emit("progress", {"text": bytescn - bytesc}, namespace=NS)
        bytesc = bytescn


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1, thread_name_prefix='speed_')
loop.run_in_executor(executor, uploadspeed, )


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
