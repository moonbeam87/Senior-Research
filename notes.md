#Step By Step AES-128
 - Add Round Key
 - Substitute Bytes
 - shift rows
 - mix columns
 - Add round key

Steps 2-5 is part of "Round Function"

Represent Data in 4 by 4 Matrix

Each Cell has 1 byte (8 bit) resulting in 128 bit block

Data Block to be encrypted is 128 bit, Key is 128 bit

Round Key is generated with XOR Function

Use S-BOX to substitute data - HEX lookup key