def ft_isascii(passed_string):
    for i in passed_string:
        isAscii = 0 <= ord(i) <= 127
        if not isAscii:
          return (False)
    return (True)

i = ft_isascii("À")

print(i)
