import sys
# import Math
import os

SentinelValue = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

#this function reads files and returns them as byte arrays
def read_file(file):
	#create an empty byte array
	bytearr = bytearray()
	pos = 0
	while True:
		#read a single byte
		newByte = file.read(1)
		print(newByte)
		if not newByte:
			break
		#move the file up one byte
		pos += 1
		file.seek(pos)
		#add new byte to byte array
		bytearr.append(newByte)
	return bytearr

def storage(wrapper, hidden, interval):
	i = 0
	while (i < len(hidden)):
		wrapper[offset] = hidden[i]
		offset += interval
		i += 1

	i = 0
	while (i < len(SentinelValue)):
		wrapper[offset] == SentinelValue[i]
		offset += interval
		i += 1
	return wrapper

def extraction(wrapper, offset, interval): ## !! there is no "hidden" to be passed in in this case !!##
	hidden = bytearray()
	print("offset = {}".format(offset))
	print("interval = {}".format(interval))
	print("wrapper length = {}".format(len(wrapper)))

	while (offset < len(wrapper)):
		b = wrapper[offset]
		print("b = {}".format(b))
		# Check if b matches a sentinel byte
		if(b == SentinelValue[0]):
			# Check further...
			tempB = b
			sentinelHit = True
			for i in range(1, 6):
				# check for all sentinel values
				if((tempB + (offset * i)) != SentinelValue[i]):
					sentinelHit = False
			#break while loop and return hidden if the sentinel was reached
			if(sentinelHit == False):
				break
		# Add b to hidden
		else:
			hidden.append(b)
			print("hidden = {}".format(hidden))
			offset += interval
	return hidden


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
	offset = sys.argv[3]
	#check that the correct argument was given
	if(offset[0] != '-' and offset[1] != 'o'):
		print("third argument should be -o<val> (for offset)")
	else:
		offset = int(offset[2:])
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



# see if argv[5] is -w or -h or null	##!! I don't think this comment matches what's under it. !!##
# w_size = os.path.getSize(wrapper)		##!! This is not used, should we takeit out? !!##

#open wrapper file in byte mode and read it
infile = open(wrapper, "rb")
wrapper = read_file(infile)
infile.close()

sys.stdout.buffer.write(wrapper)


# Start method calling
if(methodVersion == "byte"):
	if(mode == "store"):
		wrapper = storage(wrapper, hidden, interval)
		sys.stdout.buffer.write(wrapper)
	elif(mode == "retrieve"):
		hidden = extraction(wrapper, offset, interval)
		print(hidden)
		sys.stdout.buffer.write(hidden)
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

