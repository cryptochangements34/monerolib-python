from . import crypto
from . import conversions as conv
import os
from binascii import hexlify, unhexlify

def derive_public_key(derivation, index, base):
    scalar = crypto.derivation_to_scalar(derivation, index)
    point = crypto.ge_scalarmult_base(scalar)
    res = crypto.ge_add(point, base)
    return res


def generate_rand_output(pub_key, sec_key, index):
    tx_sec_key = hexlify(os.urandom(32))
    tx_pub_key = crypto.ge_scalarmult_base(tx_sec_key)

    shared_sec = crypto.generate_key_derivation(tx_pub_key, sec_key)
    return derive_public_key(shared_sec, index, pub_key), tx_pub_key
    
