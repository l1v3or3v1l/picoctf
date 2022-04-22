def bintowrd(str):
	for wrd in str.split(' '):
		print(chr(int(wrd, 2)), end='')
	print()

def octtowrd(str):
	for wrd in str.split(' '):
		print(chr(int(wrd, 8)), end='')
	print()

def hextowrd(str):
	for i in range(0, len(str), 2):
		print(chr(int('0x' + str[i] + str[i+1], 16)), end='')
	print()

bintowrd(input("Enter binary : "))
octtowrd(input("Enter octal : "))
hextowrd(input("Enter hexadecimal : "))

# 70656172
# 6c616d70