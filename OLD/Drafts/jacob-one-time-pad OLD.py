# normal one time pad example


import random
import string

#add the salt to the list
randomValueList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 
def generate_key_one_time_pad(length):
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return key


def encrypt_one_time_pad(plaintext, key):
    plaintext = plaintext.ljust(100, random.choice(randomValueList)) # expand plaintext to 100 characters
    encrypted_text = ''
    for i in range(len(plaintext)):
        encrypted_text += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return encrypted_text


def decrypt_one_time_pad(encrypted_text, key):
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        decrypted_text += chr(ord(encrypted_text[i]) ^ ord(key[i % len(key)]))
    return decrypted_text


# Example usage:
plaintext = "lets do this"
key = generate_key_one_time_pad(len(plaintext))
encrypted_text = encrypt_one_time_pad(plaintext, key)
decrypted_text = decrypt_one_time_pad(encrypted_text, key)




print("Plaintext: ", plaintext)
print("Key: ", key)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)