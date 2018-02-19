import getpass
from aescipher import AESCipher

password = getpass.getpass()

cipher = AESCipher(password)

plaintxt = ''
with open('plaintext.txt', 'r') as f:
    plaintxt = f.read()

ciphertxt = cipher.encrypt(plaintxt)

with open('cipher.bin', 'wb') as f:
    f.write(ciphertxt)
print("Encrypted Binary Created")
