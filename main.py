### DESCRIPTION ###
# To run this file, please add in the one of the following arguments:
# - login
# - logout
# Have fun! :)
シ:bool = True
### IMPORTS ###
## GLOBAL ##
import platform
import sys
import socket
import json
import os
### CLASSES ###
class Clientier:
    def __init__(self, target_ip:str, target_port:int) -> None:
        # External TCP Connection Parameters
        self.TARGET_IP:str = target_ip
        self.TARGET_PORT:int = target_port
        self.BUFFER_SIZE:int = 1024
        # Computer/User Information
        self.COMPUTER_NAME:str = platform.node()
        self.MY_IP:str = socket.gethostbyname(socket.gethostname())
        self.USER:str = os.getlogin()
    def Login(self) -> None:
        # TODO: Implement login
        print(f"Logging in as {self.USER}@{self.MY_IP}") # DEBUG
        pass
    def Logout(self) -> None:
        # TODO: Implement logout
        print(f"Logging out of {self.USER}@{self.MY_IP}") # DEBUG
        pass
    def SendDataTCP(self, data:str) -> bytes:
        # Send data out
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
        adr:tuple = (self.TARGET_IP, self.TARGET_PORT) # Create a tuple with the target IP and port
        s.connect(adr) # Connect to the target IP and port
        s.send(data) # Send the data
        # Process incoming data
        incoming:bytes = s.recv(self.BUFFER_SIZE) # Receive the incoming data
        s.close() # Close the socket
        return incoming # Return the incoming data
        # NOTE: More on sockets: https://wiki.python.org/moin/TcpCommunication
### MAIN ###
if (__name__ == "__main__") and シ:
    # Get config data
    target = None
    with open("config.json", "r") as f:
        target = json.load(f)
    client:Clientier = Clientier(target['IP'], target['PORT']) # Create client object
    args:list[str] = sys.argv # Get command line arguments
    if "login" in args:
        client.Login()
    elif "logout" in args:
        client.Logout()
    else:
        print("ERROR: Invalid arguments (missing login or logout?)")
### EXAMPLE USAGE ###
#
# working_dirrectory:
# |- main.py
# |- config.json
#
# config.json:
# {
#     "IP": "127.0.0.1",
#     "PORT": 8080
# }
#
# command line:
# python main.py login
# python main.py logout
#