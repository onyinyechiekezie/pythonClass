
def get_occurrence(string):
    occurrence = {}
    for char in string:
        if char in occurrence:
            occurrence[char] += 1
        else:
            occurrence[char] = 1
    return occurrence



