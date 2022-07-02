import socket
import time
import controller


def init():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('106.14.149.194', 9990))
    s.setblocking(True)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 50240)
    return s


def resetNet(type, s=None):
    while True:
        try:
            if s != None:
                s.close()
            s = init()
            s.send(type.to_bytes(4, byteorder="big"))
        except BaseException:
            time.sleep(2)
            resetNet(type, s)
        else:
            break
    return s


def waitCommand():
    s1 = resetNet(10000)
    while True:
        try:
            cmd = s1.recv(4)
        except BaseException:
            s1 = resetNet(10000, s1)
            continue
        cmd = int.from_bytes(cmd, byteorder="big")
        controller.action(cmd - 1)


def start():
    waitCommand()
