# add your code here
#create alphabet list
letters = "abcdefghijklmnopqrstuvwxyz"

#function to shift letters in original message over 5 spaces
def encrypt(sentence, shift):

    encrypted_sentence = " "

    for letter in sentence:
        if letter in letters:
            index = letters.index(letter)
            shifted_index = (index + shift) % len(letters)
            encrypted_sentence += letters[shifted_index]
        else:
            encrypted_sentence += letter

    return encrypted_sentence

shift = 5
input_sentence = input("Please enter a sentence: ")
encrypted_sentence = encrypt(input_sentence.lower(), shift)

print("The encrypted sentence is: ", encrypted_sentence)