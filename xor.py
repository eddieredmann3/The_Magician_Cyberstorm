from sys import *

METHOD = 10
def xor(msg, key):
    if len(msg) <= len(key):
        key = key[:len(msg)-1]
        key = int(key)
        msg = int(msg)
        cipher = key^msg
    else:
        count = 0
        msg_i = int(msg)
        cipher = ""
        while len(msg) > count:
            subset = msg[count:count+len(msg)-1]
            subset = int(subset)
            temp = subset^msg_i
            temp = bin(temp)[2:]
            cipher += temp
            count += len(key)
    cipher = bin(cipher)[2:]
    return cipher

def decode(msg):
    #stores binary strings for each character
    binaryCharacters = []
    i = 0
    while(i < len(msg)):
        #breaks the main string of numbers into 7-bit segments
        binaryCharacters.append(msg[i:i+METHOD])
        i+=METHOD
    #translates binary to base 10
    base10Characters = []
    for b in binaryCharacters:
        base10Characters.append(int(b, 2))
    #translates base 10 to ASCII
    ASCIICharacters = ""
    for c in base10Characters:
        ASCIICharacters += chr(c)
    return ASCIICharacters

data = stdin.buffer.read()
#gets the key file and reads its contents as bytes
k = "key"
f = open(k, "rb")
fc = f.read()
f.close()

#encode    
kv = bin(int.from_bytes(fc, "little"))[2:] #the magic formula for turning key text as binary
mv = bin(int.from_bytes(data, "little"))[2:] #same for the message.

if stdout.isatty():
    #decode
    cipher_text = xor(mv, kv)
    enc_msg = decode(cipher_text)
    print(enc_msg)
else:
    #print(len(mv))
    cipher_text = xor(mv, kv)
    dec_msg = decode(cipher_text)    
    print(dec_msg)
    
   
