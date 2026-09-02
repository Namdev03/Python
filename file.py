f = open("demo.text","r")
data = f.read()
print(data)
print(type(data))
line1 = f.readline()
print("reading the line hear",)

f.close()