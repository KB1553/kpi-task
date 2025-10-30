def dec_to_bin(n):
    return bin(n)[2:]

def bin_to_dec(b):
    return int(b, 2)

print(dec_to_bin(13))  
print(bin_to_dec("1101"))