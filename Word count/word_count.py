
text = input("Enter the text you intend to count here: ")
count = 0

for word in text.split():
    count += 1

print(count)
