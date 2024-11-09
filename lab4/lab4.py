# 1) Write a Python program to reverse the content of the string. (Do not use built in) 

s1=input("Enter a string to reverse : ")
reverse=s1[::-1]
print(reverse)

# 2) Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.

s2=input("Enter a string to compress : ")
d={}
for i in s2:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
#print(d)
for i in d:
    print(i+str(d[i]),end="")  

# 3) Get the Caesar cipher from the user Decrypt the cipher 

def decrypt(ct,key):
    plain_text=""
    for i in cipher:
        if i.isupper():
             plain_text+=chr((ord(i)-key-65)%26+65)
        elif i.islower():
            plain_text+=chr((ord(i)-key-97)%26+97)
        else:
            plain_text+=i
    
    return plain_text

cipher=input("\nEnter a Caesar Cipher to decrypt it : ")
key=3
print("The Decrypted Cipher using Caesar Cipher is ",decrypt(cipher,key))

# Get the cipher encrypted using shift cipher. Identify the key used to encrypt using brute force (ie all the values in the key space) 
key_space=26
def encrypt(pt,key):
    ct=""
    for i in pt:
        if i.isupper():
            ct+=chr((ord(i)+key-65)%26+65)
        elif i.islower():
            ct+=chr((ord(i)+key-97)%26+97)
        else:
            ct+=i
    return ct

def finding_key(plain,cipher):
    for i in range(key_space):
        res=decrypt(cipher,i)
        if res==plain:
            return i      

plain=input("Enter a text to Encrypt : ")
key=int(input("Enter any Key Value to Encrypt : "))
cipher=encrypt(plain,key)
print("The Encrypted Cipher using shift cipher is ",cipher)
key_found_brute=finding_key(plain,cipher)
print(f"The Key for the {plain} and {cipher} is {key_found_brute}")


#Find the k value , Provided cipher text and plain text 

print("The key value for provided cipher and plain text is", ((ord(cipher[0])-ord(plain[0]))%26))

#Encrypt and decrypt the string using Atbash cipher 
n=26
def atbash_cipher(pt):
    res=""
    for i in pt:
        if i.isupper():
            res+=chr(91-(ord(i)-65)-1)
        elif i.islower():
            res+=chr(123-(ord(i)-97)-1)
        else:
            res+=i
    return res

text=input("Enter a text to encrypt using atbash : ")
atbash=atbash_cipher(text)
print(f"The Encrypted text using Atbash Cipher for given {text} is {atbash}")

#Encrypt and decrypt using Affine cipher (add validation)
        
