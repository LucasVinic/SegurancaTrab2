import re
from expandKey import ExpandKey
from aux_funct import RevertStateMatrix
from cypher import Cypher, InvCypher
from aux_funct import block_data, pad, unpad

def key_handler(key, isInv):
  # Return the expanded key
  if not isInv: return ExpandKey(key)
  # Return the inverse expanded key
  if isInv: return [re.findall('.' * 2, RevertStateMatrix(x)) for x in ExpandKey(key)]

def aes_main(data, key, isInv, mode='ecb'):
  expanded_key = key_handler(key, isInv)
  if mode == 'ecb': return ecb(data, expanded_key, isInv)
  # add ctr below

def ecb(data, expanded_key, isInv):
  if isInv: return InvCypher(expanded_key, data)
  else: return Cypher(expanded_key, data)
