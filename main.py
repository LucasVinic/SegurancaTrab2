#! /usr/bin/python3
from aes import aes_main
import os

# Test vector 128-bit key
key = '000102030405060708090a0b0c0d0e0f'

# next step: get data from file
data = '000000012345670000000abcde000000'

# encrypt data
encrypted = aes_main(data, key, False)
print(f"encrypted: {encrypted}")

# Decrypt data with the same key
decripted = aes_main(encrypted, key, True)
print(f"decrypted: {decripted}")
