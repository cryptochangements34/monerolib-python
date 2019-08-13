from . import base58
from . import crypto
from . import varint
from . import stealth_address
from binascii import hexlify, unhexlify

# descr: generates a version 1 coinbase tx with one output and unlock height 60
# params:
# view_key: secret viewkey of recipient
# spend_key: public spendkey of recipient
# tx_key: public transaction key
# amount: amount in atomic units

def generate_genesis_tx(view_key, spend_key, tx_key, amount):
    version = "01"
    unlock_height = "3c"
    vin_count = "01"
    coinbase_vin = "ff"
    gen_height = "00"
    vout_count = "01"
    out_amount = varint.encodeVarInt(amount)
    out_type = "02"
    key_derivation = crypto.generate_key_derivation(tx_key, view_key)
    vout_key = stealth_address.derive_public_key(key_derivation, "00", spend_key)
    extra = "2101" + tx_key + "00"
    return version + unlock_height + vin_count + coinbase_vin + gen_height + vout_count + out_amount + out_type + vout_key + extra
