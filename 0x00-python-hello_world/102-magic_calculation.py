import dis

def magic_calculation(a, b):
    result = 98
    result += a ** b
    return result

# Display the bytecode of the magic_calculation function
dis.dis(magic_calculation)
