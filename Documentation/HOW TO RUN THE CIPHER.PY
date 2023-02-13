# ********************************************
# HOW TO RUN JACOB CLOUSE'S CIPHER FOR HM1 526
# ********************************************


'''ENCRYPTION'''

# 1) Move this program into its own folder


# 2) Open either a GIT BASH terminal or BASH TERMINAL and navigate into the folder that contains the program


# 3) Run this program with the command: python jacob-final-cipher.py 
#       NOTE: if you have python2 and python3 installed use this command: python3 jacob-final-cipher.py


# 4) The first thing it will ask you for is if you want to either 'Encrypt' or 'Decrypt', type in 'Encrypt'


# 5) The next thing it will ask you for is the plaintext, enter in the message you want to encode


# 6) It should let you know that a simple subsitution cipher has been activated, then you have to enter in the offset you want to set
#       Any number between 1 and 26


# 7) It should move onto the transposition cipher, and will ask you for a unique sequence of the numbers: 1,2,3,4


# 8) After this, it will move onto the One time pad section, but this will be taken care of automatically
#       This should finish and show you the One time pad key and your final Cipher Text!!
#       It will make two pickle files: CIPHER.pickle and OTP_KEY.pickle - keep these safe, they are your ciphertext and key!
#       A text file containing your output ciphertext will also generate


'''DECRYPTION'''

# 1) This is basically the reverse of encryption, make sure that both CIPHER.pickle and OTP_KEY.pickle are in the 
#       same directory as the jacob-final-cipher.py script and on the same level


# 2) Open up your terminal and run the script again with either: 
#       python jacob-final-cipher.py 
#       python3 jacob-final-cipher.py
# (Again, you will need to run the second one if you have both python2 and python3 installed)


# 3) This time when it asks you what to do enter in 'Decrypt' 


# 4) It will start off with the One time pad function and automatically open both your pickle files
#       You shouldn't have to do anything for this step


# 5) Next it will move on to the transposition function, it will ask you to enter in that combo of 1,2,3,4
#       you had previously used in the encryption step


# 6) Then it will move on to the subsitution function and ask you for the offset you had set


# 7) Finally, it will print out your original plaintext you had encrypted!
#       A text file containing this original plaintext will also be created.