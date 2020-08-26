from Crypto.Util.number import getRandomInteger
salt = 1234123412341234
register1 = (salt >> 3)
register2 = ((salt >> 3) << 4)
register3 = ((salt >> 3) << 4) + 8
register = ((salt >> 3) << 4) + 8 + (salt & 0x7)
# print bin(salt)
# print bin(register1)
# print bin(register2)
# print bin(register3)
# print bin(register)

taps = [0, 14]

# for i in taps : 
#     print i
#     ((register >> i) & 1)
# print [ ((register >> i) & 1) for i in taps ]
print getRandomInteger(5)
print reduce(lambda x, y: x ^ y, [0,0])

# invert = True

# print bin(register)
# output = reduce(lambda x, y: x ^ y, [(register >> i) & 1 for i in taps])
# register = (register >> 1) + (output << (16 - 1))
# output ^= invert
# print bin(output)


# print bin(register)
# output = reduce(lambda x, y: x ^ y, [(register >> i) & 1 for i in taps])
# register = (register >> 1) + (output << (16 - 1))
# output ^= invert
# print bin(output)

# print bin(register)
# output = reduce(lambda x, y: x ^ y, [(register >> i) & 1 for i in taps])
# register = (register >> 1) + (output << (16 - 1))
# output ^= invert
# print bin(output)

# print bin(register)
# output = reduce(lambda x, y: x ^ y, [(register >> i) & 1 for i in taps])
# register = (register >> 1) + (output << (16 - 1))
# output ^= invert
# print bin(output)
