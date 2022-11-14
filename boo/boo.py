import socket
from time import sleep

from playsound import playsound
LISTEN_PORT = 8888
listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding to local port 80
server_address = ('', LISTEN_PORT)
listening_sock.bind(server_address)

# Listen for incoming connections
listening_sock.listen(1)

# Create a new conversation socket
client_soc, client_address = listening_sock.accept()


while True:
    msg = client_soc.recv(1000024).decode()
    print(msg)
    if("hi" in msg):
        playsound('C:/Users/magshimim/Downloads/be  o.mp3')
    else:
        print("bro")
    sleep(1)


