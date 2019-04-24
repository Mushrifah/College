def gen_k(a, Q, x):
    key = pow(a, x) % Q
    return key



q = 11
alpha = 3
xa = 5
xb=7
ya = gen_k(alpha, q, xa)
print("Private Key:", xa, "Public Key:", ya)

yb = gen_k(alpha, q, xb)
print("Private Key:", xb, "Public Key:", yb)


ka = gen_k(yb, q, xa)
print("Shared Key Is:", ka)

kb = gen_k(ya, q, xb)
print("Shared Key Is:", kb)