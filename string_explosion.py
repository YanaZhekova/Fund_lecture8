text = input()
output = text
for i in range(0, len(text)):
    if text[i].isdigit():
        strength = int(text[i])

