remove_str = input()
text = input()

while remove_str in text:
    text = text.replace(remove_str, "")

print(text)