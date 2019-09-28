try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass

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
ui=coprimes(phi)
e=ui[random.randint(int(len(ui)/2),len(ui))]
d=modinv(e,phi)

c=131
d=113
n1=c*d
ph=(d-1)*(c-1)
v=coprimes(ph)
a=ui[random.randint(int(len(v)/2),len(v))]
b=modinv(a,ph)
def enc(c):
   c1=modinv(c**a,n1)
   return c1
def dec(c):
   c1=modinv(c**b,n1)
   return c1
A=enc(e)
B=enc(d)
print("\nYour public key is a pair of numbers (A=" + str(A) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (B=" + str(B) + ", n=" + str(n) + ").\n")
def encrypt_block(m):
    c = modinv(m**(dec(A)), n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**(dec(B)), n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
print("Encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")
