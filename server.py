import socket #-------------importing socket----------------
from threading import Thread#-------------importing thread----------------



server= socket.socket(socket.AF_INET,socket.SOCK_STREAM) #--------------------socket creation-----------------
server.bind(("localhost",9999)) #-----------------binding socket to port number---------------
server.listen() #--------------allows client to get into server also controls the flow of clients-----------
all_party={} #-----------creating a disctionary to store every individual client----------------



def party_thread(party): #---------------------Independent thread for each client-------------------
    while True:
        try:
            msg=party.recv(1024)#------------recieve msg sent by the participants and display it to other members-----------
            for f in all_party:#---------msg sent my one participant should be visible to all----------
                f.send(msg)
        except:
            for f in all_party:
                f.send(f"{name} has left the chat".encode())
            del all_party[party]
            party.close()
            break

            

while True : #------------to continously accept participants-----------------
    print("Waiting for connection.....")
    party , address = server.accept() #--------------returns two values (socket, address)-----------------

    print("Connection Established")
    name=party.recv(1024).decode() #------------asking participants for their username-------------
    all_party[party]=name
    for f in all_party:
        f.send(f"{name} has joined the chat".encode())

   
    all_party[party]=name #----------------to take key as party and set their values as name-------------
    thread=Thread(target=party_thread,args=(party,))#----------------Making a thread---------------
    thread.start()
