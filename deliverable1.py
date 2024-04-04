import random

def cipherkey():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key = ""
    l = len(alphabet) - 1

    for n in range(0, l + 1):
        key = key + alphabet.pop(random.randint(0, l))
        l = l - 1

    return key

def encryptmessage(plainText, key):
    cipher = ""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for character in plainText:
        if character in alphabet:
            index = alphabet.index(character)
            cipher = cipher + key[index]

    return cipher

def decryptedmessage(cipherText, key):
    decrypted = ""
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for character in cipherText:
      if character in key:
        index = key.index(character)
        decrypted = decrypted + alphabet[index]
    return decrypted

cipherkey = cipherkey()
print("Key ->", cipherkey)

message = input("Enter message to encrypt: ")
plainText = message

cipherText = encryptmessage(plainText.upper(), cipherkey)
print("Plain Text ->", plainText)
print("Cipher Text ->", cipherText)

newmessage = input("Enter message to decrypt: ")

decryptedText = decryptedmessage(cipherText, cipherkey)
print("Decrypted Text ->", decryptedText)