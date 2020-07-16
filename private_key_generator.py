from bitcoin import *
import json


def btc_priv_key_generator(myVariable):
    priv = sha256(myVariable)
    privwif = encode_privkey(priv, 'wif')
    privpub = privtopub(priv)
    addr = pubtoaddr(privpub)
    print(f'private key: {privwif}')
    print(f'public key: {addr}')
    keys = {'private key': f'{privwif}', 'public key': f'{addr}'}
    json_keys = json.dumps(keys)
    return json_keys

if __name__ == "__main__":
    mnemonic_key = input("Enter passphrase:")
    btc_priv_key_generator(f"{mnemonic_key}")