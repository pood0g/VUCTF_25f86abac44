from os import urandom
from flag import flag as m

m = int.from_bytes(m.encode(), "little")
c = int.from_bytes(urandom(3), "little")

E = m * c ** 2

print("m =", m)
print("c =", c)

print(f"{E:x}")