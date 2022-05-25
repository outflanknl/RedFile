# RedFile
A flask wsgi application that serves files with intelligence, good for serving conditional RedTeam payloads.

## quickest start
```
git clone https://github.com/outflanknl/RedFile
cd RedFile
docker-compose up
```
(or add -d to run without logging to console)

## running code
get a browser and point to:
```
http://127.0.0.1:8001/agent/one/two
```
This will launch module 'agent', the code for that module can be found on 
`RedFile/code/m/agent/__init__.py`

This example returns the request information and the agent information in a json.
note the 'key' and 'h' fields coming from the incoming function call.

 `` happy coding  ``

 ## next
 have a look at the dstart module
 This will serve a payload X times at the start of the day and thereafter serve empty.txt
 This allows for a stealhy persistence.

 Not that at the end of the init function a request call can be made to another webserver for logging purposes.
 Storage of the state is done in `data.shelve`