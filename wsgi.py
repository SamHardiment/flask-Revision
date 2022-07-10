from server import server
## default python server that flask offers is not poweerful enoughj
## So we use WSGI, a simple calling convetion for for web serveers to forward web requests to web applications in python

## Argument allows auto restart on file changes

server.run()
