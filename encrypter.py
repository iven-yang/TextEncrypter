import getpass
from aescipher import AESCipher

plaintext_file_name = 'plaintext.txt'
ciphertext_file_name = 'cipher.bin'

password = getpass.getpass()

cipher = AESCipher(password)

plaintext = ''
with open(plaintext_file_name, 'r') as f:
    plaintext = f.read()

ciphertext = cipher.encrypt(plaintext)

with open(ciphertext_file_name, 'wb') as f:
    f.write(ciphertext)
print("Encrypted Binary Created")
