text = input()
output = ""
while text != "end":

    output = "".join(reversed(text))
    print(f"{text} = {output}")
    text = input()
