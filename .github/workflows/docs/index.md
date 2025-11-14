# Project Documentation

## Usage

The functions in this project are utility helpers designed for cleaning and sanitizing text input.

### Example Usage

```python
from helpers import clean_string, remove_special_characters

# Remove spaces and convert to lowercase
print(clean_string(" Hello World "))  
# Output: helloworld

# Remove special characters
print(remove_special_characters("he!!o@#"))   
# Output: heo
