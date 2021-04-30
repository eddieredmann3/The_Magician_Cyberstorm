
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
