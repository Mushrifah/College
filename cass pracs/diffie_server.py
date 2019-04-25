import socket

def gen_k(a, Q, x):
    key = pow(a, x) % Q
    return key


print("\nWelcome to Chat Room\n")

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\n")
conn.send(name.encode())

q = 11
alpha = 3
xa = 5
ya = gen_k(alpha, q, xa)
print("Private Key:", xa, "Public Key:", ya)

ya = str(ya).encode()
conn.send(ya)
yb = conn.recv(1024)
yb = yb.decode()
yb = int(yb)
k = gen_k(yb, q, xa)
print("Shared Key Is:", k)