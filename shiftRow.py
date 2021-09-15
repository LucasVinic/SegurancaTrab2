from aux_funct import StateMatrix, RevertStateMatrix
import re

def ShiftRows(state, isInv):
  # change state shifting the last three rows with offsets a bunch of times
  offset = 0
  if isInv: state = re.findall('.' * 2, RevertStateMatrix(state))
  for x in range(0, 16, 4):
    state[x:x + 4] = state[x:x + 4][offset:] + state[x:x + 4][:offset]
    if not isInv:
      offset += 1
    elif isInv:
      offset -= 1
  if isInv: return StateMatrix(''.join(state))
  return state
