'''
1. Write a Python Program to perform brute force attack on the cipher text “dvvkzecfssprkkve"

2. Write a Python program to use brute force attack to decipher the message. 
Assume Affine cipher was used and "ab" is encrypted as "GL". Find the value of keys. 

XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS


3. Encrypt the plain text using Rail Fence cipher 


4. Decrypt the cipher using Rail Fence

AAIUJ SIHBE KTEAO TEADE SNUTF EAEMR TAHSA
RHROA YHNFO AITTE EHCBO FVCAT RNMNS NUTFE
RASHL WFHLN HIUJS IHTKS OEHNI FISAE FNTIG
RMRSO LSTIS OKIEH PEOE
'''
def brute_force_attack(ct):
    print(len(ct))
    result=[]
    for i in range(26):
        l=""
        for j in ct:
            if j.isalpha():
                if j.isupper():
                    l+=chr((ord(j) + i-65) % 26 + 65)
                else:
                    l+=chr((ord(j) + i-97) % 26 + 97)
        result.append(l)
    return result

def rail_encrypt(pt):
    l=""
    for i in range(0,len(pt),2):
        l+=pt[i]

    for j in range(1,len(pt),2):
        l+=pt[j]
    print("The Encrypted cipher is ",l)
    return l

def rail_decrypt(ct):
    l1=ct[:len(ct)//2]
    l2=ct[len(ct)//2:]
    print("The Decrypted text is ",end="")
    for i,j in zip(l1,l2):
        print(i+j,end="")

brute_cipher="dvvkzecfssprkkve"
for i in brute_force_attack(brute_cipher):
    print(i)
pt=input("Enter the Plain Text to Encrypt : ")
ct=rail_encrypt(pt)
rail_decrypt(ct)
