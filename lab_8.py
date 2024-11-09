#!usr/bin/python

# 1. Write a Python script that takes two integers as input and calculates their GCD using the Euclidean algorithm.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def check_coprime_and_suitability(a, b):
    gcd_value = gcd(a, b)
    if gcd_value == 1:
        print(f"The numbers {a} and {b} are co-prime. They are suitable for cryptographic key generation.")
    else:
        print(f"The numbers {a} and {b} are not co-prime. They are not suitable for cryptographic key generation.")

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
check_coprime_and_suitability(a, b)

  
# 2. Write a python script to take two integer values (number (n) and modulo (m)) from the user and find the modular inverse using extended Euclidean algorithm.

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def lcm(a, b):
    return a * b // gcd_extended(a, b)[0]

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def coprime_check(a, b):
    g, _, _ = gcd_extended(a, b)
    return g == 1

a, b = 12, 23
gcd_value = gcd_extended(a, b)[0]
lcm_value = lcm(a, b)
coprime = coprime_check(a, b)
factors_a = prime_factors(a)
factors_b = prime_factors(b)
print(f"GCD: {gcd_value}, LCM: {lcm_value}, Co-prime: {coprime}")
print(f"Prime factors of {a}: {factors_a}")
print(f"Prime factors of {b}: {factors_b}")


# 3. Write a Python script that generates a random binary number of length 100. The output should be a string of 100 binary digits (0s and 1s). After generating the binary sequence, implement a function to check whether any subsequence of digits repeats itself within the sequence.

import random

def generate_random_binary(length=100):
    return ''.join(random.choice('01') for _ in range(length))

def repeated_subsequence(bin_string):
    exist = set()
    for length in range(1, len(bin_string) // 2 + 1):
        for i in range(len(bin_string) - length + 1):
            subseq = bin_string[i:i+length]
            if subseq in exist:
                return True
            exist.add(subseq)
    return False

bin_sequence = generate_random_binary(100)
print("Generated Binary Sequence:", bin_sequence)

if repeated_subsequence(bin_sequence):
    print("The binary sequence has repeated subsequences.")
else:
    print("The binary sequence does not have any repeated subsequences.")



# 4. Write a Python script that performs the Golomb test to the numbers provided below. 101011001010, 111111000000
from collections import Counter

def golomb_test(seq):
    count_0 = seq.count('0')
    count_1 = seq.count('1')
    rule1 = abs(count_0 - count_1) <= 1
    print(f"First Rule: {'Pass' if rule1 else 'Fail'}")
    
    runs = []
    current_run = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += seq[i]
        else:
            runs.append(current_run)
            current_run = seq[i]
    runs.append(current_run)
    
    run_lengths = [len(run) for run in runs]
    run_count = Counter(run_lengths)
    rule2 = True
    for length in sorted(run_count):
        if length + 1 in run_count and run_count[length] != 2 * run_count[length + 1]:
            rule2 = False
            break
    print(f"Second Rule: {'Pass' if rule2 else 'Fail'}")
    
    rule3 = seq[:len(seq)//2] == seq[len(seq)//2:]
    print(f"Third Rule: {'Pass' if rule3 else 'Fail'}")

    if rule1 and rule2 and rule3:
        print("The sequence passes the Golomb tests.")
    else:
        print("The sequence does not pass the Golomb tests.")

# Example sequences
sequences = ["101011001010", "111111000000"]
for seq in sequences:
    print(f"\nTesting sequence: {seq}")
    golomb_test(seq)

