# This Python Program was written on Windows 10 and Linux Mint using VScode, your milage may vary based on your OS and configuration.

'''
This is draft 2: I am writing a preliminary transposition cipher to later incorporate into my final cipher

I think I am going to use like 4 rows for this cipher and see how it goes
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import datetime # used to get the datetime for "defang_datetime" function


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Variables
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# maybe make an option where the user can specify the number of arrays and have it custom create them


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
def write_to_file(filename,plaintextOrCipherText,dataToWrite):
    outboundFile = open(f"{filename}.txt", "w")
    lesGoBoi = outboundFile.write(f'{plaintextOrCipherText} : {dataToWrite}')
    outboundFile.close()


# --- Function to ENCRYPT a simple transposition cipher ---
def encrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nSimple Transposition has been activated!\n")

    # The four Arrays used to encrypt a transposition cipher, in here because I don't want the data to remain outside this function
    Array0 = []
    Array1 = []
    Array2 = []
    Array3 = []

    ListOfLists = [[],[],[],[]]

    # getting plaintext from the user
    input_plaintext = input("\nWhat is the plaintext message you want to encode? ") # getting the plaintext to encrypt

    # # Getting Length of the String
    # length_of_input = len(input_plaintext)
    # print(f"Length of Input: {length_of_input}")

    # pushing that plaintext into arrays
    for index,character in enumerate(input_plaintext):
        print(f"Character: {character}")
        print(f"Index: {index}")

        # Get mod 4 of the current char 
        current_mod_of_char = index % 4
        print(f"Current Modulus: {current_mod_of_char}")

        # if mod is equal to 0, we move to Array0
        if (current_mod_of_char == 0):
            Array0.append(character)

        # if mod is equal to 1, we move to Array1
        elif (current_mod_of_char == 1):
            Array1.append(character)

        # if mod is equal to 2, we move to Array2
        elif (current_mod_of_char == 2):
            Array2.append(character)

        # mod has to be equal to 3, we move to Array3
        else:
            Array3.append(character)


    for index,elements in enumerate(Array0):
        print(f"element: {elements}")


    # input_column_order_key = input("What is the column order you want? ") # getting the column order value from the user
    
    


# --- Function to DECRYPT a simple substitution cipher ---
def decrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nDecrypt Transposition has been activated!\n")


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


encrypt_transposition()