# caesar cipher

def caesar_cipher(p,k):
    res=""
    for i in range(len(p)):
        c=p[i]
        if(c.isupper()):
            res+=chr((ord(c)+k-65)%26+65)
        else:
            res+=chr((ord(c)+k-97)%26+97)
    return res

# convert cipher text into uppercase characters and split the cipher into group of 5 of characters

def split_into_five_group(c):
    c=c.upper()
    new_c=""
    for i in c:
        if i.isalpha():
            new_c+=i
    grp=' '.join(new_c[i:i+5] for i in range(0,len(new_c),5))

    return grp

# Write a Python program to Find the histogram for each characters.

def hist(p):
    histogram={}
    p=p.upper()
    for char in p:
        if char.isalpha():
            if char in histogram:
                histogram[char]+=1
            else:
                histogram[char]=1

    for char,count in histogram.items():
        print(f'{char}:{"*"*count}')

# Write a Python script to read the contents from the file.
def read_file(filename):
    with open(filename,'r') as file:
        x=file.read()
        return x

# Write a Python script to encrypt the contents from the file.
def encrypt(filename,k):
    content=read_file(filename)
    encrypted_text=caesar_cipher(content,k)
    with open("encrypted_file.txt",'w') as file:
        file.write(encrypted_text)
        print("Encrypted Successfully")

"""Do validation to the python program (2) 
   - not to accept special characters 
   - not to accept numeric values 
   - not to accept empty value 
   - accept only string
   - string should be lowercase if not convert the case """
def validation(data):
    if not data:
        return "Input should not be empty"
    if not data.isalpha():
        return "Input should only contain alphabets"
    return data.lower()

"""8. Write a Python program to checks if two given strings are anagrams of each other.
example: mug, gum
         cork, rock
         note, tone """

def check_anagram(data1,data2):
    if len(data1)!=len(data2):
        return False
    if sorted(data1)==sorted(data2):
        return True
    else:
        return False
"""9. Write a Python program to check the given string is palindrome or not
Do not use built in functions 

Example: MADAM 
         RACECAR
         LEVEL
         CIVIC   """

def palindrome(data):
    return data.lower()==data.lower()[::-1]

"""10. Write a Python program to check if a substring is present in a given string.
Example: Understand -- stand   """

def check_substring(data,sub):
    if sub in data:
        return True
    else:
        return False

""" 
11. Explore string module 
   import the string module in your python script. 
   print all the lowercase characters
   print all the uppercase characters 
   print all the lowercase and uppercase characters
   print all the digits 
   print all the punctuation symbols  
   count the total number of punctuation symbols 
"""


p="Hello World"
k=3
c="exampleofcipher"
print("The Caesar Cipher:",caesar_cipher(p,k))
print("Group of 5 of characters of cipher text:",split_into_five_group(c))
hist(p)
filename=input("Enter filename:")
print("The Content from the given file is:",read_file(filename))
encrypt(filename,k)
data=input("Enter a String: ")
print("Validated Results = ",validation(data))
print("Check if given strings are anagrams or not")
print(check_anagram("gum","mug"))
print("Check given string is palindrome or not")
print(palindrome("Madam"))

#STRING MODULE
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print("Count of Punctuation = ", len(string.punctuation))



