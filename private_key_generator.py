from bitcoin import *


def btc_priv_key_generator(myVariable):
    priv = sha256(myVariable)
    privwif = encode_privkey(priv, 'wif')
    privpub = privtopub(priv)
    addr = pubtoaddr(privpub)
    print("private key: "f'{privwif}')
    print("public key: "f'{addr}')

if __name__ == "__main__":
    mnemonic_key = input("Enter passphrase:")
    btc_priv_key_generator(f"{mnemonic_key}")