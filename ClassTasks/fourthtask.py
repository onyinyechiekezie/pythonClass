def get_mix_upper(string):
    upper = ""
    lower = ""
    for char in string:
        if char.isupper():
            upper += char
        else:
            lower += char
    return upper + lower