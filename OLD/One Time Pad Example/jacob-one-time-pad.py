# This Python Program was written on Windows 10 and Linux Mint using VScode, your milage may vary based on your OS and configuration.

'''
This is draft 1: I am writing a preliminary substituion cipher to later incorporate into my final cipher
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import random # one time pad use
import pickle # saving array data to file

import datetime # used to get the datetime for "defang_datetime" function



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Variables
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to print out my Logo ---
def myLogo():
    print("Created and Tested by: ")
    print("   __                  _         ___ _                       ")
    print("   \ \  __ _  ___ ___ | |__     / __\ | ___  _   _ ___  ___  ")
    print("    \ \/ _` |/ __/ _ \| '_ \   / /  | |/ _ \| | | / __|/ _ \ ")
    print(" /\_/ / (_| | (_| (_) | |_) | / /___| | (_) | |_| \__ \  __/ ")
    print(" \___/ \__,_|\___\___/|_.__/  \____/|_|\___/ \__,_|___/\___| ")
    print("Dedicated to Peter Zlomek and Harely Alderson III")


# --- Function to Defang date time ---
def defang_datetime():
    current_datetime = f"_{datetime.datetime.now()}"

    current_datetime = current_datetime.replace(":","_")
    current_datetime = current_datetime.replace(".","-")
    current_datetime = current_datetime.replace(" ","_")
    
    return current_datetime


# --- Function to Write Data to a file ---
def data_to_file(NameOfFile,dataToWrite):
    # if type == 'array':
    # can't use write for list type, need to use writelines
    with open(f"{NameOfFile}.pickle", "wb") as out_file:
        pickle.dump(dataToWrite, out_file)
    # else:
    #     # to handle strings
    #     outboundFile = open(f"{NameOfFile}.txt", "w")
    #     ThisIsForStrings = outboundFile.write(dataToWrite)
    #     outboundFile.close()






# --- Function to Encrypt a One Time Pad ---
def encrypt_one_time_pad(plaintext):
    # will take in input from user outside of function and then pass it in
    print("Simple One Time Pad Encrypt\n")

    # using the length of pad to generate random one digit numbers from 0 to 9, need to store and output
    one_time_pad_key= ''
    for letters in plaintext:
        current_key_value = str(random.randint(0,9))
        one_time_pad_key += current_key_value
        # print(f"Letter: {letters}, Key value: {current_key_value}")

    # take your key and combine with your plaintext to get your ciphertext
    array_ciphertext = [chr(ord(p) ^ ord(k)) for (p,k) in zip(plaintext, one_time_pad_key)]
    # output_ciphertext = ' '.join(array_ciphertext)

    # output ciphertext and key
    print(f"\nOne Time Pad Key: {one_time_pad_key}")
    print(f"Output Ciphertext: {array_ciphertext}")
    print(f"Length of Ciphertext Array: {len(array_ciphertext)}")
    
    # Write ciphertext and key to separate files
    data_to_file("CIPHER",array_ciphertext)
    data_to_file("OTP_KEY",one_time_pad_key)

    return one_time_pad_key, array_ciphertext
    


# --- Function to Decrypt a One Time Pad ---
#def decrypt_one_time_pad(one_time_pad_decrypt_key,ciphertext):
def decrypt_one_time_pad():
    # will take in input from user outside of function and then pass it in
    print("Simple One Time Pad Decrypt\n")

    # loading key from pickle
    with open("OTP_KEY.pickle", "rb") as loaded_key_file:
        one_time_pad_decrypt_key = pickle.load(loaded_key_file)

    # Loading ciphertext from pickle
    with open("CIPHER.pickle", "rb") as loaded_cipher_file:
        ciphertext = pickle.load(loaded_cipher_file)
    

    print(f"Ciphertext: {ciphertext}, Key: {one_time_pad_decrypt_key}")

    # take your key and combine with your ciphertext to get your plaintext back
    array_plaintext = [chr(ord(p) ^ ord(k)) for (p,k) in zip(ciphertext, one_time_pad_decrypt_key)]

    # change output from array to a string
    output_plaintext = ''
    for characters in array_plaintext:
        output_plaintext += characters

    print(f"Your plaintext: {output_plaintext}")

    return output_plaintext
''''''


'''
change it so that it outputs a string of letters for the plaintext
have python save the one time pad ciphertext to a file, then open that file and read it for decryption
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

outside_key, outside_ciphertext = encrypt_one_time_pad("LETS GO BOI")

print(f"Outside of function:\nKey: {outside_key},\nCiphertext:{outside_ciphertext}")

# outside_plaintext = decrypt_one_time_pad(outside_key,outside_ciphertext)
outside_plaintext = decrypt_one_time_pad()
print(f"\nFINAL Outside Plaintext: {outside_plaintext}")


# encrypt_one_time_pad("cool runnings")