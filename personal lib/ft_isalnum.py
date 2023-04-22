def ft_isalnum(stringToBeChecked):

     alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

     numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
     
     for i in range(0, len(stringToBeChecked)):
        if (stringToBeChecked[i] in alphaList + numberList):
            pass
        else:
            return(False)
        if ((i + 1 ==len(stringToBeChecked))):
            return(True)

string1 = "Piplup2"

i = ft_isalnum(string1)

print(i)