import re

def StateMatrix(state):
  # formats a state matrix str into a properly formatted list.
  new_state = []
  split = re.findall('.' * 2, state)
  for x in range(4):
    new_state.append(split[0:4][x]); new_state.append(split[4:8][x])
    new_state.append(split[8:12][x]); new_state.append(split[12:16][x])
  return new_state

def RevertStateMatrix(state):
  # reverts state matrix format as str
  columns = [state[x:x + 4] for x in range(0, 16, 4)]
  return ''.join(''.join([columns[0][x], columns[1][x], columns[2][x], columns[3][x]]) for x in range(4))

# divide binary data into blocks of size 16
def block_data(data):
  size = 16
  return [data[x:x + size] for x in range(0, len(data), size)]

# pad data to size 16
def pad(data):
  block_size = 16
  if len(data) == block_size: return data
  pads = block_size - (len(data) % block_size)
  return data + binascii.unhexlify(('%02x' % int(pads)).encode()) + b'\x00' * (pads - 1)

# remove data padding
def unpad(data):
  p = None
  for x in data[::-1]:
    if x == 0:
      continue
    elif x != 0:
      p = x; break
  data = data[::-1]
  data = data[p:]
  return data[::-1]
