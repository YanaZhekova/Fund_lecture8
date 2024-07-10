def valid_username(user):
    is_valid = True
    for ch in user:
        if ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_":
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


usernames = input().split(", ")

for username in usernames:

    if 3 <= len(username) <= 16:
        if valid_username(username):
            print(username)
