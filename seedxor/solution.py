from seeded_otp_xor import SeedPad

tries = 0

with open("/usr/share/wordlists/rockyou.txt", "rb") as words:
    crypter = SeedPad()
    crypter.cipher_text = "1af4ba843c90331be5e42d81691feb33a3a2c1b997d11eff90adcadb843c97f4cd"

    for word in words:
        word = word.strip()
        print(f"\rTries = {tries}", end="")
        tries += 1
        crypter.seed_key = word
        plain = crypter.decrypt()
        if "vuctf{" in plain:
            print("\n\n" + plain)
            break

