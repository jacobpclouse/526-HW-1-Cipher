# 526-HW-1-Cipher
My own cryptographic cipher based off of the 1st homework issued - 526 Cryptography - Spring 2023
Written in: ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)


## Objectives for this Homework:
Design and implement your own (new) encryption scheme that uses the three operations widely used in classical cryptography: *Substitution*, *Transposition* and *Product*. 

Provide a description of your algorithm and justify the choice of steps and operations used in the algorithm. 
[3+2 = 5 points]

In addition, show that:
- * (a) breaking your algorithm is going to require coding effort (i.e., your algorithm cannot be broken by using pen and paper). [1.5 points]

- * (b) your algorithm is secure against any two cryptanalytic attacks. [1.5 points]


## My Idea:
I want to create something unique that uses random/psuedo random input to 'salt' the password in a way that is very hard to break.
- [ ] Add a random salt to the cipher that prevents freqency analysis (and doesn't make decryption impossibles)
- [ ] Create a Simple GUI for the user to interact with (Tkinter)


## Resources used:
- Difference between Substitution Cipher Technique and Transposition Cipher Technique: https://www.geeksforgeeks.org/difference-between-substitution-cipher-technique-and-transposition-cipher-technique/
