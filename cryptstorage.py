import algorithm as alg # algorithm.py

# option
option = input('Option:\n1 - Encrypt\n2 - Decrypt\n: ')
# encrypt
if option == '1':
    # from file / input
    option_encrypt = input('Option:\n1 - From file\n2 - From input\n: ')
    # from file
    if option_encrypt == '1':
        filename = input('Filename: ')
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    # input
    elif option_encrypt == '2':
        text = input('Text: ')
    # abort
    else:
        print('Invalid option. Aborting...')
        exit(1)
    # encryption passphrase
    passphrase = input('Passphrase: ')

    # encrypt text
    encrypted = alg.encrypt(text, passphrase)
    print('Successfully encrypted!')
    # ask where to save
    filepath = input('Enter path and name to save output file: ')
    # write output to file
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f'BEGIN OF ENCRYPTED TEXT\n===\n{encrypted}\n===\nEND OF ENCRYPTED TEXT')
    except:
        print('Incorrect path or filename! Aborting...')
    print(f'Successfully wrote to file! (path: {filepath})')
# decrypt
elif option == '2':
    # from file / input
    option_decrypt = input('Option:\n1 - From file\n2 - From input\n: ')
    # from file
    if option_decrypt == '1':
        filename = input('Filename: ')
        with open(filename, 'r', encoding='utf-8') as file:
            encrypted = file.read()
            encrypted = encrypted.removeprefix('BEGIN OF ENCRYPTED TEXT\n===\n')
            encrypted = encrypted.removesuffix('\n===\nEND OF ENCRYPTED TEXT')
    # input
    elif option_decrypt == '2':
        encrypted = input('Text: ')
    # abort
    else:
        print('Invalid option. Aborting...')
        exit(1)
    # decryption passphrase
    passphrase = input('Passphrase: ')

    # decrypt
    decrypted = alg.decrypt(encrypted, passphrase)
    # ask where to save
    filepath = input('Enter path and name to save output file: ')
    # write to file
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f'BEGIN OF DECRYPTED TEXT\n===\n{decrypted}\n===\nEND OF DECRYPTED TEXT')
    except:
        print('Incorrect path or filename! Aborting...')
    print(f'Successfully wrote to file! (path: {filepath})')
else:
    print('Invalid option. Aborting...')
    exit(1)