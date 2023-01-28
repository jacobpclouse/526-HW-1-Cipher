# 526-HW-1-Cipher
> My own cryptographic cipher based off of the 1st homework issued - 526 Cryptography - Spring 2023 
> - Started on 1/28/2023!

## Objectives for this Homework:
Design and implement your own (new) encryption scheme that uses the three operations widely used in classical cryptography: *Substitution*, *Transposition* and *Product*. 

Provide a description of your algorithm and justify the choice of steps and operations used in the algorithm. 
[3+2 = 5 points]

In addition, show that:
- * (a) breaking your algorithm is going to require coding effort (i.e., your algorithm cannot be broken by using pen and paper). [1.5 points]

- * (b) your algorithm is secure against any two cryptanalytic attacks. [1.5 points]


## My Idea:
I want to create something unique that uses random/psuedo random input to 'salt' the password in a way that is very hard to break. I'm thinking of writing one substitution cipher, then a transposition cipher and then trying to combine the two into a final cipher (and add in some extras to spice it up).
- [x] I want these written in: ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
- [ ] Substitution cipher draft has been finished
- [ ] Transposition cipher draft has been finished
- [ ] Combine both programs into the final program
- [ ] Make it uncrackable: Add a random salt to the cipher that prevents freqency analysis (and doesn't make decryption impossibles)
- [ ] Create a Simple GUI for the user to interact with (Tkinter)


## Resources used:
- Basic writing and formatting syntax Github Markdown: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- Difference between Substitution Cipher Technique and Transposition Cipher Technique: https://www.geeksforgeeks.org/difference-between-substitution-cipher-technique-and-transposition-cipher-technique/
- Encyclopaedia Britannica Definitions: 
- * Substitution cipher: https://www.britannica.com/topic/substitution-cipher
- * Transposition cipher: https://www.britannica.com/topic/transposition-cipher
- * Product cipher: https://www.britannica.com/topic/product-cipher
