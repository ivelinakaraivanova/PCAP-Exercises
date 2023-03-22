'''
data = bytearray(100)
data[0] = 100
data[1] = 120

try:
    stream = open('bin_file.bin', 'wb')
    stream.write(data)
    stream.close()
except Exception as e:
    print(e)
'''

'''
try:
    bin_text = open('bin_file.bin', 'rb')
    byte_array = bin_text.read()
    bin_text.close()
except Exception as e:
    print(e)

# print(byte_array)

for byte in byte_array:
    print(hex(byte), end='')

print()

for byte in byte_array:
    print(byte, end=' ')
'''


data = bytearray(10)
try:
    bf = open('bin_file.bin', 'rb')
    bf.readinto(data) # bytearray(bf.read())
    bf.close()
except Exception as e:
    print('An error occured:', e)

