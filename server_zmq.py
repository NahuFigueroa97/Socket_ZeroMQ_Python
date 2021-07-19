import zmq
import time
host = "tcp://*:5555"

contexto = zmq.Context()
socket = contexto.socket(zmq.REP)
socket.bind(host)

while True :

    message = socket.recv()

    print("solicitud recibida %s" % message)

    time.sleep(1)

    socket.send(b"Hola soy el servidor")