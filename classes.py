import socket
import os

class Fuck:
    def __init__(self, server,  socket_path: str = "/tmp/my_socket.sock"):
        self.socket_path = socket_path
        pass


    def connect(self) -> bool:
        return True

    def tx(self, data: str) -> bool:
        # is anyone here
        pass

    def rx() -> str | None:
        self.func()
        pass

    def set_rx_callback(self, func):
        self.func = func

    def valaiable_data(self) -> int:
        return 0;

class Socket:

    def __init__(self, socket_path: str = "/tmp/my_socket.sock"):
        self.socket_path = socket_path

    def transmit(self) -> None:
        try:
            os.unlink(self.socket_path)
        except OSError:
            if os.path.exists(self.socket_path):
                raise

        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(self.socket_path)
        server.listen(1)
        print("Server is listening for incomig commands...")
                                                                                                                                                                      1,1           Top
        while True:
            connection, _ = server.accept()
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print("Received data:", data.decode())
                response = "Hello from the server!"
                connection.sendall(response.encode())
            connection.close()


    def receive(self) -> str:
        message="Hello from the client!"

        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # is socket open?
        client.connect(self.socket_path)
        client.sendall(message.encode())
        response = client.recv(1024)
        print("Received response:", response.decode())
        client.close()
        return ????


