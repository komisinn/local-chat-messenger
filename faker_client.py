import socket
import os

server_address = '/tmp/faker_socket_file'
client_address = '/tmp/faker_client_socket_file'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(client_address): os.remove(client_address)
sock.bind(client_address)

try:
    while True:
        cmd = input("Command (name/address/email/exit) > ")
        if cmd == 'exit': break
        sock.sendto(cmd.encode('utf-8'), server_address)
        data, server = sock.recvfrom(4096)
        print(f"Response: {data.decode('utf-8')}")
finally:
    sock.close()
    if os.path.exists(client_address): os.remove(client_address)