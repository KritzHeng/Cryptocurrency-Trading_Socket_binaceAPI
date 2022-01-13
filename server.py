# นาย คริษฐ์คณิน เฮงนิรันดร์ 6210450041
# นาย ณัฐดนัย คุ้มศิริ 6210450563
from dotenv import load_dotenv
from re import search
import socket, time, json
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import _thread
import time
load_dotenv()
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen(5)

#create .env following .envExample (get API key from binace)
api_key = os.environ.get("api-key")
api_secret = os.environ.get("api-secret")

def search(get_cryp):
    client = Client(api_key, api_secret)
    prices = client.get_all_tickers()
    flag = True
    for p in prices:
      if p['symbol'] == get_cryp.upper():
        p = "%s: %.2f "%(p['symbol'],float(p['price']))
        flag = False
        break
    if flag:
      p = "can not found!!!"
    return p
while True:
    clientsocket, address = server.accept()

    print(f"Connection from {address} has been established!")

    while True:
        string = clientsocket.recv(1024)
        if not string or (string.decode('utf-8')=="2.") or (string.decode('utf-8')=="2"):
            print(f"Exited by client {address}")
            break
        try:
            string = string.decode("utf-8")
            clientsocket.send(bytes(search(string), "utf-8"))          
        except: 
            print(f"Exited by client {address}")

    
