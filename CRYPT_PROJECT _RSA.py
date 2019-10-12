p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
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
        raise Exception('modular inverse does not exist')
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
import random
#print("Choose an e from a below coprimes array:\n")
#print(str(coprimes(phi)) + "\n")
l=coprimes(phi)
w=random.randint(0,len(coprimes(phi))-1)

e=l[w]
d=modinv(e,phi)
p1=113
q1=131
n1=p1*q1
ph1=(p1-1)*(q1-1)
l1=coprimes(ph1)
e1=l1[random.randint(0,len(coprimes(ph1)))]
d1=modinv(e1,ph1)

def encrypt_block(m,e,n):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c,d,n):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s,e,n):
    return ''.join([chr(encrypt_block(ord(x),e,n)) for x in list(s)])
def decrypt_string(s,d,n):
    return ''.join([chr(decrypt_block(ord(x),d,n)) for x in list(s)])

e2=encrypt_block(e,e1,n1)
d2=encrypt_block(d,e1,n1)
print("public key = ",e1,n-1,e2)
print("private key= ",d1,n-1,d2)

s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
e3=decrypt_block(e2,d1,n1)
print(e,e1,e2,e3)
enc = encrypt_string(s,e3,n)
print("Encrypted message: " + enc + "\n")
d3=decrypt_block(d2,d1,n1)
print(d,d1,d2,d3)
dec = decrypt_string(enc,d3,n)
print("Decrypted message: " + dec + "\n")
