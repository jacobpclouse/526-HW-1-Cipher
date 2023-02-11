# This Python Program was written on Windows 10 and Linux Mint using VScode, your milage may vary based on your OS and configuration.

'''
This is draft 1: I am writing a preliminary substituion cipher to later incorporate into my final cipher
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import random
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
def cipher_to_file(dataToWrite):
    outboundFile = open(f"cipher.txt", "w")
    lesGoBoi2 = outboundFile.write(dataToWrite)
    outboundFile.close()



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
    output_ciphertext = [chr(ord(p) ^ ord(k)) for (p,k) in zip(plaintext, one_time_pad_key)]

    # output ciphertext and key
    print(f"\nOne Time Pad Key: {one_time_pad_key}")
    print(f"Output Ciphertext: {output_ciphertext}")

    return one_time_pad_key, output_ciphertext
    


# --- Function to Decrypt a One Time Pad ---
def decrypt_one_time_pad(one_time_pad_decrypt_key,ciphertext):
    # will take in input from user outside of function and then pass it in
    print("Simple One Time Pad Decrypt\n")

    # take your key and combine with your ciphertext to get your plaintext back
    array_plaintext = [chr(ord(p) ^ ord(k)) for (p,k) in zip(ciphertext, one_time_pad_decrypt_key)]

    output_plaintext = ''
    for characters in array_plaintext:
        output_plaintext += characters

    print(f"Your plaintext: {output_plaintext}")

    return output_plaintext



'''
change it so that it outputs a string of letters for the plaintext
have python save the one time pad ciphertext to a file, then open that file and read it for decryption
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

outside_key, outside_ciphertext = encrypt_one_time_pad("my letters")

print(f"Outside of function:\nKey: {outside_key},\nCiphertext:{outside_ciphertext}")

outside_plaintext = decrypt_one_time_pad(outside_key,outside_ciphertext)
print(f"Outside Plaintext: {outside_plaintext}")