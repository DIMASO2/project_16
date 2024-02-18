import json

numbers = {
    1: 5,
    2: 8,
    3: 3,
    4: 6,
    5: 0
}

result = json.dumps(numbers)
print(type(result))
print(result)