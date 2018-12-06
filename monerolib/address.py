from . import base58
from . import crypto
from binascii import hexlify, unhexlify

def encode_address(net_byte, public_spend_key, public_view_key):
    checksum =  crypto.keccak_256(net_byte + public_spend_key + public_view_key)
    return base58.encode(net_byte + public_spend_key + public_view_key + checksum[0:8])

def decode_address(address):
    data = base58.decode(address)
    net_byte = data[0:2]
    public_spend_key = data[2:66]
    public_view_key = data[66:130]
    return net_byte, public_spend_key, public_view_key
