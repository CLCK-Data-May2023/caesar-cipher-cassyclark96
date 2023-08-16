# add your code here
#create alphabet list
letters = "abcdefghijklmnopqrstuvwxyz"

#function to shift letters in original message over 5 spaces
def encrypt(message, shift):

    encrypted_message = " "

    for letter in message:
        if letter in letters:
            index = letters.index(letter)
            shifted_index = (index + shift) % len(letters)
            encrypted_message += letters[shifted_index]
        else:
            encrypted_message += letter

    return encrypted_message

shift = 5
input_message = input("Please enter a sentence: ")
encrypted_message = encrypt(input_message.lower(), shift)

print("The encrypted sentence is:", encrypted_message)