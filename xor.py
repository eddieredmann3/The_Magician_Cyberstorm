from sys import *

#METHOD = 10
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


data = stdin.buffer.read()
#gets the key file and reads its contents as bytes
k = "key"
f = open(k, "rb")
fc = f.read()
f.close()

print(data)
#encode    
kv = bin(int.from_bytes(fc, "little"))[2:] #the magic formula for turning key text as binary
mv = bin(int.from_bytes(data, "little"))[2:] #same for the message.

print(mv)
print()
print(kv)
print()
print(xor(mv, kv))
