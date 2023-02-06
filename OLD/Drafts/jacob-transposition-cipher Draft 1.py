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


# --- Function to return a combination of 1,2,3 and 4 with each number being used only once ---
def get_combo_of_1234():

    # setting up numbers left and current key
    current_numbers_left = [1,2,3,4]
    desired_combo_key = []

    # get current length of the numbers left
    current_length_of_what_is_left = len(current_numbers_left)

    # loop through until all the numbers are removed
    while current_length_of_what_is_left > 0:
        next_to_remove = input(f"The current numbers left for the key are {current_numbers_left},\nSelect a number from these: ")

        # if below passes, this is a number at least
        if next_to_remove.isnumeric() == True:
            # if below passes, than i
            if int(next_to_remove) in current_numbers_left:
                desired_combo_key.append(int(next_to_remove)) # appending to the key
                current_numbers_left.remove(int(next_to_remove)) # removing number from number left
                current_length_of_what_is_left = len(current_numbers_left) # recalculating length that is left
            
            else:
                print("Nice try, that was an invalid option. Try again.\n")
        
        else:
            print("This has to be a number wise guy.\n")

    print(f"Your key is going to be: {desired_combo_key}")
    return desired_combo_key




# --- Function to ENCRYPT a simple transposition cipher ---
def encrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nSimple Transposition has been activated!\n")

    # The four Arrays used to encrypt a transposition cipher, in here because I don't want the data to remain outside this function
    # Array0 = []
    # Array1 = []
    # Array2 = []
    # Array3 = []

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

        # if mod is equal to 0, we move to List 0
        if (current_mod_of_char == 0):
            # Array0.append(character)
            ListOfLists[0].append(character)

        # if mod is equal to 1, we move to List 1
        elif (current_mod_of_char == 1):
            # Array1.append(character)
            ListOfLists[1].append(character)

        # if mod is equal to 2, we move to List 2
        elif (current_mod_of_char == 2):
            # Array2.append(character)
            ListOfLists[2].append(character)

        # mod has to be equal to 3, we move to List 3
        else:
            # Array3.append(character)
            ListOfLists[3].append(character)

    print(ListOfLists)
    # for index,elements in enumerate(Array0):
    #     print(f"element: {elements}")


    input_column_order_key = input("What is the column order you want? \nNOTE: You must only use the numbers 4,3,2,1 and only use them once: ") # getting the column order value from the user
    
    # make sure that the length of the key is not greater than 4
    length_of_key = len(input_column_order_key)
    # valid_chars_only = True
    # for character_valid in input_column_order_key:
    #     while character_valid not in [4,3,2,1]:
    #         valid_chars_only = False
    
    # while length_of_key != 4 or valid_chars_only == False:
    while length_of_key != 4:
        input_column_order_key = input("The key needs to be 4 characters long, no exceptions.\nAlso it must only contain 4,3,2,1\nList a new 4 character key with 4,3,2,1: ")
        
        # rechecking inputs
        length_of_key = len(input_column_order_key)
        # valid_chars_only = True
        # for character_valid in input_column_order_key:
        #     while character_valid not in [4,3,2,1]:
        #         valid_chars_only = False


    # Iterating through the array and creating the ciphertext
    # getting ciphertext ready
    outbound_ciphertext = ''

    # appending arrays to ciphertext
    for numbers in input_column_order_key:
        print(f"Appending List {numbers}")
        print(f"This is ListOfLists{numbers}, or: {ListOfLists[numbers]}")
        outbound_ciphertext.join(ListOfLists[int(numbers)]) 

    
    # printing out final ciphertext and saving it to a file
    print(outbound_ciphertext)


# --- Function to DECRYPT a simple substitution cipher ---
def decrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nDecrypt Transposition has been activated!\n")


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# encrypt_transposition()
thisVal = get_combo_of_1234()


print(f"THIS COMBO IS {thisVal}")