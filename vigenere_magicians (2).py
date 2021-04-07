#!/usr/bin/env python3

# Program 2:Vigenere
# Team: The Magician
# Date: 3/29/2021

# Imported library
import sys

# Function to encrypt the message
def encrypt(message,key):

    # Stores the message in a list, reds it of spaces, and places it in a new list
    splitMessage = list(message)
    keyAlt = key.split(" ")
    keyString = ""
    for i in keyAlt:
        keyString += i
    splitkey = list(keyString)

    # Space for encrypted value and placement value
    EncryptedValue = ""
    keyPlacement = 0

    # Reduces each letter in key to lower case, then turns into number, which is modified to follow the same chart we used in class
    for i in range(len(splitkey)):
        splitkey[i] = splitkey[i].lower()
        splitkey[i] = ord(splitkey[i])
        splitkey[i] = splitkey[i] - 97
    
    # Records if it is a special value or not, turns character to an int, and then determines if it is a cap or lowercase letter. The order of upper and lower case values are then recorded
    for charValue in splitMessage:
        otherValue = False
        intCharValue = ord(charValue)

        # If uppercase
        if(intCharValue >= 65 and intCharValue <= 90):
            intCharValue = intCharValue - 65
            casePlacement=True

        # If lowercase
        elif(intCharValue >= 97 and intCharValue <= 122):
            intCharValue = intCharValue - 97
            casePlacement=False

        # Is a other value such as " "
        else:
            otherValue = True
        
        # Calculates altered value via the Vigenere Cipher, then moves placement of key or resets key placement
        if(otherValue == False):
            alteredChar = (intCharValue + splitkey[keyPlacement])

            # Makes lower than 26 to use class chart
            while(alteredChar >= 26):
                alteredChar = alteredChar - 26
            
            # Moves or resets key placement
            if(keyPlacement == len(keyString)-1):
                keyPlacement = 0
            else:
                keyPlacement = keyPlacement + 1

            # Uses dictionary to covert to letter
            alteredChar = dictionary[alteredChar]

            # Makes a capital letter if true
            if(casePlacement == True):
                alteredChar = alteredChar.upper()

        # For other values to convert to normal
        else:
            alteredChar = chr(intCharValue)

        # Adds to encrypted value
        EncryptedValue += alteredChar
    
    #returns encrypted value
    return EncryptedValue


def decrypt(message,key):
    # Stores the message in a list, reds it of spaces, and places it in a new list

    splitMessage = list(message)
    keyAlt = key.split(" ")
    keyString = ""
    for i in keyAlt:
        keyString += i
    splitkey = list(keyString)

    # Space for encrypted value and placement value
    DecryptedValue = ""
    keyPlacement = 0

    # Reduces each letter in key to lower case, then turns into number, which is modified to follow the same chart we used in class
    for i in range(len(splitkey)):
        splitkey[i] = splitkey[i].lower()
        splitkey[i] = ord(splitkey[i])
        splitkey[i] = splitkey[i] - 97
        
    # Records if it is a special value or not, turns character to an int, and then determines if it is a cap or lowercase letter. The order of upper and lower case values are then recorded
    for charValue in splitMessage:
        otherValue = False
        intCharValue = ord(charValue)

        # If uppercase
        if(intCharValue >= 65 and intCharValue <= 90):
            intCharValue = intCharValue - 65
            casePlacement=True
        
        # If lowercase
        elif(intCharValue >= 97 and intCharValue <= 122):
            intCharValue = intCharValue - 97
            casePlacement=False
        
        # If special value
        else:
            otherValue = True
        
        # Calculates altered value via the Vigenere Cipher, then moves placement of key or resets key placement
        if(otherValue == False):
            alteredChar = (26 +intCharValue - splitkey[keyPlacement])

            # Makes less than 26 to use class table
            while(alteredChar >= 26):
                alteredChar = alteredChar - 26

            # Moves or resets key placement
            if(keyPlacement == len(splitkey)-1):
                keyPlacement = 0
            else:
                keyPlacement = keyPlacement + 1
            
            # Uses dictionary to translate numbers to letters
            alteredChar = dictionary[alteredChar]

            # Makes uppercase
            if(casePlacement == True):
                alteredChar = alteredChar.upper()
        # Turns special values back to normal
        else:
            alteredChar = chr(intCharValue)

        # Adds it to decrypted string
        DecryptedValue += alteredChar
    
    # Returns decrypted string
    return DecryptedValue

#MAIN

# Dictionary that is used for conversion
dictionary = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

# Checks to see if input is given
if(sys.__stdin__.isatty()):
    # if encoded
    if(sys.argv[1] == "-e"):
        key = sys.argv[2]
        #print(key)
        while(True):
            try:
                # Gets input, then encodes and gives message
                value = input()
                EncryptedValue = encrypt(value,key)
                sys.stdout.write(EncryptedValue)
                sys.stdout.write("\n")
            except EOFError:
                break
    
    # If decoded
    elif(sys.argv[1] == "-d"):
        key = sys.argv[2]
        while(True):
            try:
                # Gets input then decodes and gives message
                value = input()
                decryptedValue = decrypt(value,key)
                sys.stdout.write(decryptedValue)
                sys.stdout.write("\n")
            except EOFError:
                break


else:
    while(True):
        try:
            key = sys.argv[2]
            if(sys.argv[1] == "-e"):
                while(True):  
                    # Gets input, then encodes and gives message
                    value = sys.stdin.read().rstrip()
                    EncryptedValue = encrypt(value, key)
                    sys.stdout.write(EncryptedValue)


            elif(sys.argv[1] == "-d"):
                key = sys.argv[2]
                while(True):
                    # Gets input then decodes and gives message
                    value = input()
                    decryptedValue = decrypt(value, key)
                    sys.stdout.write(decryptedValue)
        except EOFError:
            break

        
