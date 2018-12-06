import struct
from . import crypto
from . import address
from . import conversions as conv
from binascii import hexlify, unhexlify


def generate_subaddr_secret_key(major_index, minor_index, sec_key):
    prefix = "SubAddr\0"
    index = struct.pack("II", major_index, minor_index)
    return crypto.hash_to_scalar(hexlify(prefix) + sec_key + hexlify(index))
    
def generate_subaddress_spend_public_key(spend_public_key, subaddr_secret_key):
	mG = crypto.ge_scalarmult_base(subaddr_secret_key)
	D = crypto.ge_add(spend_public_key, mG)
	return D

def generate_subaddr_view_public_key(subaddr_spend_public_key, view_secret_key):
	return crypto.ge_scalarmult(subaddr_spend_public_key, view_secret_key)
	
def generate_subaddress(major_index, minor_index, view_secret_key, spend_public_key):
    subaddr_secret_key = generate_subaddr_secret_key(major_index, minor_index, view_secret_key)
    subaddr_public_spend_key = generate_subaddress_spend_public_key(spend_public_key, subaddr_secret_key)
    subaddr_public_view_key = generate_subaddr_view_public_key(subaddr_spend_public_key, view_secret_key)
    return address.encode_address("12", subaddr_public_spend_key, subaddr_public_view_key)
    
