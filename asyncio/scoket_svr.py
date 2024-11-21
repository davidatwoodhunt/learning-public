import socket
import logging
logging.basicConfig(level=logging.INFO)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

address = ('127.0.0.1',8000)
server_socket.bind(address)
server_socket.setblocking(False)
server_socket.listen()
connections = []
try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            logging.info(f'I got a connection from {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass
 
        for connection in connections:
            try:
                buffer = b''
 
                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        logging.info(f'I got data: {data}!')
                        buffer = buffer + data
 
                logging.info(f"All the data is: {buffer}")
                connection.send(buffer)
            except BlockingIOError:
                pass
 
finally:
    server_socket.close()