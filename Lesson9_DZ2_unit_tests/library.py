
def filter_cut_string(input_string: str) -> str:
    '''Converts a string to lower case and trims it'''
    clean_string = ''
    for item in input_string:
        if item.isupper():
            clean_string += item

    cut_string = clean_string[:25]

    return cut_string
