# This Python Program was written on Windows 10 using VScode, your milage may vary based on your OS and configuration.

'''
This is draft 1: I am writing a preliminary substituion cipher to later incorporate into my final cipher
'''

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


# --- Function for a simple substitution cipher ---
def simple_substitution():
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

    print(f"Output Array: {ciphertextArray}")



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MAIN PROGRAM
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# myTest = 'Plan 9 From outer Space'
# myPlaintextLettersArray = []
# print(myTest, myTest.isalpha())
# for letters in myTest:
#     # Checking to see if it is a letter, if not we don't lowercase it
#     print(letters, letters.isalpha())
#     if (letters.isalpha()) == True: 
#         print("This is a letter")
#         lowerCaseLetter = letters.lower()
#     else:
#         print('NOT A LETTER')
#         lowerCaseLetter = letters

#     print(f"Current Character: {lowerCaseLetter}, Letter Value: {lettersToNumbersDict[lowerCaseLetter]}")
#     myPlaintextLettersArray.append(lettersToNumbersDict[lowerCaseLetter])

# print(f"Output Array: {myPlaintextLettersArray}")

simple_substitution()