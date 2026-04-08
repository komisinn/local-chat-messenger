import socket
import os
from faker import Faker

fake = Faker()
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/tmp/faker_socket_file'

if os.path.exists(server_address): os.remove(server_address)
sock.bind(server_address)

print("--- Server is Ready: Type 'name', 'address', or 'email' on client ---")

try:
    while True:
        data, address = sock.recvfrom(4096)
        if data:
            request = data.decode('utf-8').strip().lower()
            # 入力内容に応じてFakerを使い分ける
            if request == 'name':
                response = f"Name: {fake.name()}"
            elif request == 'address':
                response = f"Address: {fake.address()}"
            elif request == 'email':
                response = f"Email: {fake.email()}"
            else:
                response = "Try: name, address, or email"
            
            sock.sendto(response.encode('utf-8'), address)
finally:
    if os.path.exists(server_address): os.remove(server_address)