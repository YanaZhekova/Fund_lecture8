text = input().split(":")
emoticon = ":"
counter = 0
if len(text) == 1:
    emoticon += text[1][0]
    print(emoticon)
else:
    for i in range(1, len(text)):
        emoticon += text[i][0]
        print(emoticon)
        emoticon = ":"
