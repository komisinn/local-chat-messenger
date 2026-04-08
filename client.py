import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# サーバーの住所（同じPCなら 127.0.0.1）
server_address = ('127.0.0.1', 9001)

try:
    while True:
        # ユーザーから入力を受け取る
        message = input("Say something to the server: ")
        if not message: break

        # データを送信
        sock.sendto(message.encode('utf-8'), server_address)

        # サーバーからの応答を受信
        data, server = sock.recvfrom(4096)
        print(f"Server says: {data.decode('utf-8')}")

finally:
    sock.close()