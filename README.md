# Crypt storage
Easily encrypt and decrypt any text document you want - txt, html, md, any document encoded with UTF-8.

# How to use
Open your terminal emulator, clone this repo with `git clone https://github.com/mifizz/crypt-storage` or just download **cryptstorage.py** and **algorithm.py**. After that, use **cd** command to open folder with *crypt storage*, eg. `cd crypt-storage`. 
Finally, type `python cryptstorage` or `python3 cryptstorage` (depends on your system).

## Encrypting
Type **1** to choose Encrypt option. After that, choose what you want to encrypt - file (1) or user input (2).
1. If you chose *file* you will be asked for a text file path (including file name, eg. `D:/some/folders/file.txt`).
2. If you chose *input* you will be asked for a text you want to encrypt.
Next you type your passphrase (you MUST keep it somewhere, it will be used to decrypt encrypted file later).
Lastly, you type file path to new encrypted text file (eg. `D:/some/folders/encrypted_text.txt`). That is all, you have successfully encrypted your text!

## Decrypting
Type **2** to choose Decrypt option. After that, choose what you want to decrypt - file (1) or user input (2).
1. If you chose *file* you will be asked for a **encrypted** text file path (eg. `D:/some/folders/encrypted_text.txt`).
2. If you chose *input* you will be asked for a text you want to decrypt. *(**NOT RECOMMENDED**, even if you paste encrypted text from file, there may be difference)*
Next you type your passphrase you used to encrypt this file/text.
Lastly, you type file path to new decrypted text file (eg. `D:/some/folders/decrypted_text.txt`). That is all, you have successfully decrypted your text back!
