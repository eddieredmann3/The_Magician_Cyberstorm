import sys
from sys import stdout


W = 
H = 

SENTINEL = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

offset = []

def storage():
	i == 0
	while (i < len(H)):
		W[offset] == H[i]
		offset += interval
		i += 1

	i == 0
	while (i < len(SENTINEL)):
		W[offset] == SENTINEL[i]
		offset += interval
		i += 1

def extraction():
	while (offset < len(W)):
		b == W[offset]
		H += b
		offset += interval

def bit():
	i == 0
	while (i < len(H)):
		for j in range(0, 7):
			W[offset] &= 11111110
			W[offset] |= ((SENTINEL[i] & 10000000) >> 7)
			H[i] <<= 1
			offset += interval
		i += 1

	i == 0
	while (i < len(SENTINEL)):
		for j in range(0, 7):
			W[offset] &= 11111110
			W[offset] |= ((SENTINEL[i] 10000000) >> 7)
			SENTINEL[i] <<= 1
			offset += interval
		i += 1

def direct():
	while (offset < len(W)):
		b == 0
		for j in range(0, 7):
			b |= (W[offset] & 10000000)
			if (j < 7):
				b <<= 1
				offset += interval
		H += b
		offset += interval


###################### ENTRY POINT ##########################
# Will take in command-line arguments

if(sys.__stdin__.isatty()):
    # if store option
    if(sys.argv[1] == "-s"):
        stdout.write("STORE\n")
        stdout.flush()
    # if retrieve option
    elif(sys.argv[1] == "-r"):
        stdout.write("RETRIEVE\n")
        stdout.flush()
    # if bit option
    if(sys.argv[2] == "-b"):
        stdout.write("BIT\n")
        stdout.flush()
    # if byte option
    elif(sys.argv[2] == "-B"):
        stdout.write("BYTE\n")
        stdout.flush()
    # get the offset value
    print(sys.argv[3][2:])
    # check to see if there is a given interval
    if(sys.argv[4][0:2] == "-i"):
        print("INTERVAL = " + sys.argv[4][2:])
    # interval not given so sys.argv[4] is -w
    elif(sys.argv[4][0:2] == "-w"):
        print("INTERVAL = 1")
        print("WRAPPER FILE = " + sys.argv[4][2:])
    # see if argv[5] is -w or -h or null
    if(len(sys.argv) >= 6):
        if(sys.argv[5][0:2] == "-w"):
            print("WRAPPER FILE = " + sys.argv[5][2:])
        elif(sys.argv[5][0:2] == "-h"):
            print("HIDDEN FILE = " + sys.argv[5][2:])
    # sys.argv[6] is -h
    if(len(sys.argv) == 7):
        print("HIDDEN FILE = " + sys.argv[6][2:])