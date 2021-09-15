from constant import sbox, rcon, Nk, Nb, Nr
import re
from aux_funct import StateMatrix

def ExpandKey(key):
  # expand key into Nb (Nr + 1) words
  w = ['%08x' % int(x, 16) for x in re.findall('.' * 8, key)]

  i = Nk
  while i < Nb * (Nr + 1):
    temp = w[i - 1]
    if i % Nk == 0:
      temp = '%08x' % (SubWord(RotWord(temp)) ^ (rcon[i // Nk] << 24))
    elif Nk > 6 and i % Nk == 4:
      temp = '%08x' % SubWord(int(temp, 16))
    w.append('%08x' % (int(w[i - Nk], 16) ^ int(temp, 16)))
    i += 1

  return [StateMatrix(''.join(w[x:x + 4])) for x in range(0, len(w), Nk)]

def SubWord(byte):
  # apply a sbox substituition into a 4 byte word
  return ((sbox[(byte >> 24 & 0xff)] << 24) + (sbox[(byte >> 16 & 0xff)] << 16) +
    (sbox[(byte >> 8 & 0xff)] << 8) + sbox[byte & 0xff])

def RotWord(word):
  # permutate a word (ex: [a0, a1, a2, a3] -> [a1, a2, a3, a0])
  return int(word[2:] + word[0:2], 16)
