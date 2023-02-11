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
    lesGoBoi = outboundFile.write(f'{plaintextOrCipherText} : "{dataToWrite}"')
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


# --- Function to get remainder and let us know how many spaces to add ---
def get_remainder(input_string):
    # print(input_string)
    # getting length of input
    length_of_input = len(input_string)
    # print(f"Length: {length_of_input}")
    number_of_spaces_to_add = 4 - (int(length_of_input) % 4)
    # print(number_of_spaces_to_add)
    return int(number_of_spaces_to_add)


# --- Function to split up a string into 4 equal parts ---
def split_my_string_in_4(string):
    length = len(string) # getting length
    part_length = length // 4
    return [string[i:i + part_length] for i in range(0, length, part_length)] # returning each piece in an array



# --- Function to ENCRYPT a simple transposition cipher --- do a custom number of rails
def encrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nSimple Transposition has been activated!\n")

    # The four Arrays used to encrypt a transposition cipher, in here because I don't want the data to remain outside this function
    ListOfLists = [[],[],[],[]]

    # getting plaintext from the user
    input_plaintext = input("\nWhat is the plaintext message you want to encode? ") # getting the plaintext to encrypt

    # Getting remainder, seeing if we have to add any values to get it to be a factor of 4
    current_spaces_to_add = get_remainder(input_plaintext)
    print(current_spaces_to_add)

    if current_spaces_to_add != 4:
        for space in range(current_spaces_to_add):
            input_plaintext += ' ' # if you use spaces to add, then they don't know if they are 'real' spaces or just the padding at the end
            print(input_plaintext)
    print(f"\nNow with the displacement, the new plaintext is: {input_plaintext}")


    # pushing that plaintext into arrays
    for index,character in enumerate(input_plaintext):
        print(f"Character: {character}")
        print(f"Index: {index}")

        # Get mod 4 of the current char 
        current_mod_of_char = index % 4
        print(f"Current Modulus: {current_mod_of_char}")

        # if mod is equal to 0, we move to List 0
        if (current_mod_of_char == 0):
            ListOfLists[0].append(character)

        # if mod is equal to 1, we move to List 1
        elif (current_mod_of_char == 1):
            ListOfLists[1].append(character)

        # if mod is equal to 2, we move to List 2
        elif (current_mod_of_char == 2):
            ListOfLists[2].append(character)

        # mod has to be equal to 3, we move to List 3
        else:
            ListOfLists[3].append(character)

    print(ListOfLists)

    # getting key from user
    input_column_order_key = get_combo_of_1234()
    
    # print(input_column_order_key)


    # Iterating through the array and creating the ciphertext
    # getting ciphertext ready
    outbound_ciphertext = ''

    # appending arrays to ciphertext
    for numbers in input_column_order_key:
        print(f"Appending List {(numbers - 1)} as value was: {numbers}")
        print(f"This is ListOfLists{(numbers - 1)}, or: {ListOfLists[(numbers - 1)]}")

        # Changing list to string
        stringify_this = ''.join(ListOfLists[int((numbers - 1))])
        print(f"Stringifying: {stringify_this}")
        outbound_ciphertext += stringify_this

        # showing what the current ciphertext is
        print(f"\nCurrent Ciphertext: {outbound_ciphertext}\n")

    
    # printing out final ciphertext
    print(outbound_ciphertext)
    # Writing Data to a file
    write_to_file(f"Transposition_Encryption_{currentTime}","Trans CipherText",outbound_ciphertext)


# --- Function to DECRYPT a simple substitution cipher --- do a custom number of rails
def decrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nDecrypt Transposition has been activated!\n")

    # The four Arrays used to decrypt a transposition cipher, in here because I don't want the data to remain outside this function
    ciphertextList = []
    plaintextList = []
    
    # getting plaintext from the user
    input_ciphertext = input("\nWhat is the ciphertext message you want to decode? ") # getting the ciphertext to decrypt
    split_up_ciphertext = split_my_string_in_4(input_ciphertext)

    #number of columns in each column
    numOfCharsInEachColumn = int(len(input_ciphertext) / 4)
    print(numOfCharsInEachColumn)
    for jakes in range(numOfCharsInEachColumn):
        plaintextList.append([])

    print(f"We should have {numOfCharsInEachColumn} in plaintextList = {plaintextList}")

    print(f"Splitting up Plaintext: {split_up_ciphertext}")

    # getting key from user
    input_column_order_key = get_combo_of_1234()

    # append each array in order
    for nums in input_column_order_key:
        ciphertextList.append(split_up_ciphertext[(nums - 1)])

    print(f"After Re order: {ciphertextList}")

    #adding array
    for index,arrays in enumerate(ciphertextList):
        print(f"Index: {index}, Array: {arrays}")
        for index2,character in enumerate(arrays):
            print(f"Index2: {index2}, Array: {character}")

            # if (index2 % numOfCharsInEachColumn) 
                    # if mod is equal to 0, we move to List 0
            plaintextList[index2].append(character)

    # Printing out final array
    print(f"Final Array: {plaintextList}")

    # converting to string
    outbound_plaintext = ''
    for arraysMyBoi in plaintextList:
        for letters in arraysMyBoi:
            outbound_plaintext += letters

    print(f"Final Ciphertext: {outbound_plaintext}")




