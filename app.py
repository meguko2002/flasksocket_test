from flask import Flask, send_file
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return send_file("index.html")


@socketio.on("message")
def handle_message(data):
    emit("new_message", data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)