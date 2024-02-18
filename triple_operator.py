import random

auto = ["audi", "BMW", "lada"]
her = random.choice(auto)

print(her)
print("NET") if (her == "audi" or her == "BMW") else print("da")