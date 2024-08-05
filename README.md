# Minatar Monitar

This is a simple application for executing an external connection on login and logout for community computers. 
Runs in python in this one file, no PIP libraries needed. 
Still a WIP (Work In Progess), so feel free to report any errors or sugestion here.

--Anthony Smith

# Config

Along with the main application, there needs to be a "config.json". 
Example: 
```json
{
    "TCP": {
        "IP": "127.0.0.1",
        "PORT": 8080,
        "FORMS":  {
            "Login": "tcp login name $[THIS_NAME], ip $[THIS_IP], user $[THIS_USER]",
            "Logout": "tcp logout name $[THIS_NAME], ip $[THIS_IP], user $[THIS_USER]"
        }
    },
    "HTTP-GET": {
        "URI": "http://127.0.0.1:8080",
        "FORMS": {
            "Login": "name=$[THIS_NAME]&ip=$[THIS_IP]&user=$[THIS_USER]&type=login",
            "Logout": "name=$[THIS_NAME]&ip=$[THIS_IP]&user=$[THIS_USER]&type=logout"
        }
    },
    "HTTP-POST": {
        "URI": "http://127.0.0.1:8080",
        "FORMS": {
            "Login": "",
            "Logout": ""
        }
    }
}
```

## HTTP-GET / HTTP-POST

The HTTP areas of the config file contains the information for sening to a HTTP server. 
It contain these properties: 

* `URI`: URI of the HTTP server.
* `FORMS`: Data form to send (see below).

## TCP

The TCP area of the config file contains the information for sending to a TCP listener server. 
It contain these properties: 

* `IP`: IP of the listening server.
* `PORT`: TCP port on the listening server.
* `FORMS`: Data form to send (see below).

## FORMS

The Form is the Format of the data that will be sent. It conatins regular text, and variables.
The variables are conatined within brackets with a dollar sign in front (like `$[THIS]`). 
Here are the accepted variables: 

* `THIS_NAME`: Name of the computer.
* `THIS_IP`: IP of the computer.
* `THIS_USER`: Current logged in user.

For the HTTP requests, there is a special syntax that they should follow. 
This should reflect the text that follows the question mark. 
An acceptable example is `name=$[THIS_NAME]&ip=$[THIS_IP]` 
Note that for HTTP-POST, it will automatically send all the user data in a json post package, 
so the GET data is not used. However, for the current state, you cannot forget to add the FORMS 
data for HTTP-POST.