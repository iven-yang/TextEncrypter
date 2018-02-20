import getpass
from aescipher import AESCipher

plaintext_file_name = 'plaintext.txt'
ciphertext_file_name = 'cipher.bin'

password = getpass.getpass()
write_file = input("Write to file {}? (y/n):".format(plaintext_file_name))

cipher = AESCipher(password)

ciphertext = ''
with open(ciphertext_file_name, 'r') as f:
    ciphertext = f.read()

plaintext = cipher.decrypt(ciphertext)

try:
    displaytext = plaintext.decode('utf-8')
    print(displaytext)
except UnicodeDecodeError:
    displaytext = "You're not me"
    print(plaintext)

print("Binary Decrypted")

if write_file == 'y':
    with open('plaintext.txt', 'w') as f:
        file = f.write(displaytext)
        print("Plaintext written to {}".format(plaintext_file_name))
