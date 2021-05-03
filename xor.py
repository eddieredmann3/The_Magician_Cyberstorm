###########################################################################
# The Magician
# Alex Davis, Landon Jackson, Skyler McAffry, Mary Nations, Matt Post,
# Eddie Redmann, Brandon Rogers, Thomas Schwartzenburg
###########################################################################
from sys import *

def read_file(infile):
    # this function aims to read a file byte by byte and 
    # to covnvert that to a list of integers, which we can
    # perform the xor operation on
    char_vals = [] 
    chars = []
    fb = infile.read(1) # reads the first byte
    fb = ord(fb) #gives the UTF-8 value of that byte
    char_vals.append(fb) #appends it to char_vals
    while fb:
        try:
            fb = infile.read(1)
            fb = ord(fb)
            #print(chr(fb))
            char_vals.append(fb)
        # ord() throws a TypeError when it reaches the end of the file
        # because it's trying to perform ord(b'')
        except TypeError:
            break
    #print(chars)
    return char_vals

def xor(msg, key):
    xorlist = []
    #actually doing the xor
    if len(key) > len(msg):
    #checking to see if the key is longer than the messsage
        key_v = key[0:(len(msg))]
    else:
        key_v = []
        while len(key_v) < len(msg):
            for k in key:
                if (len(key_v) == len(msg)):
                    break
                key_v.append(k)
    for i in range(len(key_v)):
        xc = msg[i]^key_v[i] # '^' is the python bitwise xor operator 
        xorlist.append(xc)
    return xorlist

def convert_message(x_list):
    message = ""
    #takes the xor list of characters and creates the message
    for char in x_list:
        x = chr(char)
        message += x
    return message

data = stdin.buffer

#gets the key file and reads its contents as bytes
k = "key2"
f = open(k, "rb")
msg = read_file(data)
key = read_file(f)
f.close()
data.close()
xor_vals = xor(msg, key)

print(convert_message(xor_vals))
