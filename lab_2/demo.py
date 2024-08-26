#!usr/bin/python

#STRING OPERATIONS IN PYTHON
s1="Hello"
#Find the length of the string 
print(len(s1))

#Slice the string as per your choice 
print(s1[::2])

#Concatenate two strings 
s2="World"
print(s1+s2)

#Convert in to lower case in to uppercase character 
print(s1.upper())

#Convert upper case into lower case characters
print(s2.lower())

#convert the character into Unicode ( Ascii values)
c='A'
uni=ord(c)
print(uni)

#convert Unicode into character 
print(chr(uni))

#Check whether the given "substring" exists in the string
sub="Hell"
if sub in s1:
    print("Yes, The Substing is present in the string")
else:
    print("No, The Substring is not present in the string")

#Replace the character 'k' with 'h'
s3="Kill"
n_s3=s3.replace('K','H')
print(n_s3)

#Pad the string with "x" at the end
print(n_s3+'x')

#remove leading and trailing whitespace or specified characters from the string
print(n_s3.strip())

#split the given string in to group of five characters 
s4="Hi There!!! How are you?"
split =[s4 [i:i+5] for i in range(0, len(s4), 5)]
print(split)

#count total number of words 
print(len(s4.split()))

#Find the frequency of each characters in the string 
freq={}
for char in s4:
      if char in freq:
        freq[char]+=1
      else:
        freq[char]=1
print(freq)

#STDIN AND FILE OPEARTORS
# get the file name from the user 
filename=input("Enter file name:")

# check the file exist or not 
import os
if os.path.exists(filename):
    print(f"The file '{filename}' exists.")
else:
    print(f"The file '{filename}' does not exist.")

#LOOPING AND FILE HANDLING
#read the contents from the file 
with open(filename,'r') as file:
    content = file.read()
    print("File Content:")
    print(content)
    print(content[::-1])  #reverse the contents from the file

# Write into the file 
content=input("Enter file content:")
with open(filename,'w') as file:
    file.write(content)
print(f"The content has been written to '{filename}'.")

#MATH OPERATIONS
#convert Frequency in to percentage (continuation of 12th Question) 
total_char=len(s4)
freq_percent={char: round(count/total_char) *100 for char,count in freq.items()}
print(freq_percent)

#Perform modular arithmetic operation 
print(10%3)

# Find the prime numbers
#(i) check the given number is prime or not
n=int(input("Enter a number to check if is prime or not:"))
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime.")
else:
    print(f"{n} is not a prime number.")


#(ii)print the prime numbers with the given range 
n1,n2=map(int,input("Give a range:").split())
prime=[]
for num in range(n1,n2+1):
    if num>1:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            prime.append(num)
print(f"The Prime numbers between {n1} and {n2}:", prime)

#Check the given two numbers are co prime or not 
import math
n1,n2=map(int,input("Enter two number to check if it is co prime or not:").split())
gcd=math.gcd(n1,n2)
if gcd==1:
    print(f"{n1} and {n2} are co-prime")
else:
    print(f"{n1} and {n2} are not co-prime")

#find the factors for the given number (can use python library)
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print("\n")
# generate 10 random numbers 
import random
print(*[random.randint(1,100) for _ in range(10)])
# Explore : Miller-Rabin Test (pen paper method)


