import socket
from threading import Thread


class Client(Thread):
    def __init__(self, conn, adr, n) -> None:
        super().__init__()
        self.conn = conn
        self.adr = adr
        self.n = n

        self.start()

    def run(self) -> None:
        while True:
            data = conn.recv(1024)
            if not data:
                conn.close()
                break
            txt = data.decode().split(',')
            x, y = float(txt[0]), float(txt[1])
            print(f"{self.n} : ({x}, {y})")
    


socket_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_listen.bind(("127.0.0.1", 65432))
socket_listen.listen()

n = 1

while True:
    print("Listening ...")
    conn, adr = socket_listen.accept()
    print(f"Client on {adr}")
    Client(conn, adr, n)
    n += 1



