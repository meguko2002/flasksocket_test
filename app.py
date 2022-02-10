# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = 'ABCDEFGH'
socketio = SocketIO(app, async_mode='eventlet')


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my event')
def my_message(message):
    print(message)
    emit('message', {'msg':'hello client'},broadcast=True)


if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    socketio.run(app,  port=5000, debug=True)