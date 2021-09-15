from aux_funct import StateMatrix

def MixColumns(state, isInv):
  # operates on the state on each columnas a four-term polynomial.
  # modulo x^4 + 1 with a fixed polynomial a(x).  
  if isInv: fixed = [14, 9, 13, 11]; state = StateMatrix(''.join(state))
  else: fixed = [2, 1, 1, 3]
  columns = [state[x:x + 4] for x in range(0, 16, 4)]
  row = [0, 3, 2, 1]
  col = 0
  output = []
  for _ in range(4):
    for _ in range(4):
      # noinspection PyTypeChecker
      output.append('%02x' % (
        multEight(int(columns[row[0]][col], 16), fixed[0]) ^
        multEight(int(columns[row[1]][col], 16), fixed[1]) ^
        multEight(int(columns[row[2]][col], 16), fixed[2]) ^
        multEight(int(columns[row[3]][col], 16), fixed[3])))
      row = [row[-1]] + row[:-1]
    col += 1
  return output

def multEight(a, b):
  # multEight multiplication of 8 bit characters a and b
  p = 0
  for counter in range(8):
    if b & 1: p ^= a
    hi_bit_set = a & 0x80
    a <<= 1
    # keep a 8 bit
    a &= 0xFF
    if hi_bit_set:
      a ^= 0x1b
    b >>= 1
  return p
