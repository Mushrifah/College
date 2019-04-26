
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

msg = input("Enter Message:")
msg = str.encode(msg)
public_key = private_key.public_key()
cip = public_key.encrypt(
    msg,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=b"")
)
print("Encrypted:", cip)

#Prac 13
decip = private_key.decrypt(
    cip,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=b"")
)
print("Decrypted:", decip)
