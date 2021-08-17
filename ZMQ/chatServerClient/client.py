import zmq

context = zmq.Context()

print("Connecting to chat server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:7777")

while True:
    msg = input('Enter your msg here: ')
    socket.send_string(msg)
    print('From server:', socket.recv().decode())
    print('')
    