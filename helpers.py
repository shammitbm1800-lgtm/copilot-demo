def clean_string(input_string):
    return input_string.replace(" ", "").lower()

def remove_special_characters(s):
    import re
    return re.sub(r'[^A-Za-z0-9]', '', s)
