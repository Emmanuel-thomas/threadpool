import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.on('random_number')
def on_random_number(data):
    print(f'Received random number: {data}')

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')
    sio.wait()
