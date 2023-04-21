def ft_isalpha(passed_string):
    for i in passed_string:
        isAlpha = 97 <= ord(i) <= 122
        isAlphaCap = 65 <= ord(i) <= 90
        if not isAlpha and not isAlphaCap:
          return (False)
    return (True)

i = ft_isalpha("Piplup")

print(i)