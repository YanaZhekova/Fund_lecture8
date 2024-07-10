text = input().split(" ")
total_sum = 0
first_word = text[0]
second_word = text[1]

if len(first_word) >= len(second_word):
    for i in range(len(first_word)):
        if i <= len(second_word) - 1:
            for a in range(len(second_word)):
                if a == i:
                    total_sum += ord(first_word[i]) * ord(second_word[i])
                    break
        else:
            total_sum += ord(first_word[i])

else:
    for i in range(len(second_word)):
        if i <= len(first_word) - 1:
            for a in range(len(first_word)):
                if a == i:
                    total_sum += ord(first_word[i]) * ord(second_word[i])
                    break
        else:
            total_sum += ord(second_word[i])

print(total_sum)
