from Crypto.Util.number import getRandomInteger, long_to_bytes
ciphertext = "1b4eb59dce68c7d5173871ff3211a35bc8d089147c0c4c0f7cdf1b9489d4a640ee173557778095d84d0cd344e213100f2923e8ea96"
known_text = "The flag is: "

ct = bin(int(ciphertext, 16))[2:].zfill(len(ciphertext) * 4)
kt = ''.join(bin(ord(x))[2:].zfill(8) for x in known_text)

class LFSR:
	def __init__(self, size, salt, invert,register = 0):
		assert(size == 17 or size == 25)
		self.size = size
		if register == 0:
		    self.register = ((salt >> 3) << 4) + 8 + (salt & 0x7)
		else :
		    self.register = register
		self.taps = [0, 14]
		if size == 25:
			self.taps += [3, 4]
		self.invert = 1 if invert == True else 0
	def clock(self):
		output = reduce(lambda x, y: x ^ y, [(self.register >> i) & 1 for i in self.taps])
		self.register = (self.register >> 1) + (output << (self.size - 1))

		output ^= self.invert
		return output

def encryptData(key, data):
    assert(key < 2**40)
    data = data.decode("hex")
    
    lfsr17 = LFSR(17, key >> 24, True)
    lfsr25 = LFSR(25, key & 0xffffff, False)
    
    keystream = 0
    for i in range(len(data) * 8):
        keystream <<= 1
        keystream |= lfsr17.clock() ^ lfsr25.clock()
        
    pt = int(data.encode("hex"),16)
    ct = ("%x"%(pt ^ keystream)).rjust(len(data) * 2, "0")
    
    return ct

def decryptData(key, ct):
	return encryptData(key, ct)

def findstream(num):
    lfsr17 = LFSR(17,num,True)
    
    keystream2 = ""
    for i in range(25):
    	keystream2 += str(lfsr17.clock() ^ int(ct[i]) ^ int(kt[i]))
    
    lfsr25 = LFSR(25,0,False,int(keystream2[::-1],2))
    pt = kt[:25]
    for i in range(25,len(ct)):
    	res = lfsr17.clock() ^ lfsr25.clock() ^ int(ct[i])
    	if ( i < len(kt) and  (res != int(kt[i])) ) :
            return False
        else :
    	    pt += str(res)
    return pt

for i in range(1 << 16):
    res = findstream(i)
    if  res != False :
        print(long_to_bytes(int(res, 2)))
