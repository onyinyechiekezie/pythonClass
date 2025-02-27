def get_string_and_ce(string):
    # for char in string:
    if len(string) % 2 == 0:
        new_string = string[:len(string)//2] + "ce" + (string[len(string)//2:])
        return new_string
    else:
        new_string = string + "ce"
        return new_string


