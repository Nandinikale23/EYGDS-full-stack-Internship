import random
import string

print("Password Generation")
n = int(input("Enter length of password: "))

c = string.ascii_letters + string.digits + string.punctuation
p = "".join(random.choice(c) for i in range(n))

print("Your password:", p)
