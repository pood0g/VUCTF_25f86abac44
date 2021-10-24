from math import isqrt

try:
    ct = int(input("Enter E: "), 16)
except ValueError:
    print("You must enter a hexadecimal string.")
    exit()

for i in range(1, 256 ** 3):
    try:
        pt = (ct // (i ** 2)).to_bytes(32, "little").decode()
        if "vuctf{" in pt:
            print(pt)
            break
    except UnicodeDecodeError:
        pass
