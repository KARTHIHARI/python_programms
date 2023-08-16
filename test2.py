a = 8

bit = 8

a = bin(a)[2:].rjust(bit,'0')

print(a[:4],a[4:])