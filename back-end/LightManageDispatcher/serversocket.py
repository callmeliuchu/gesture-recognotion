import socket
import threading

sock_list = []


def listenConn(s):
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        sock.setblocking(True)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 102400)
        command = sock.recv(4)
        command = int.from_bytes(command, byteorder='big')
        if command == 10000:
            sock_list.append(sock)


def start_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9990))
    s.listen(10)
    t1 = threading.Thread(target=listenConn, args=(s,))
    t1.start()


def send(cmd):
    for s in sock_list:
        try:
            s.sendall(cmd.to_bytes(cmd, byteorder="big"))
        except:
            s.close()
