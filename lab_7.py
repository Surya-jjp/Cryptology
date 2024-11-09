#!usr/bin/python

# 1. Write a Python script to encrypt columnar transposition using keyword.

def columnar_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    num_col = len(key)
    num_row = len(text) // num_col + (len(text) % num_col > 0)
    grid = ['' for _ in range(num_col)]
    for i, char in enumerate(text):
        grid[i % num_col] += char
    sorted_col = sorted((k, col) for k, col in zip(key, grid))
    encrypted_text = ''.join(column for _, column in sorted_col)
    return encrypted_text

plaintext = "WEAREDISCOVERED"
key1 = "KEY"
encrypted = columnar_transposition_encrypt(plaintext, key1)
print("Encrypted Text:", encrypted)


# 2. Write a Python script to encrypt double columnar transposition. 

def double_columnar_transposition_encrypt(text, key1, key2):
    first = columnar_transposition_encrypt(text, key1)
    second = columnar_transposition_encrypt(first, key2)
    return second

key2 = "SECRET"
encrypted = double_columnar_transposition_encrypt(plaintext, key1, key2)
print("Double Encrypted Text:", encrypted)

# 3. Write a Python script to encrypt the message “She is listening” using the 6-character keyword “PASCAL” with Vigenere cipher.

def vigenere_encrypt(text, keyword):
    text = text.replace(" ", "").upper()
    keyword = keyword.upper()
    encrypted_text = ""
    keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    
    for i in range(len(text)):
        shift = ord(keyword_repeated[i]) - ord('A')
        encrypted_char = chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
        encrypted_text += encrypted_char
    
    return encrypted_text

keyword = "PASCAL"
encrypted = vigenere_encrypt(plaintext, keyword)
print("Vigenere Encrypted Text:", encrypted)


# 4. Write a Python script to encrypt and decrypt Hill cipher

import numpy as np

def hill_cipher_encrypt(pt, key_matrix):
    pt = pt.replace(" ", "").upper()
    if len(pt) % 2 != 0:
        pt += 'X'
    key_matrix = np.array(key_matrix)
    encrypted_text = ""

    for i in range(0, len(pt), 2):
        vector = [ord(pt[i]) - ord('A'), ord(pt[i+1]) - ord('A')]
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_text += ''.join(chr(num + ord('A')) for num in encrypted_vector)

    return encrypted_text

def hill_cipher_decrypt(encrypted_text, key_matrix):
    encrypted_text = encrypted_text.replace(" ", "").upper()
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = pow(det, -1, 26)
    adj_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inverse_key_matrix = (det_inv * adj_matrix) % 26
    decrypted_text = ""

    for i in range(0, len(encrypted_text), 2):
        vector = [ord(encrypted_text[i]) - ord('A'), ord(encrypted_text[i+1]) - ord('A')]
        decrypted_vector = np.dot(inverse_key_matrix, vector) % 26
        decrypted_text += ''.join(chr(num + ord('A')) for num in decrypted_vector)

    return decrypted_text

pt = "HELLO"
key_matrix = [[3, 3], [2, 5]]
encrypted = hill_cipher_encrypt(pt, key_matrix)
print("Hill Cipher Encrypted Text:", encrypted)
decrypted = hill_cipher_decrypt(encrypted, key_matrix)
print("Hill Cipher Decrypted Text:", decrypted)


# 5. Write a Python script to perform Kasiski test. 

from collections import defaultdict

def kasiski_test(ct):
    ct = ct.replace(" ", "").upper()
    sequence_distances = defaultdict(list)

    for seq_len in range(3, 6):  
        for i in range(len(ct) - seq_len):
            sequence = ct[i:i + seq_len]
            for j in range(i + seq_len, len(ct) - seq_len):
                if ct[j:j + seq_len] == sequence:
                    distance = j - i
                    sequence_distances[sequence].append(distance)

    print("Repeated sequences and distances:")
    for sequence, distances in sequence_distances.items():
        print(f"Sequence: {sequence}, Distances: {distances}")

ct = "FJAFWJSLLDHMIGYEQZWLCJKFWIPVCOFJAFWJSLLD"
kasiski_test(ct)

