from . import base58
from . import crypto
from . import varint
from . import stealth_address
from binascii import hexlify, unhexlify

# descr: generates a version 1 coinbase tx with one output and unlock height 60
# params:
# view_key: public viewkey of recipient
# spend_key: public spendkey of recipient

def generate_genesis_tx(view_key, spend_key, amount):
    version = "01"
    unlock_height = "3c"
    vin_count = "01"
    coinbase_vin = "ff"
    gen_height = "00"
    vout_count = "01"
    out_amount = varint.encodeVarInt(amount)
    out_type = "02"
    key_data = stealth_address.generate_rand_output(spend_key, view_key, "00")
    vout_key = key_data[0]
    extra = "2101" + key_data[1] + "00"
    return version + unlock_height + vin_count + coinbase_vin + gen_height + vout_count + out_amount + out_type + vout_key + extra
