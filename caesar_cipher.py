"""
This is implementation of a Caesar Cipher! 
There are two functions here

'encrypt' does the encoding of the passed
text. Alphabets are shifted.
'decrypt' does the decoding of the passed
encoded text. 
Program asks the user if the text is to be
encoded or decoded. It also asks the user
the shift of the alphabet. Non-alphabetical
characters are not shifted.

"""

# Lowercase list
small_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) ]

# Uppercase list
big_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1) ]





def encrypt(original_text):
    encrypted_text = [None] * len(original_text)

    for i, letter in enumerate(original_text):
        if letter.islower():
            index = small_alphabet.index(letter)
            new_letter = shifted_small_alphabet[index]
            encrypted_text[i] = new_letter
        elif letter.isupper():
            index = big_alphabet.index(letter)
            new_letter = shifted_big_alphabet[index]
            encrypted_text[i] = new_letter
        else:
            encrypted_text[i] = letter

    return ''.join(encrypted_text)
    
def decrypt(encrypted_text):
    original_text = [None] * len(encrypted_text)

    for i, letter in enumerate(encrypted_text):
        if letter.islower():
            index = shifted_small_alphabet.index(letter)
            new_letter = small_alphabet[index]
            original_text[i] = new_letter
        elif letter.isupper():
            index = shifted_big_alphabet.index(letter)
            new_letter = big_alphabet[index]
            original_text[i] = new_letter
        else:
            original_text[i] = letter
    
    return ''.join(original_text)

while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ['encode', 'decode']:
        print("Invalid choice! Please choose 'encode' or 'decode'.\n")
        continue

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n")) % 26

    # shift is to the left
    shifted_small_alphabet = small_alphabet[(shift):] + small_alphabet[:(shift)]
    shifted_big_alphabet = big_alphabet[(shift):] + big_alphabet[:(shift)]  

    if direction == 'encode':
        print(f"Here's the encoded result: {encrypt(text)}")
    elif direction == 'decode':
        print(f"Here's the decoded result: {decrypt(text)}")


    question = input("Type 'yes' if you want to ago again. "
                "Otherwise type 'no'.\n").lower()
    
    if (question == 'yes'):
        continue
    elif (question == 'no'):
        print("\nThank You. Please visit again.")
        break
    else:
        print("Incorrect response")
        break
