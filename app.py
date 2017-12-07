import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)


@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect', namespace='/telemetries_found')
def connect(sid, environ):
    print("connect ", sid)


@sio.on('beacons_discovered')
def message(sid, data):
    print("message ", data)

@sio.on('telemetries_found')
def message(sid, data):
    print("message ", data)

@sio.on('nearable_discovered')
def message(sid, data):
    print("message ", data)



if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)
