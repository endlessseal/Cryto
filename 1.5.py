from itertools import cycle
x = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'
key_values = cycle([ord(a) for a in key])
output = b''
for each in x:
    output += bytes([ord(each) ^ next(key_values)])
    
print(output.hex())
