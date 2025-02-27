def remove_special_characters(string):
    letters = ""
    for char in string:
        if char.isalnum():
            letters += char
    return letters
