#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase character to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            # Add other characters to the result string as they are
            result += char
    
    print(result)

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
