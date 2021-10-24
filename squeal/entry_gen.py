import random
from hashlib import sha256
from app.db import Database

db_conn = Database("app/db/users.db")

first_names = open("/usr/share/wordlists/misc/given-names.txt", "rt").read().split()
last_names = open("/usr/share/wordlists/misc/common-surnames.txt", "rt").read().split()
passwords = open("/usr/share/wordlists/rockyou.txt", "rb").read().split()

for entry in range(50):
    f_name = first_names[random.randint(0, len(first_names))].capitalize()
    l_name = last_names[random.randint(0, len(last_names))].capitalize()
    username = f_name[0].lower() + l_name.lower()
    email = username + "@diceycyber.com"
    password = sha256(passwords[random.randint(0, len(passwords))]).hexdigest()

    db_conn.add_user(f_name,l_name,email,"staff",username,password)
