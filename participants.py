import socket
from threading import Thread


name=input("enter your username")
party= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
party.connect(("localhost",9999))
party.send(name.encode())


def send(party):
    while True:
        data= f'{name}:{input(" ")}'
        party.send(data.encode())
    

def receive(party):
    while True:
        try:
            data=party.recv(1024).decode()
            print(data)
        except:
            party.close()
            break

thread1=Thread(target=send,args=(party,))
thread1.start()
thread2=Thread(target= receive,args=(party,))
thread2.start()
