import re
from aux_funct import StateMatrix, RevertStateMatrix
from constant import sbox, rsbox
from shiftRow import ShiftRows
from mixColumn import MixColumns
from constant import Nr

def Cypher(expandedKey, data):
  state = AddRoundKey(StateMatrix(data), expandedKey[0])
  for r in range(Nr - 1):
    state = SubBytes(state, False)
    state = ShiftRows(state, False)
    state = StateMatrix(''.join(MixColumns(state, False)))
    state = AddRoundKey(state, expandedKey[r + 1])

  state = SubBytes(state, False)
  state = ShiftRows(state, False)
  state = AddRoundKey(state, expandedKey[Nr])
  return RevertStateMatrix(state)

def InvCypher(expandedKey, data):
  state = AddRoundKey(re.findall('.' * 2, data), expandedKey[Nr])

  for r in range(Nr - 1):
    state = ShiftRows(state, True)
    state = SubBytes(state, True)
    state = AddRoundKey(state, expandedKey[-(r + 2)])
    state = MixColumns(state, True)

  state = ShiftRows(state, True)
  state = SubBytes(state, True)
  state = AddRoundKey(state, expandedKey[0])
  return ''.join(state)

def AddRoundKey(state, key):
  return ['%02x' % (int(state[x], 16) ^ int(key[x], 16)) for x in range(16)]

def SubBytes(state, isInv):
  if not isInv: return ['%02x' % sbox[int(state[x], 16)] for x in range(16)]
  elif isInv: return ['%02x' % rsbox[int(state[x], 16)] for x in range(16)]
