# TextEncrypter
Encrypts a txt file to bin using AES

You can use this to store/backup whatever info you don't want other people snooping on for peace of mind (I made this so i can keep cryptocurrency in cold storage and have all my private keys in a file that I can backup).
You can store copies of wallet.bin around on cloud storage for added peace of mind.
Just don't forget your password, and run wallet_accessor.py once to make sure you got your password right.
Feel free to use my code or whatever.

Instructions:
Make a file (to be encrypted) called plaintext_wallet.txt in current directory.

Use wallet_creator.py to encrypt "plaintext_wallet.txt" to "wallet.bin"

Use wallet_accessor.py to decrypt "wallet.bin" to "plaintext_wallet.txt"

Don't forget your password...
