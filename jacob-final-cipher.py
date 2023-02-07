# This Python Program was written on Windows 10 using VScode, your milage may vary based on your OS and configuration.

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import datetime # used to get the datetime for "defang_datetime" function


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Variables
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# To convert intial plaintext to number values
lettersToNumbersDict = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
    # ' ':'-',
    # '1':'!',
    # '2':'@',
    # '3':'#',
    # '4':'$',
    # '5':'%',
    # '6':'^',
    # '7':'&',
    # '8':'*',
    # '9':'(',
    # '0':')'

}

# To convert finished numbers back into finished ciphertext
numbersTolettersDict = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z'
    # '-':' ',
    # '!':1,
    # '@':2,
    # '#':3,
    # '$':4,
    # '%':5,
    # '^':6,
    # '&':7,
    # '*':8,
    # '(':9,
    # ')':0
}


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


# --- Function to return a combination of 1,2,3 and 4 with each number being used only once --- Trans Specific
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


# --- Function to get remainder and let us know how many spaces to add --- Trans Specific
def get_remainder(input_string):
    # print(input_string)
    # getting length of input
    length_of_input = len(input_string)
    # print(f"Length: {length_of_input}")
    number_of_spaces_to_add = 4 - (int(length_of_input) % 4)
    # print(number_of_spaces_to_add)
    return int(number_of_spaces_to_add)


# --- Function to ENCRYPT a simple substitution cipher --- Sub Specific
def encrypt_substitution():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nSimple Sub has been activated!\n")
    input_offset_key = input("What is the offset key you want? ") # getting the offest value from the user
    input_plaintext = input("\nWhat is the plaintext message you want to encode? ") # getting the plaintext to encrypt


    # Converts the plaintext into corresponding numbers
    # myPlaintextLettersArray = []
    ciphertextArray = []
    for letters in input_plaintext:

        # Checking to see if it is a letter, if not we don't lowercase it
        # print(letters, letters.isalpha())
        if (letters.isalpha()) == True: 
            # print("This is a letter")

            # Lowercasing - prevents issues with capital letters
            lowerCaseLetter = letters.lower()

            # Why not change it into the cipher text right now if we have the offset?
            # The algorithm for substitution ciphers basically is: (Plaintext_Letter_Val + Offset_Val) mod 26 = Cipher_Letter_Val 
            plaintextValue = lettersToNumbersDict[lowerCaseLetter]
            covertedToCipherValue = (int(plaintextValue) + int(input_offset_key)) % 26

            # We have the cipher value, now we just need to convert it to the ciphertext letter
            convertedToCipherLetter = numbersTolettersDict[covertedToCipherValue]
            print(f"Current Character: {lowerCaseLetter}, Character Value: {lettersToNumbersDict[lowerCaseLetter]}, Cipher Value: {covertedToCipherValue}, Cipher Letter: {convertedToCipherLetter}")

            # Append to the array
            ciphertextArray.append(convertedToCipherLetter)


        else:
            # print('NOT A LETTER')
            print(f"Current Character: {letters}, Appending to Array as is...")
            # myPlaintextLettersArray.append(lettersToNumbersDict[letters])
            ciphertextArray.append(letters)

    print(f"Output Array: {ciphertextArray}\n")

    # Turn array into a string
    cipherText = ''
    for characters in ciphertextArray:
        cipherText += characters
    
    print(f"Ciphertext: {cipherText}")
    # Writing Data to a file
    write_to_file(f"Subsitution_Encryption_{currentTime}","Sub CipherText",cipherText)


# --- Function to DECRYPT a simple substitution cipher --- Sub Specific
def decrypt_substitution():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nDecrypt Sub has been activated!\n")

    input_offset_decrypt_key = input("What is the offset key set to? ") # getting the offest decrypt key from the user
    input_ciphertext = input("\nWhat is the Ciphertext message you want to decode? ") # getting the ciphertext to decrypt

    # Converts the ciphertext into corresponding numbers
    PlaintextArray = []
    for letters in input_ciphertext:

        # Checking to see if it is a letter, if not we don't lowercase it
        # print(letters, letters.isalpha())
        if (letters.isalpha()) == True: 
            # Lowercasing - prevents issues with capital letters
            lowerCaseLetter = letters.lower()

            # Why not change it into the plain text right now if we have the offset?
            # If we reverse the algorithm for substitution, the forumla is: (Cipher_Letter_Val - Offset_Val) mod 26 = Orig_Plaintext_Letter_Val 
            cipherValue = lettersToNumbersDict[lowerCaseLetter]
            covertedToPlaintextValue = (int(cipherValue) - int(input_offset_decrypt_key)) % 26

            # We have the plaintext value, now we just need to convert it to the original letter
            convertedToPlaintextLetter = numbersTolettersDict[covertedToPlaintextValue]
            print(f"Current Cipher Character: {lowerCaseLetter}, Character Value: {lettersToNumbersDict[lowerCaseLetter]}, Plaintext Value: {covertedToPlaintextValue}, Original Letter: {convertedToPlaintextLetter}")

            # Append to the array
            PlaintextArray.append(convertedToPlaintextLetter)


        else:
            print(f"Current Character: {letters}, Appending to Array as is...")
            PlaintextArray.append(letters)

    print(f"Output Array: {PlaintextArray}\n")

    # Turn array into a string
    plainText = ''
    for characters in PlaintextArray:
        plainText += characters
    
    print(f"Ciphertext: {plainText}")

    # Writing Data to a file
    write_to_file(f"Subsitution_Decryption_{currentTime}","Retrieved Plaintext",plainText)


# --- Function to ENCRYPT a simple transposition cipher ---
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


# --- Function to DECRYPT a simple substitution cipher ---
def decrypt_transposition():
    currentTime = defang_datetime()
    print(f"Current Date/Time: {currentTime}")
    myLogo()
    print("\nDecrypt Transposition has been activated!\n")

    # The four Arrays used to decrypt a transposition cipher, in here because I don't want the data to remain outside this function
    ListOfLists = [[],[],[],[]]

    # getting plaintext from the user
    input_ciphertext = input("\nWhat is the ciphertext message you want to decode? ") # getting the ciphertext to decrypt



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



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# 1st: get the substitution program working, then take the out put and pipe it into the transpostion - encryption works
# 2nd: reverse it for decryption: first transpose and then substitute to decrypt
# 3rd: verify encrypt to decrypt works fully with one pass each
# 4th: add an additional subsitution (either after 1st sub or the transposition) -- add more if you want
# 5th: see if you can break it with two cryptoanalyical methods - if not, then you are done!
# 6th: make a video on this explaining it from start to finish


# test sub -- both working, just need to have it return value for **encryption** instead of making file
#encrypt_substitution()
#decrypt_substitution()


# test trans -- both working, just need to have it return value for **decrpytion** instead of making file
#encrypt_transposition()
#decrypt_transposition()