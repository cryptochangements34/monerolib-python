import construct
from binascii import hexlify

def readVarInt(data, pop_bytes):
	result = 0
	c = 0
	pos = 0
	while True:
		isLastByteInVarInt = True
		i = int(data[pos], 16)
		if i >= 128:
			isLastByteInVarInt = False
			print i
			i -= 128
		result += (i * (128 ** c))
		c += 1
		pos += 1
		
		if isLastByteInVarInt:
			break
	if pop_bytes:
		for x in range(0, pos):
			data.pop(x)
	return result

def encodeVarInt(data):
    return hexlify(construct.VarInt.build(data))
