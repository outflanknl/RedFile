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
http://127.0.0.1:8001/test1/one/two?three=drie
```
This will launch module 'agent', the code for that module can be found on 
`RedFile/code/m/test1/__init__.py`

This example returns the request information and the agent information in a json.
note the 'agent' field coming from the incoming function call, all other details can be obtained from the flask request object

 `` happy coding  ``

 ## daystart
 have a look at the dstart module:
 `http://127.0.0.1:8001/daystart/one/two?three=drie`
 This will serve a payload X times at the start of the day and thereafter serve empty.txt
 This allows for a stealhy persistence.

 Not that at the end of the init function a request call can be made to another webserver for logging purposes.
 Storage of the state is done in `data.shelve`

## keyer
keyer will serve unique contect for a certain key.
The key is a string appended with an md5 of "that first half string + a secret". this means new keys can be generated on the fly and will be valid as often ad you want.

example:
`http://127.0.0.1:8001/keyer/7103f096074271321c6cebd743ac8d9b5b6b52d65f7e16a8a08a33570275a750/`

## onePerUser
Now next level, if you can build a payload that will include the username in the call have a look at:
```
http://127.0.0.1:18080/onePerUser/?u=John
http://127.0.0.1:18080/onePerUser/?u=Alice
http://127.0.0.1:18080/onePerUser/?u=NotExisting
```
You will see that john.txt and alice.txt get served once, notextist.txt isn't available so error.txt will be served once there.
All calls after that point will serve 'default.txt'. 

Consider a cronjob that deletes data.shelve every night to have a select group of users being served a payload once a day :)

# OPSEC
ofcourse, this is proof of concept code. Consider using a proxy like haproxy to rewrite calls and have them end up at the correct module, also consider building encryption of obfuscation on the url and parameter.