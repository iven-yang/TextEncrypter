import getpass
from aescipher import AESCipher

password = getpass.getpass()

cipher = AESCipher(password)

ciphertxt = ''
with open('cipher.bin', 'r') as f:
    ciphertxt = f.read()

plaintxt = cipher.decrypt(ciphertxt)
with open('plaintext.txt', 'w') as f:
    try:
        print(plaintxt)
        file = f.write(plaintxt.decode('utf-8'))
    except UnicodeDecodeError:
        print("You're not me")
        f.write("You're not me")
        exit(0)
print("Encrypted Binary Decrypted")
