flag = b"vuctf{t0_byt3_th3_h4nd_th4t_f33ds}"


def dec2rn(val: int):
    if 0 < val < 255:
        tens_vals = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L",
                    6: "LX", 7: "LXX", 8: "LXXX", 9: "XC", 0: ""}
        ones_vals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
                    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 0: ""}
        result = ""
        result += (val // 100) * "C"
        result += tens_vals[(val % 100) // 10]
        result += ones_vals[((val % 100) % 10) // 1]
        return result

encoded = ""

for char in flag:
    encoded += dec2rn(char) + " "

print(encoded.strip())