with open("example.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")

print(new_data)

with open("example.txt", "w") as f:
    f.write(new_data)