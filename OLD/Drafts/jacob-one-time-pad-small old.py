def one_time_pad(plaintext, key):
    ciphertext = [chr(ord(p) ^ ord(k)) for (p,k) in zip(plaintext, key)]
    return ''.join(ciphertext)

def encrypt(plaintext, key):
    return one_time_pad(plaintext, key)

def decrypt(ciphertext, key):
    return one_time_pad(ciphertext, key)


plaintext1 = input("feed me plaintext: ")
this_key = input('input key: ')

encryptboi = encrypt(plaintext1, this_key)
print(f"Encrypted form: {encryptboi}")


decryptboi = decrypt(encryptboi, this_key)
print(f"Decrypted form: {decryptboi}")