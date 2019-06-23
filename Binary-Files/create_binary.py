binary_message = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
file = open("zeros.bin","wb")
file.write(binary_message)
file.close()

binary_message = b'\x00\x01\x03\x07\x0f\x1f\x3f\x7f\xff'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x01\x03\x07\x0f\x1f\x3f\x7f\xff'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
binary_message += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
file = open("crescent_pattern.bin","wb")
file.write(binary_message)
file.close()

binary_message = b'\x01\xc2\x31\x5b\xcf\x11\x6e\xc6\x75\x15\xb5\x7d\xa8\x9e\xcd\x68'
binary_message += b'\x14\x18\x59\x25\xa4\x70\xb9\xc1\xe9\x63\x19\xb0\x02\x3e\x9f\x53'
binary_message += b'\xfa\x43\xf2\xcd\x1c\x99\xb5\x7c\x6b\x3b\x88\xf4\xf9\x02\xfe\x25'
binary_message += b'\x66\xeb\xc4\x64\xf9\x7b\x22\x12\x5f\x51\x66\xfd\xaf\x2e\xf1\xbb'
binary_message += b'\xfe\xc2\xfe\xfc\xe4\x52\xfb\x86\x02\x0a\x55\xeb\x29\xf2\xfc\x93'
binary_message += b'\x63\xdb\x0f\x12\xc4\xc3\x02\x0a\x01\xa0\xfb\x18\x4d\x3f\x5b\x9a'
binary_message += b'\x67\x6b\x1d\x36\x16\x21\x70\x8c\x70\x27\x3d\x9f\x12\xdd\x20\xf1'
binary_message += b'\xd5\x9b\x34\xb3\xab\xd1\x1c\x9a\x99\x2a\x02\x13\x72\xad\x32\x7c'
binary_message += b'\x5d\x14\x86\xbd\xf4\x42\x1f\xb7\x28\xa3\x66\xb4\x94\x7c\xa5\xe6'
binary_message += b'\x81\xe9\xe4\x7c\x86\x61\xa3\x5b\x4e\x54\x5e\xd6\xde\xc6\x77\xe8'
binary_message += b'\xd3\xe3\x28\x26\x64\x14\x2e\xbe\xb6\xaf\x7b\xc8\x43\x43\x02\x45'
binary_message += b'\x8b\x62\xa5\x38\x7e\xf7\xb7\x4a\x9f\x7f\x02\xe9\xea\x18\x50\x05'
file = open("random.bin","wb")
file.write(binary_message)
file.close()

message = "Hello FloripaSat-I"
binary_message = bytearray(message,'utf8')
binary_message += b'\x66\xeb\xc4\x64\xf9\x7b\x22\x12\x5f\x51\x66\xfd\xaf\x2e\xf1\xbb'
binary_message += b'\xfe\xc2\xfe\xfc\xe4\x52\xfb\x86\x02\x0a\x55\xeb\x29\xf2\xfc\x93'
binary_message += b'\x63\xdb\x0f\x12\xc4\xc3\x02\x0a\x01\xa0\xfb\x18\x4d\x3f'
binary_zeros = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
for i in range(20):
    binary_message += binary_zeros
file = open("hello.bin","wb")
file.write(binary_message)
file.close()

#Preamble + Hello string

preamble = b'\xaa\xaa\xaa\xaa\x5d\xe6\x2a\x7e'
message = "Hello FloripaSat-I"
binary_message = preamble
binary_message += bytearray(message,'utf8')
binary_message += b'\x66\xeb\xc4\x64\xf9\x7b\x22\x12\x5f\x51\x66\xfd\xaf\x2e\xf1\xbb'
binary_message += b'\xfe\xc2\xfe\xfc\xe4\x52\xfb\x86\x02\x0a\x55\xeb\x29\xf2\xfc\x93'
binary_message += b'\x63\xdb\x0f\x12\xc4\xc3\x02\x0a\x01\xa0\xfb\x18\x4d\x3f'
binary_zeros = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
for i in range(20):
    binary_message += binary_zeros
file = open("preamble_hello.bin","wb")
file.write(binary_message)
file.close()
