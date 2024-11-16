def encrypt(text: str, encryption_key: str) -> str:
    encrypted = []
    key_length = len(encryption_key)
    try:
        for i, char in enumerate(text):
            substitution = (ord(char) + ord(encryption_key[i % key_length]))
            encrypted.append(chr(substitution))
        return ''.join(encrypted)
    except:
        print('Unable to encrypt with that passphrase! Aborting...')
        exit(1)

def decrypt(encrypted_text: str, decryption_key: str) -> str:
    decrypted = []
    key_length = len(decryption_key)
    try:
        for i, char in enumerate(encrypted_text):
            original = (ord(char) - ord(decryption_key[i % key_length]))
            decrypted.append(chr(original))
        return ''.join(decrypted)
    except:
        print('Unable to decrypt with that passphrase! Aborting...')
        exit(1)