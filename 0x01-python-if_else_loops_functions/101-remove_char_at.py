#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    return str[:n] + str[n+1:]

# Test the remove_char_at function
if __name__ == "__main__":
    print(remove_char_at("Chicago", 3))  # Correct output - case: remove_char_at("Chicago", 3)
    print(remove_char_at("Chicago", 15))  # Correct output - case: remove_char_at("Chicago", 15)
    print(remove_char_at("", 4))  # Correct output - case: remove_char_at("", 4)
    print(remove_char_at("Chicago", -3))  # Correct output - case: remove_char_at("Chicago", -3)
    print(remove_char_at("Chicago", 0))  # Correct output - case: remove_char_at("Chicago", 0)
