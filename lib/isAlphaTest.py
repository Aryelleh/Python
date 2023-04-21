def ft_isalpha(passed_string):
    for i in passed_string:
        isAlpha = ord('a') <= ord(i) <= ord('z')
        isAlphaCap = ord('A') <= ord(i) <= ord('Z')
        if not isAlpha and not isAlphaCap:
          return (False)
    return (True)

i = ft_isalpha('Piplup')

print(i)