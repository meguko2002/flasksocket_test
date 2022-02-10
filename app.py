# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
# app.secret_key = 'ABCDEFGH'
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on("message", namespace='/test')
def handleMessage(data):
    emit("new_message", data, broadcast=True)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    socketio.run(app)