#!usr/bin/python

# 1. Assume you intercepted the following ciphertext. Using a statistical attack, find the plaintext

from collections import Counter

ct = "XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVX-LQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW"

# Most common letters in English in order of frequency
freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

freq = Counter(ct)
sorted_freq = freq.most_common()

mapping = {}
for i, (cipher_letter, _) in enumerate(sorted_freq):
    if i < len(freq_order):
        mapping[cipher_letter] = freq_order[i]

def substitute_cipher(ct, mapping):
    result = ""
    for char in ct:
        result += mapping.get(char, char)
    return result

deciphered_text = substitute_cipher(ct, mapping)
print("Mapping:", mapping)
print("Partially Deciphered Text:", deciphered_text)

# 2. Write a Python script to encrypt using Rail Fence (Zig zag ) with three rows and with key (ONE).

def rail_fence_encrypt_with_keyword(text, num_rails=3, keyword="ONE"):
    text = text.replace(" ", "").upper()
    rails = [''] * num_rails
    row = 0
    direction = 1

    for char in text:
        rails[row] += char
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
    
    rail_order = sorted((keyword[i], rails[i]) for i in range(num_rails))
    encrypted_text = ''.join(rail for _, rail in rail_order)
    return encrypted_text

pt = "WEAREDISCOVERED"
num_rails = 3
keyword = "ONE"
encrypted_rail = rail_fence_encrypt_with_keyword(pt, num_rails, keyword)
print("Encrypted Text using Rail Fence Cipher with Keyword:", encrypted_rail)

# 3. Write a python script to encrypt columnar transposition 

def columnar_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    num_columns = len(key)
    num_rows = len(text) // num_columns + (len(text) % num_columns > 0)

    grid = ['' for _ in range(num_columns)]

    for index, char in enumerate(text):
        grid[index % num_columns] += char

    sorted_columns = sorted((k, col) for k, col in zip(key, grid))
    encrypted_text = ''.join(column for _, column in sorted_columns)
    return encrypted_text

plaintext = "WEAREDISCOVERED"
key = "ONE"
encrypted = columnar_transposition_encrypt(plaintext, key)
print("Encrypted Text using Columnar Transposition with Keyword:", encrypted)

# 4. Write a Python script to decrypt Rail Fence Cipher 

def rail_fence_decrypt(ciphertext, num_rails):
    rail_lengths = [0] * num_rails
    row = 0
    direction = 1

    for char in ciphertext:
        rail_lengths[row] += 1
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1

    rails = []
    start = 0
    for length in rail_lengths:
        rails.append(ciphertext[start:start + length])
        start += length

    plaintext = ""
    row = 0
    direction = 1
    rail_pointers = [0] * num_rails  

    for _ in range(len(ciphertext)):
        plaintext += rails[row][rail_pointers[row]]
        rail_pointers[row] += 1
        row += direction

        if row == 0 or row == num_rails - 1:
            direction *= -1

    return plaintext

num_rails = 3
decrypted = rail_fence_decrypt(encrypted_rail, num_rails)
print("Decrypted Text using Rail Fence Cipher:", decrypted)


