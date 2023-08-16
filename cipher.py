# add your code here
#create alphabet list
letters = "abcdefghijklmnopqrstuvwxyz"
shift = 5
input_sentence = input("Please enter a sentence: ")

#function to shift letters in original message over 5 spaces
def encrypt(sentence, shift):

    new_sentence = " "

    for letter in sentence:
        if letter in letters:
            index = letters.index(letter)
            shifted_index = (index + shift) % len(letters)
            new_sentence += letters[shifted_index]
        else:
            new_sentence += letter

    return new_sentence

encrypted_sentence = encrypt(input_sentence.lower(), shift)

print("The encrypted sentence is:" + encrypted_sentence)