'''
    # pushing that plaintext into arrays
    for index,character in enumerate(input_ciphertext):
        print(f"Character: {character}")
        print(f"Index: {index}")

        # Get mod 4 of the current char 
        current_mod_of_char = index % 4
        print(f"Current Modulus: {current_mod_of_char}")

        # if mod is equal to 0, we move to List 0
        if (current_mod_of_char == 0):
            ListOfLists[0].append(character)

        # if mod is equal to 1, we move to List 1
        elif (current_mod_of_char == 1):
            ListOfLists[1].append(character)

        # if mod is equal to 2, we move to List 2
        elif (current_mod_of_char == 2):
            ListOfLists[2].append(character)

        # mod has to be equal to 3, we move to List 3
        else:
            ListOfLists[3].append(character)

    print(ListOfLists)

    # getting key from user
    input_column_order_key = get_combo_of_1234()
    
    # Iterating through the array and creating the ciphertext
    # getting ciphertext ready
    outbound_plaintext = ''

    # appending arrays to ciphertext
    for numbers in input_column_order_key:
        print(f"Appending List {(numbers - 1)} as value was: {numbers}")
        print(f"This is ListOfLists{(numbers - 1)}, or: {ListOfLists[(numbers - 1)]}")

        # Changing list to string
        stringify_this = ''.join(ListOfLists[int((numbers - 1))])
        print(f"Stringifying: {stringify_this}")
        outbound_plaintext += stringify_this

        # showing what the current ciphertext is
        print(f"\nCurrent Ciphertext: {outbound_plaintext}\n")

    
    # printing out final ciphertext
    print(outbound_plaintext)
    # Writing Data to a file
    write_to_file(f"Transposition_Decryption_{currentTime}","Trans Plaintext",outbound_plaintext)
'''


'''
# --- Function to ENCRYPT a simple transposition cipher ---
def encrypt(text, key):
    # Create a 2D matrix with the given key
    matrix = [[0 for x in range(key)] for y in range(len(text)//key + 1)]
    k = 0
    for i in range(len(text)//key + 1):
        for j in range(key):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1
            else:
                matrix[i][j] = 'X'

    # Transpose the matrix
    matrix = list(map(list, zip(*matrix)))
    # Join the rows of the transposed matrix and return the result
    return ''.join([''.join(row) for row in matrix])
'''

'''
# --- Function to DECRYPT a simple substitution cipher ---
def decrypt(text, key):
    # Find the number of columns in the original matrix
    cols = len(text)//key + 1
    # Create a 2D matrix with the given key
    matrix = [[0 for x in range(cols)] for y in range(key)]
    k = 0
    for i in range(key):
        for j in range(cols):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1
    # Transpose the matrix
    matrix = list(map(list, zip(*matrix)))
    # Join the rows of the transposed matrix, removing padding characters, and return the result
    return ''.join([''.join(row).rstrip('X') for row in matrix])
'''

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

chooseOperation = input("What kind of operation do you want: ENCRYPT or DECRYPT? ")
print(chooseOperation.upper())
print('\n')

# Catch statement to prevent invalid selections
while chooseOperation == '':
    chooseOperation = input("Can't be left blank, please input either ENCRYPT or DECRYPT: ")

# execute encrypt operation
if chooseOperation.upper() == 'ENCRYPT':
    encrypt_transposition()

# execute decrypt operation
elif chooseOperation.upper() == 'DECRYPT':
    decrypt_transposition()

# if nonsense, end the script
else:
    print("Response Not Recognized, Ending Program...")