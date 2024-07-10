text = input()
output = text[0]
for ch in text:
    if ch != output[len(output)-1]:
        output += ch

print(output)
