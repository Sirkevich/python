data = [12, 3, 4, 10]

if len(data) > 1:
    data.insert(0, data.pop())

print(data)