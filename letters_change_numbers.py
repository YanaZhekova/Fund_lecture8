text = input().split()
sum_word = 0
total_sum = 0
letter_before = ""
letter_after = ""
digit = ""
for word in text:
    for i in range(0, len(word)):
        if i == 0:
            letter_before = word[i]
        elif i == len(word) - 1:
            letter_after = word[i]

        if word[i].isdigit():
            digit += word[i]
    if letter_before.isupper():
        sum_word += int(digit) / (ord(letter_before) - 64)
    else:
        sum_word += int(digit) * (ord(letter_before) - 96)

    if letter_after.isupper():
        sum_word -= (ord(letter_after) - 64)
    else:
        sum_word += (ord(letter_after) - 96)

    total_sum += sum_word
    sum_word = 0
    digit = ""
print(f"{total_sum:.2f}")
