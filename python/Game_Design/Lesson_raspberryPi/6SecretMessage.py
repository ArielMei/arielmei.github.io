## Learn how to make your own encryption program. Send and receive secret messages with a friend
## What you will learn?
## 1. iteration over a text string variable (looping)
## 2. find() method
## 3. modulus operator (%)
## 4. Make the input lower case before searching.
## About encrypt: https://projects.raspberrypi.org/en/projects/secret-messages/1
## To encrypt the letter, you just move 3(can be other number) letters clockwise.
## Getting text back to normal is called decryption. To decrypt a word, just subtract the key instead of adding it.

##-------------- Basic ideal ---------------
#alphabet = 'abcdefghijklmnopqrstuvwxyz'  # string
#key = int(input('Please enter your key:'))
#
#character = input('Please enter a character:')
#position = alphabet.find(character)
#newPosition = (position + key) % 26 # Go back to position 0 once it gets to position 26
#newCharacter = alphabet[newPosition]
#
#print(character)
#print('The new character is: ',newCharacter)

## ------------ Encrypting entire messages -------------

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # string
key = int(input('Please enter your key:'))
newMessage = ''

message = input('Please enter a message:')

for character in message:
    if character in alphabet: # skip any character if it's not in the alphabet
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        print('The new character is: ',newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character
    
print('New message is :', newMessage)

## ------------ Decrypting entire messages -------------
print('--------Start decrypting-----------')
realMessage = ''

for character in newMessage:
    if character in alphabet: # skip any character if it's not in the alphabet
        position = alphabet.find(character)
        newPosition = (position - key) % 26
        newCharacter = alphabet[newPosition]
        print('The new character is: ',newCharacter)
        realMessage += newCharacter
    else:
        realMessage += character
    
print('Real message is :', realMessage)
