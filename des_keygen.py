s = '10100111'
#64 bit key as binary bit

HexKEY = "22234512987ABB23"

def hexToBinary(Hex):
    scale = 16
    res = bin(int(Hex, 16)).zfill(8)
    n = len(res)-1
    res = res.replace('b','0')
    return res

keyBinary = hexToBinary(HexKEY)
print(keyBinary)


#What is Parity Drop?
#Parity drop reserves 1 bit in each 8 bit byte of the Key for error detection
#Bits 8, 16, 24, 32, 40, 48, 56, and 64 are used for the parity drop
keyp = [57, 49, 41, 33, 25, 17, 9,  
        1, 58, 50, 42, 34, 26, 18,  
        10, 2, 59, 51, 43, 35, 27,  
        19, 11, 3, 60, 52, 44, 36,  
        63, 55, 47, 39, 31, 23, 15,  
        7, 62, 54, 46, 38, 30, 22,  
        14, 6, 61, 53, 45, 37, 29,  
        21, 13, 5, 28, 20, 12, 4 ] 
#Standard Parity Drop Table
cipher = ""
key = "0001001100110100010101110111100110011011101111001101111111110001"
for i in keyp:
    cipher += keyBinary[i-1]

print(cipher)
