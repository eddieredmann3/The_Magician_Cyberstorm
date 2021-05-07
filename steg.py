import sys
import os

SentinelValue = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

#this function reads files and returns them as byte arrays
def read_file(file):
	#open the file in read/byte mode
	infile = open(file, 'rb')
	#create an empty byte array
	bytearr = bytearray()
	while True:
		#read a single byte
		newByte = infile.read(1)
		if not newByte:
			break
		#turn byte to int
		newByte = ord(newByte)
		#add new byte to byte array
		bytearr.append(newByte)
	infile.close()
	return bytearr

def byteStorage(wrapper, hidden, interval, offset):
	i = 0
	#set the designated wrapper bits to the hidden bit
	while (i < len(hidden)):
		wrapper[offset] = hidden[i]
		offset += interval
		i += 1

	#add the sentinel
	i = 0
	while (i < len(SentinelValue)):
		wrapper[offset] = SentinelValue[i]
		offset += interval
		i += 1
	return wrapper

def byteExtraction(wrapper, offset, interval):
	hidden = bytearray()
	while (offset < len(wrapper)):
		b = wrapper[offset]
		# Check if b matches a sentinel byte
		if(b == SentinelValue[0]):
			# Check further...
			tempB = b
			sentinelHit = True
			for i in range(1, 6):
				# check for all sentinel values
				if((tempB + (offset * i)) != SentinelValue[i]):
					sentinelHit = False
					break
			#break while loop and return hidden if the sentinel was reached
			if(sentinelHit == True):
				break
		# Add b to hidden
		hidden.append(b)
		offset += interval
	return hidden


# bit Method
def bitStorage(wrapper, hidden, interval):
	i = 0
	while (i < len(hidden)):
		for j in range(0, 7):
			wrapper[offset] = wrapper[offset] & 254
			wrapper[offset] = wrapper[offset] | ((hidden[i] & 128) >> 7)
			hidden[i] = hidden[i] << 1
			offset += interval
		i += 1

	i = 0
	while (i < len(SentinelValue)):
		for j in range(0, 7):
			wrapper[offset] = wrapper[offset] & 254
			wrapper[offset] = wrapper[offset] | ((SentinelValue[i] & 128) >> 7)
        		
			SentinelValue[i] = SentinelValue[i] << 1
			offset += interval
		i += 1
	return wrapper

def bitExtraction(wrapper, offset, interval):
	#used for looking for the sentinel
	sentinelCheck = []
	sentinelSearch = False
	hidden = bytearray()
	while (offset < len(wrapper)):
		bit = 0
		#for all 8 bits in the byte
		for j in range(0, 8):
			bit = bit | ((wrapper[offset]) & 1)
			if (j < 7):
				bit = bit << 1
				offset += interval

		# Check if bit (now a full byte) matches a sentinel byte
		if(bit == SentinelValue[0]):
			sentinelSearch = True
		# Check further...
		if(sentinelSearch == True):
			sentinelCheck.append(bit)
			#if our array is the length of the sentinel
			if(len(sentinelCheck) == 6):
				if(sentinelCheck == SentinelValue):
					break
				#else, restart the search
				else:
					sentinelCheck = []
					sentinelSearch = False
		hidden.append(bit) 
		offset += interval
	return hidden


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

#set interval, offset, and hidden defaults
interval = 1
offset = 0
hidden = "null"

#check for offset, interval, wrapper, and hidden
for i in range(3,7):
	try:
		current = sys.argv[i]
		if(current[0] != '-'):
			print("dashes ('-') must be placed before all arguments")
		#offset
		if(current[1] == 'o'):
			offset = int(current[2:])

		#interval
		elif(current[1] == 'i'):
			interval = int(current[2:])

		#wrapper
		elif(current[1] == 'w'):
			wrapper = current[2:]

		#hidden
		elif(current[1] == 'h'):
			hidden = current[2:]

		#incorrect parameter
		else:
			print("incorrect parameter; possible parameters are -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
	#if there are no more parameters
	except:
		break

#if no wrapper file is given, ensure we are in retrieve mode
if((mode != "retrieve") and (hidden == "null")):
	print("a hidden file argument is required for store mode; should be -h<val>")

#open wrapper file in byte mode and read it
wrapper = read_file(wrapper)

# Start method calling
if(methodVersion == "byte"):
	if(mode == "store"):
		wrapper = byteStorage(wrapper, hidden, interval, offset)
		sys.stdout.buffer.write(wrapper)
	elif(mode == "retrieve"):
		hidden = byteExtraction(wrapper, offset, interval)
		sys.stdout.buffer.write(hidden)
	else:
		print("Problem with mode varible")
elif(methodVersion =="bit"):
    if(mode == "store"):
        wrapper = bitStorage(wrapper, hidden, interval)        
        sys.stdout.buffer.write(wrapper)
    elif(mode == "retrieve"):
        hidden = bitExtraction(wrapper, offset, interval)
        sys.stdout.buffer.write(hidden)
else:
	print("Probelm with methodVersion")

