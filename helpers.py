def remove_special_characters(s):
    import re
    return re.sub(r'[^A-Za-z0-9]', '', s)
