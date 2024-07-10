text = input()
output = ""
for ch in text:
    if ch.isdigit():
        strength = int(ch)
        output += slice(text[0], ch)
