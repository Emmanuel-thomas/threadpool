import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connect')
def on_connect():
    print('Client connected')
    random_number = random.randint(1, 100)
    emit('random_number', random_number)

if __name__ == '__main__':
    socketio.run(app)
