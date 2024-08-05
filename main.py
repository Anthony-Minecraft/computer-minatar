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
from urllib import request, parse
### CLASSES ###
class TCPTarget:
    def __init__(self, target:dict) -> None:
        self.IP:str = target['IP']
        self.PORT:int = target['PORT'] or 0
        self.FORMS:dict = target['FORMS']
class HTTPTarget:
    def __init__(self, target:dict) -> None:
        self.URI:str = target['URI']
        self.FORMS:dict = target['FORMS']
class Clientier:
    def __init__(self, target:dict) -> None:
        # External TCP Connection Parameters
        self.Types = {
            "TCP": TCPTarget(target['TCP']),
            "HTTP-GET": HTTPTarget(target['HTTP-GET']),
            "HTTP-POST": HTTPTarget(target['HTTP-POST'])
        }
        # Computer/User Information
        self.INFO:dict = {
            "THIS_NAME": platform.node(),
            "THIS_IP": socket.gethostbyname(socket.gethostname()),
            "THIS_USER": os.getlogin()
        }
    def Fire(self, sendingType:str, formType:str) -> None:
        # TODO: Implement login
        match sendingType:
            case "TCP":
                formated:str = self.FormatString(self.Types['TCP'].FORMS[formType])
                print(formated) # DEBUG
                self.SendDataTCP(formated)
            case "HTTP-GET":
                print(self.FormatString(self.Types['HTTP-GET'].FORMS[formType])) # DEBUG
            case "HTTP-POST":
                print(self.FormatString(self.Types['HTTP-POST'].FORMS[formType])) # DEBUG
        pass
    def FormatString(self, form) -> str:
        for key, value in self.INFO.items():
            form = form.replace(f"$[{key}]", value)
        return form
    def SendDataTCP(self, data:str) -> bytes:
        # Send data out
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
        adr:tuple = (self.Types['TCP'].IP, self.Types['TCP'].PORT) # Create a tuple with the target IP and port
        s.connect(adr) # Connect to the target IP and port
        s.send(data) # Send the data
        # Process incoming data
        incoming:bytes = s.recv(self.BUFFER_SIZE) # Receive the incoming data
        s.close() # Close the socket
        return incoming # Return the incoming data
        # NOTE: More on sockets: https://wiki.python.org/moin/TcpCommunication
    def SendDataHTTPGet(self, data:str) -> str:
        contents:str = request.urlopen(f"{self.Types['HTTP-GET'].URI}?client=minatar&{data}").read()
        return contents
    def SendDataHTTPPost(self) -> str:
        dataBytes = parse.urlencode(self.INFO).encode()
        req =  request.Request(f"{self.Types['HTTP-GET'].URI}?client=minatar", data=dataBytes)
        resp = request.urlopen(req)
        return resp.read().decode("utf-8")
### MAIN ###
def main() -> None:
    # Get config data
    target = None
    with open("config.json", "r") as f:
        target = json.load(f)
    client:Clientier = Clientier(target) # Create client object
    args:list[str] = sys.argv # Get command line arguments
    # Check if TCP or HTTP
    sendingType:str
    if "TCP" in args: sendingType = "TCP"
    elif "HTTP-GET" in args: sendingType = "HTTP-GET"
    elif "HTTP-POST" in args: sendingType = "HTTP-POST"
    else:
        print("ERROR: Invalid arguments (missing <TCP|HTTP-GET|HTTP-POST>?)")
        return
    # Check if login or logout
    if "login" in args:
        client.Fire(sendingType, "Login")
    elif "logout" in args:
        client.Fire(sendingType, "Logout")
    else:
        print("ERROR: Invalid arguments (missing <login|logout>?)")
        return

if (__name__ == "__main__") and シ:
    main()