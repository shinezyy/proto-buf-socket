import socket
import msg_pb2
from struct import unpack


def main():
    host = '127.0.0.1'
    port = 1101
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print('connection from {}'.format(addr))
    while True:
        header = conn.recv(4)
        if not header:
            break
        message_length, = unpack('>I', header) #unpack always returns a tuple.
        data = conn.recv(message_length)
        if not data:
            break
        da = msg_pb2.DependancyArray()
        da.ParseFromString(data)
        for d in da.elements:
            print('L dep:{}, R dep: {}'.format(d.dependancy[0],
                d.dependancy[1]))

if __name__ == '__main__':
    main()

