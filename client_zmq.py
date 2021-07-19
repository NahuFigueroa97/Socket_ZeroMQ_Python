import zmq
import time
host = "tcp://localhost:5555"

contexto = zmq.Context()

print ("Conectando al servidor")
socket = contexto.socket(zmq.REQ)
socket.connect(host)

for solicitud in range(10) :

    print("enviando solicitud %s" %solicitud)
    socket.send(b"Hola soy el cliente")

    message = socket.recv()
    print(message)
