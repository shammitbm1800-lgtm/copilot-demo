# Function: clean a string by removing spaces and converting to lowercase
def clean_string(input_string):
    cleaned = input_string.replace(" ", "").lower()
    return cleaned
    
    # Helper: create a function to remove special characters
    def remove_special_characters(s):
        import re
        return re.sub(r'[^a-zA-Z0-9]', '', s)      