from . import crypto
from binascii import hexlify, unhexlify

multisig_salt = "4d756c7469736967000000000000000000000000000000000000000000000000"

def get_multisig_blinded_secret_key(secret_key):
    data = secret_key + multisig_salt
    return crypto.hash_to_scalar(data)

def get_multisig_signer_public_key(spend_skey):
    blinded_secret = get_multisig_blinded_secret_key(spend_skey)
    pkey = crypto.ge_scalarmult_base(blinded_secret)
    return pkey
