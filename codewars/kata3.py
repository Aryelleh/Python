# returns the sum of two values as a binary value
def add_binary(a, b):
    return str(bin(a + b)[2:])


print(add_binary(8, 9))