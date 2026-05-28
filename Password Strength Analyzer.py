import re
import random
import string

common_passwords = ["123456", "password", "admin", "qwerty"]

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[!@#$%^&*]", password):
    score += 1

if password in common_passwords:
    print("Common password detected")
    score -= 1

if score <= 2:
    print("Weak Password")

elif score <= 4:
    print("Medium Password")

else:
    print("Strong Password")

chars = string.ascii_letters + string.digits + "!@#$%^&*"

suggestion = ''.join(random.choice(chars) for i in range(14))

print("Suggested Strong Password:", suggestion)