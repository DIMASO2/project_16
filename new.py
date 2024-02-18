import random
import string

unga = []
for i in range(10):
    unga.append(random.choice(string.ascii_letters).lower())

print(unga)

print("da") if ("d" in unga and "a" in unga) else print("no")