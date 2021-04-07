#The Magicians
#Binary to ASCII
#Python 3
#03/23/2021

import sys

#puts a long string of numbers into a list of 7-bit segments
def bit7Read(bini):
    i = 0
    base10list = []
    while(i < len(bini)):
        #breaks the main string of numbers into 7-bit segments
        base10list.append(bini[i:i+7])
        i+=7
    return base10list

#puts a long string of numbers into a list of 8-bit segments
def bit8Read(bini):
    i = 0
    base10list = []
    while(i < len(bini)):
        #breaks the main string of numbers into 7-bit segments
        base10list.append(bini[i:i+8])
        i+=8
    return base10list

#translates binary string to base 10 int
def binTo10(biniList):
    base10List = []
    for b in biniList:
        base10List.append(int(b, 2))
    return base10List

#translates base 10 numbers to ASCII
def ASCIITranslate(b10List):
    ASCIIString = ""
    for b in b10List:
        ASCIIString += chr(b)
    return ASCIIString

#the main driving function that calls all the other functions where appropriate
def binToASCII(bini):
    binaryList = []
    #checks for 8 or 7 bit
    if((len(bini) % 8 == 0) and (len(bini) % 7 == 0)):
        #in this case, print both base7 & base8
        print("base 7: ")
        binaryList = bit7Read(bini)
        base10 = binTo10(binaryList)
        ASCII = ASCIITranslate(base10)
        print(ASCII)
        print("base 8: ")
        binaryList = bit8Read(bini)
    elif(len(bini) % 8 == 0):
        binaryList = bit8Read(bini)
    elif(len(bini) % 7 == 0):
        binaryList = bit7Read(bini)
    #Feeds a list of binary numbers to the binTo10 function
    base10 = binTo10(binaryList)
    #Feeds a list of base 10 numbers to the ASCIITranslate function
    ASCII = ASCIITranslate(base10)
    return ASCII

################################################################################
# Entry Point
################################################################################

# empty sting to put contents of file into
inFile = ""

# get each line from input and put into inFile
for line in sys.stdin:
    inFile += line

# get rid of \n from the string
inFile = inFile.replace('\n','')

# print the output
print(binToASCII(inFile), file = sys.stdout)
