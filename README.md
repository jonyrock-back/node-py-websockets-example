# node-py-websockets-example
Example of connectivity node.js with python3 over websockets

## Server
Node.js server waits for a websocket connection. Based on [websockets/ws](https://github.com/websockets/ws) library.

```bash
cd server
npm install
npm run start
```

## Client
Python3 client connects and sends a message to the server and waits for a response. Based on [aaugustin/websockets](https://github.com/aaugustin/websockets) library.

```bash
pip3 install -r requirements.txt
python3 main.py
```