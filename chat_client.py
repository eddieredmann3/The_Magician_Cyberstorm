# use Python 3
import socket
from sys import stdout
from time import time

#translates binary string to base 10 int
def binTo10(biniList):
    base10List = []
    for b in biniList:
        base10List.append(int(b, 2))
    return base10List

#puts a long string of numbers into a list of 8-bit segments
def bit8Read(bini):
    i = 0
    base10list = []
    while(i < len(bini)):
        #breaks the main string of numbers into 7-bit segments
        base10list.append(bini[i:i+8])
        i+=8
    return base10list

#translates base 10 numbers to ASCII
def ASCIITranslate(b10List):
    ASCIIString = ""
    for b in b10List:
        ASCIIString += chr(b)
    return ASCIIString

def binToASCII(bini):
    binaryList = []
    binaryList = bit8Read(bini)
    #Feeds a list of binary numbers to the binTo10 function
    base10 = binTo10(binaryList)
    #Feeds a list of base 10 numbers to the ASCIITranslate function
    ASCII = ASCIITranslate(base10)
    return ASCII

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.102.120"
port = 31337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# string to hold all 1's and 0's
binary_str = ""

# receive data until EOF
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)

    # if the time of the message is less than 0.05 -> add 0 to binary_str
    if(delta < 0.05):
        delta = 0
        binary_str = binary_str + str(delta)
    # if not, add 1 to binary_str
    else:
        delta = 1
        binary_str = binary_str + str(delta)

    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

# close the connection to the server
s.close()

# if the length of the str is no divisible by 8, take off bits until it is
while(len(binary_str) % 8 != 0):
    binary_str = binary_str[:len(binary_str)-1]

# convert binary_str to ASCII
covert_msg = binToASCII(binary_str)
# get rid of EOF from the end of binary_str
covert_msg = covert_msg[:len(covert_msg)-3]

# display covert_msg
stdout.write(covert_msg + "\n")
stdout.flush()
