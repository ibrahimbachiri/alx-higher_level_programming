#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase character to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            # Add other characters to the result string as they are
            result += char
    
    return result

# Test cases
if __name__ == "__main__":
    print("{}".format(uppercase("holberton")))
    print("{}".format(uppercase("Holberton School")))
    print("{}".format(uppercase("Holberton School, 98 battery street")))
    print("{}".format(uppercase("")))
    print("{}".format(uppercase("98")))
    print("{}".format(uppercase("z")))
