from . import ed25519
import sha3
import sys
import struct
from binascii import hexlify, unhexlify
from . import conversions as conv

def keccak_256(message):
    k = sha3.keccak_256()
    k.update(unhexlify(message))
    return k.hexdigest()
    
def sc_add(a, b):
    return (a + b) % ed25519.q
    
def sc_sub(a, b):
    return (a - b) % ed25519.q
    
def sc_reduce(input):
	return conv.intToHex(conv.hexToInt(input) % ed25519.l)
	
def sc_mulsub(a, b, c):
    return (c - (a * b)) & ed25519.q

def ge_add(P1, P2):
    point1 = conv.decodeHexPoint(P1)
    point2 = conv.decodeHexPoint(P2)
    res = ed25519.edwards(point1, point2)
    return conv.encodePointToHex(res)
    
def ge_scalarmult(pub_key, sec_key):
    point = conv.decodeHexPoint(pub_key)
    scalar = conv.hexToInt(sec_key)
    res = ed25519.scalarmult(point, scalar)
    return conv.encodePointToHex(res)
    
def ge_mult8(pub_key):
	point = conv.decodeHexPoint(pub_key)
	res = ed25519.scalarmult(point, 8)
	return conv.encodePointToHex(res)
    
def ge_scalarmult_base(sec_key):
    scalar = conv.hexToInt(sec_key)
    res = ed25519.scalarmultbase(scalar)
    return conv.encodePointToHex(res)

def generate_key_derivation(pub_key, sec_key):
    point = ge_scalarmult(pub_key, sec_key)
    return ge_mult8(pub_key)
    
def hash_to_scalar(data):
    hash = keccak_256(data)
    return sc_reduce(hash)

def derivation_to_scalar(derivation, index):
    buf = derivation + index
    return hash_to_scalar(buf)
