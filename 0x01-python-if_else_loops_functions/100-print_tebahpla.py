for i in range(ord('z'), ord('A') - 1, -1):
    if i % 2 == 0:
        print(chr(i), end='')
    else:
        print(chr(i - 32), end='')
