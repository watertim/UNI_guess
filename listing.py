from eth import priv_to_addr

"""
print(priv_to_addr("0"*63+"1"))
for i in range(1,10,1):
    print(priv_to_addr(f"{i:064x}"))
"""

from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

addrf = open("dict_addr.txt", mode='a+')
privaddrf = open("dict_priv_addr.txt", mode='a+')

#randomly generate 10000 private key/address pair and save them into files
for i in range(1,10000,1):
    private_key = keccak_256(token_bytes(32)).digest().hex()
    addr_from_priv = priv_to_addr(private_key)
    addrf.write(addr_from_priv+"\n")
    privaddrf.write(private_key+" "+addr_from_priv+"\n")

addrf.close()
privaddrf.close()
