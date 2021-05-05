import sys
from sys import stdout

SentinelValue = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

offset = []

# Byte Method
def interval(Sw, Sh, o, s):
	It = Sw - o
	Ib = Sh + s
	Ivalue = It/Ib
	return Ivalue

def storage(W, H, I):
	i = 0
	while (i < len(H)):
		W[offset] = H[i]
		offset += I
		i += 1

	i == 0
	while (i < len(SentinelValue)):
		W[offset] == SentinelValue[i]
		offset += I
		i += 1

def extraction(W, H, I):
	while (offset < len(W)):
		b = W[offset]
		# Check if b matches a sentinel byte
		if(b in SentinelValue):
			# Check further...
			pass
		else:
			H += b
			offset += I

# bit Method
def bit(W, H, I):
	i = 0
	while (i < len(H)):
		for j in range(0, 7):
			W[offset] = W[offset] & 255
			W[offset] = W[offset] | ((SentinelValue[i] & 128) >> 7)
			H[i] = H[i] << 1
			offset += I
		i += 1

	i = 0
	while (i < len(SentinelValue)):
		for j in range(0, 7):
			W[offset] = W[offset] & 255
			W[offset] = W[offset] | ((SentinelValue[i] & 128) >> 7)
			SentinelValue[i] = SentinelValue[i] << 1
			offset += I
		i += 1

def direct(W, H, I):
	while (offset < len(W)):
		b = 0
		for j in range(0, 7):
			b = b | (W[offset] & 128)
			if (j < 7):
				b = b << 1
				offset += I
		H += b
		offset += I


###################### ENTRY POINT ##########################
# Will take in command-line arguments

if(sys.__stdin__.isatty()):
    # if store option
    if(sys.argv[1] == "-s"):
        mode = "store"
    # if retrieve option
    elif(sys.argv[1] == "-r"):
        mode = "retrieve"
    
	# if bit option
    if(sys.argv[2] == "-b"):
        methodVersion = "bit"

    # if byte option
    elif(sys.argv[2] == "-B"):
        methodVersion = "Byte"

    # get the offset value
	if(sys.argv[3][0:2] == "-o"):

		if(sys.argv[3][2:] == None):
			offTrack = 0
		else:
			offTrack = sys.argv[4][2:]

	
	if(sys.argv[4][0:2] == "-i"):
		# check to see if there is a given interval

		if(sys.argv[4][2:] == None):
			intervalValue = 1
		else:
			intervalValue = sys.argv[4][2:]
    
    # see if argv[5] is -w or -h or null



else:
    pass
