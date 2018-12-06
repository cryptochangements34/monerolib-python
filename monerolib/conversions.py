from binascii import hexlify, unhexlify
from . import ed25519

def hexToInt(str):
    return ed25519.decodeint(unhexlify(str))

def intToHex(int):
    return hexlify(ed25519.encodeint(int))

def decodeHexPoint(point):
    return ed25519.decodepoint(unhexlify(point))

def encodePointToHex(point):
    return hexlify(ed25519.encodepoint(point))
