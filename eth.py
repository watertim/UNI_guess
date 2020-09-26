from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

#derive address from 64 words private key string
def priv_to_addr(hex_priv: str):
    try:
        if len(hex_priv) != 64:
            raise Exception("length err")
        else:
            return "0x"+keccak_256(PublicKey.from_valid_secret(bytes.fromhex(hex_priv)).format(compressed=False)[1:]).digest()[-20:].hex()
    except:
        return "0x"+"0"*40

if __name__ == "__main__":
    print("testing")

    hexpriv = "0000000000000000000000000000000000000000000000000000000000000001"

    #private_key = keccak_256(token_bytes(32)).digest()
    #private_key = hexpriv
    #public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    #addr = keccak_256(public_key).digest()[-20:]

    print('private_key:', hexpriv)
    print('eth addr: ' + priv_to_addr(hexpriv))
