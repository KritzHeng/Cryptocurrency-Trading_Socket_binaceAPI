# นาย คริษฐ์คณิน เฮงนิรันดร์ 6210450041
# นาย ณัฐดนัย คุ้มศิริ 6210450563

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 1234))


try:
    while True:
        string = input("choice the number\n1. trade cryptocurrency | 2.Exit: ")
        if string=="2." or string == "2":
            server.send(bytes(string, "utf-8"))
            server.close()
            break
        elif string=="1." or string == "1":
            crypto = input(("\ncryptocurrency pairs for trading(ex.BTCUSDT): "))
            server.send(bytes(crypto, "utf-8"))
            buffer = server.recv(1024)
            buffer = buffer.decode("utf-8")
            print(f"[Server] {buffer}\n")
except KeyboardInterrupt:
    print("\nExited by user")
server.close()