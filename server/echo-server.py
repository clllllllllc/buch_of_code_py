import socket

HOST = "127.0.0.1"
PORT = "6969"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    com, addr = s.accept()
    with conn:
        print(f"Connection: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            con.sendall(data)
