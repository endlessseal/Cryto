x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

ciphertext = bytes.fromhex(x)
past_letter = ''
highest_value = 0
best_string = ''

for i in range(256):
    output = b''
    for char in ciphertext:
        output += bytes([char ^ i])
    temp = sum(1 for a in output if a in range(65,123))
    if highest_value < temp:
        past_letter = chr(i)
        highest_value = temp
        best_string = output.decode()
        
print(past_letter)
print(highest_value)
print(best_string)
    
