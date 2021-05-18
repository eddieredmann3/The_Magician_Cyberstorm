
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

    pos = 0
    while True:
        fb = infile.read(1)
        if not fb:
            break
        pos += 1
        infile.seek(pos)
        fb = ord(fb)
        char_vals.append(fb)
    return char_vals

def xor(msg, key):
    xorlist = []
    #actually doing the xor
    if len(key) >= len(msg):
    #checking to see if the key is longer than the messsage
        key_v = key[0:(len(msg))]
    #if the key is shorter than the message...
    else:
        key_v = []
        #repeat the key until it is the length of the message
        while len(key_v) < len(msg):
            for k in key:
                if (len(key_v) == len(msg)):
                    break
                key_v.append(k)
        
    for i in range(len(key_v)):
        xc = msg[i]^key_v[i] # '^' is the python bitwise xor operator
        xc = xc.to_bytes(1, "big")
        xorlist.append(xc)
    return xorlist

def convert_message(x_list):
    #message = ""
    #takes the xor list of characters and creates the message
    for char in x_list:
        stdout.buffer.write(char)

data = stdin.buffer

#gets the key file and reads its contents as bytes
k = "key2"
f = open(k, "rb")
msg = read_file(data)
key = read_file(f)
f.close()
data.close()
xor_vals = xor(msg, key)

#print(xor_vals[:10])
convert_message(xor_vals)
