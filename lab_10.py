#!usr/bin/python

# 1. Write a Python script to list all the prime numbers from 1 to 100 using Sieve of Eratosthenes.

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    for p in range(2, num+1):
        if prime[p]:
            print(p,end=" ")

if __name__ == '__main__':
    num = 30
    print("The prime numbers are")
    SieveOfEratosthenes(num)

# 2. Write a Python script to implement RSA algorithm using build in functions (both encryption and decryption)

import math
p,q=3,7 # Two Large prime number

n=p*q
print("n =",n)

phi=(p-1)*(q-1)

e=2
while(e<phi):
  if(math.gcd(e,phi)==1):
    break
  else:
    e+=1
print("e =",e)

d = pow(e, -1, phi)
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')

m=11 # plain text
print(f'Original Message:{m}')
c=pow(m,e,n)
print(f'Encrypted Message: {c}')
m=pow(c,d,n)
print(f'Decrypted Message: {m}')

# 3. Write a Python script to implement RSA algorithm with out using build in functions (both encryption and decryption)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply result with base
            result = (result * base) % mod
        base = (base * base) % mod  # Square the base
        exp //= 2
    return result

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm to find modular inverse
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd_value, x, _ = extended_gcd(e, phi)

    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist as GCD is not 1")
    else:
        return x % phi

p, q = 3, 7  # Two large prime numbers

n = p * q
print("n =", n)

phi = (p - 1) * (q - 1)

# Find e such that 1 < e < phi and gcd(e, phi) = 1
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1
print("e =", e)

# Calculate the modular inverse of e modulo phi to get d
d = mod_inverse(e, phi)
print("d =", d)
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

# Encrypting the message
m = 11  # Plaintext message
print(f'Original Message: {m}')
c = mod_exp(m, e, n)
print(f'Encrypted Message: {c}')

# Decrypting the message
m = mod_exp(c, d, n)
print(f'Decrypted Message: {m}')


