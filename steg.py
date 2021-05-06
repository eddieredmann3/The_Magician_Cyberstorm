import sys
import Math
import os

SentinelValue = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

offset = []

# Byte Method
#def interval(Sw, Sh, o): #Sw is the size of wrapper, Sh is the size of the hidden file,
#o is the size of the offset
#	It = Sw - o
#	Ib = Sh + len(SentinelValue)
#	Ivalue = Math.floor(It/Ib)
#	return Ivalue

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
def bitStorage(W, H, I):
	i = 0
	while (i < len(H)):
		for j in range(0, 7):
			W[offset] = W[offset] & 254
			W[offset] = W[offset] | ((SentinelValue[i] & 128) >> 7)
			H[i] = H[i] << 1
			offset += I
		i += 1

	i = 0
	while (i < len(SentinelValue)):
		for j in range(0, 7):
			W[offset] = W[offset] & 254
			W[offset] = W[offset] | ((SentinelValue[i] & 128) >> 7)
        		
			SentinelValue[i] = SentinelValue[i] << 1
			offset += I
		i += 1

def bitExtraction(W, H, I):
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
#try-excepts are used to ensure correct user input

#Store/Retrieve mode
try:
	#print(sys.argv)
	if(sys.argv[1] == "-s"):
	    mode = "store"
	# if retrieve option
	elif(sys.argv[1] == "-r"):
	    mode = "retrieve"
	# if the user put neither
	else:
		print("first argument should be -s (for store) or -r (for retrieve).")
except:
	print("first argument required; should be -s (for store) or -r (for retrieve).")

#Byte/bit mode
try:
	# if bit option
	if(sys.argv[2] == "-b"):
	    methodVersion = "bit"
	# if byte option
	elif(sys.argv[2] == "-B"):
	    methodVersion = "byte"
	else:
		print("second argument should be -b (for bit) or -B (for Byte).")
except:
	print("second argument required; should be -b (for bit) or -B (for Byte).")

#offset
try:
	# get the offset value
	offTrack = sys.argv[3]
	#check that the correct argument was given
	if(offTrack[0] != '-' and offTrack[1] != 'o'):
		print("third argument should be -o<val> (for offset)")
	else:
		offTrack = offTrack[2:]
except:
	print("third argument required; should be -o<val> (for offset)")

#interval
try:
	# get given interval
	interval = sys.argv[4]
	if(interval[0] != '-' and interval[1] != 'i'):
		print("fourth argument should be -i<val> (for interval)")
	else:
		interval = interval[2:]
except:
	print("fourth argument required; should be -i<val> (for interval)")

#wrapper
try:
	# check for wrapper	
	wrapper = sys.argv[5]
	if(wrapper[0] != '-' and wrapper[1] != 'w'):
		print("fifth argument should be -w<val> (for wrapper)")
	else:
		wrapper = wrapper[2:]
except:
	print("fifth argument required; should be -w<val> (for wrapper)")


#check for a hidden file
try:
	hidden = sys.argv[6] #this should throw an error and go to "except" if no argument is given
	if(hidden[0] != '-' and hidden[1] != 'h'):
		print("sixth argument should be -h<val> (for hidden)")
	else:
		hidden = hidden[2:]
#if no wrapper file is given, ensure we are in retrieve mode
except:
	if(mode != "retrieve"):
		print("sixth argument is required for store mode; should be -h<val> (for hidden)")



# see if argv[5] is -w or -h or null
w_size = os.path.getSize(wrapper)

#open wrapper file in binary mode
infile = open(wrapper, "rb")

# Start method calling
if(methodVersion == "byte"):
	if(mode == "store"):
		storage(wrapper, hidden, interval)
	elif(mode == "retrieve"):
		extraction(wrapper, hidden, interval)
	else:
		print("Problem with mode varible")
elif(methodVersion =="bit"):
	if(mode == "store"):
		bitStorage(wrapper, hidden, interval)
	elif(mode == "retrieve"):
		bitExtraction(wrapper, hidden, interval)
	else:
		print("Problem with mode varible")
else:
	print("Probelm with methodVersion")




# v  keeping for now, but not neccesary. will probably delete later  v
# if mode == "store":
#     hiddenfile = sys.argv[6][2:]
#     h_size = os.path.getSize(hiddenfile)
#     #setting the interval size
#     file_interval = interval(w_size, h_size, offTrack)
#     print(file_interval)
#     if methodVersion == "Byte":
#         pass
#     else:
#         pass
# else:
#     pass
