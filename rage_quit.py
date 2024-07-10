word = input()
output = ""
text = ""
digit = ""
unique_letters = 0
for ch in word:
    if not ch.isdigit():
        if ch.upper() not in output:
            unique_letters += 1
        text += ch.upper()
    else:
        digit += ch
        index = word.index(ch)
        if index + 1 < len(word) - 1:
            if not word[index + 1].isdigit():
                output += int(digit) * text
                text = ""
                digit = ""
        else:
            output += int(digit) * text

print(f"Unique symbols used: {unique_letters}")
print(output)
