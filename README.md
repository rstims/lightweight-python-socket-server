# lightweight-python-socket-server
This is my attempt at a really lightweight socket server in python.

Uses Python's socket abstraction.

First the socket is opened.

Second, the socket accepts a json string with two properties (listed below) and the json string is converted to a Dict
 - path - path to python file you want to run
 - args - any data the python file specified in the path will need to run
 
After that imp is used to load the specified python file source and save the source object in a variable.

It then calls a main function in that source object, hence each specified python file must have a main() function to run.

After receiving the ouput (which must be a string) from the specified file the output is sent back to the client.

My implementation of this was to use it with PHP to offload larger computations to python.  

It uses a standard socket so anything that can use a socket can communicate with this theoretically.

Lots of todos, this is in its very early state.
 
