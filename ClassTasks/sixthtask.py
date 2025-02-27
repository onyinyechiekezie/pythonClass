def get_number_of_occurrences(string, character):
    my_tuple = ()
    count = 0
    for char in string:
        if char == character:
            count += 1
    my_tuple = (character, count)
    return my_tuple

