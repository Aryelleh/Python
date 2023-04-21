def ft_isdigit(stringToBeTested):

    numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(0, len(stringToBeTested)):
        if (stringToBeTested[i] in numberList):
            pass
        else:
            return(False)
        if ((i + 1 ==len(stringToBeTested))):
            return(True)


string1 = "12345673185472"

a = ft_isdigit(string1)

print(a)