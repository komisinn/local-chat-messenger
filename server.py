import socket
from faker import Faker

# Fakerの初期化
fake = Faker('ja_JP')
fake.job()
name = fake.name()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '0.0.0.0'
server_port = 9001
sock.bind((server_address, server_port))

print("Faker Server is ready...")

while True:
    data, address = sock.recvfrom(4096)
    if data:
        # クライアントからのメッセージを表示
        print(f"Received: {data.decode('utf-8')} from {address}")

        # Fakerで偽のデータを生成（名前や文章など）
        # ここでは「名前: 住所」というランダムな文字列を作ってみます
        response = f"あ、どうも！{fake.name()}（{fake.job()}）やん。今は{fake.city()}におるとよ。"
        
        # 応答を送信
        sock.sendto(response.encode('utf-8'), address)
