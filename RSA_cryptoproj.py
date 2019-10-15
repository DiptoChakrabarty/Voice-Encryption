p=31
q=37
r=43
n=p*q*r
print("n = p * q * r = " + str(n) + "\n")
phi=(p-1)*(q-1)*(r-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        #raise Exception('modular inverse does not exist')
        return -1
    else:
        return x % m
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

l=coprimes(phi)
e=l[int(len(l)/2)]
d=modinv(e,phi)
print(d)


def encrypt_block(m):
    c = modinv(m**e, n)
    if c == -1:
        return ord('o')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == -1:
        return ord('o')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])

print("public key = ",e,n)
print("private key= ",d,n)

s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")

enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")

dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")
