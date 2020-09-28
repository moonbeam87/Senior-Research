import sys
from BitVector import *
AES_modulus = BitVector(bitstring="100011011")
subBytesTable = [] # SBox for encryption
invSubBytesTable = [] # SBox for decryption

#Bit Vector converts an integer into a binary representation in the form of a list or a tuple
def genTables():
    c = BitVector(bitstring="01100011")
    d = BitVector(bitstring="00000101")
    for i in range(0, 256):
        # For the encryption SBox
        a = BitVector(intVal = i, size=8).gf_MI(AES_modulus, 8) if i != 0 else BitVector(intVal=0)
        #.gf_MI does the multiplicative inverse of a BitVector with another BitVector in the Galois Field (2^n) (Vector, n)
        # For bit scrambling for the encryption SBox entries:
        a1,a2,a3,a4 = [a.deep_copy() for x in range(4)]
        #generates 4 copies of the BitVector
        a ^= (a1 >> 4) ^ (a2 >> 5) ^ (a3 >> 6) ^ (a4 >> 7) ^ c
        #>> operator represents bitwise right shift. Shigts a1 right 4 bits, raises it to a2 shifted right 5 ... etc.

        subBytesTable.append(int(a))
        # For the decryption Sbox:
        b = BitVector(intVal = i, size=8)
        # For bit scrambling for the decryption SBox entries:
        b1,b2,b3 = [b.deep_copy() for x in range(3)]
        b = (b1 >> 2) ^ (b2 >> 5) ^ (b3 >> 7) ^ d
        check = b.gf_MI(AES_modulus, 8)
        b = check if isinstance(check, BitVector) else 0
        invSubBytesTable.append(int(b))
genTables()
print("SBox for Encryption:")
print(subBytesTable)
print("\nSBox for Decryption")