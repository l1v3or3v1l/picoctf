import string

ALPHABET = 'abcdefghijklmnop'

def b16_decode(encoded):
	dec = ""
	for c in [encoded[i:i+2] for i in range(0, len(encoded), 2)]:
		dec += chr(int(format(ord(c[0]) - ord("a"), "#06b") + format(ord(c[1]) - ord("a"), "#06b")[2:], 2))
	return dec

def reverse_shift(c, k):
	t1 = ord(c) - 97
	t2 = ord(k) - 97
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

#flag = "redacted"
#key = "redacted"

# key is any one char of 'abcdefghijklmnop'

#assert all([k in ALPHABET for k in key])
#assert len(key) == 1

#b16 = b16_encode(flag)

# reverse shift
dec = []
reverse_flag = input()
for key in 'abcdefghijklmnop':
	enc = ""
	for i, c in enumerate(reverse_flag):
		enc += reverse_shift(c, key)
	#print(enc)
	dec.append(enc)

# b16 decode
for each in dec:
	print(b16_decode(each) + "\n\n")
