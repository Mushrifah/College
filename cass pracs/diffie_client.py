import socket


def gen_k(a, Q, x):
    key = pow(a, x) % Q
    return key


print("\nWelcome to Chat Room\n")

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = 'localhost'
name = input(str("Enter your name: "))
port = 1234
s.connect((ip, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\n")

q = 11
alpha = 3
xb = 7
yb = gen_k(alpha, q, xb)
print("Private Key:", xb, "Public Key:", yb)
ya = s.recv(1024)
ya = ya.decode()
ya = int(ya)
yb = str(yb).encode()
s.send(yb)
k = gen_k(ya, q, xb)
print("Shared Key Is:", k)