f = open("demo.text", "a+")

f.write("i want to learn javascript tomorrow.123")

f.seek(0)          # Move pointer back to beginning

data = f.read()
print(data)

f.close()