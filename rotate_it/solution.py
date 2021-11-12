def main():
    plain = input().encode().split()
    ciph = ""
    for i in plain[0]:
        new = i + int(plain[1])
        if new > 122:
            new -= 26
        ciph += chr(new)
    return ciph

print(main())