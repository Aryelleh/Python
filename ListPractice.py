def first_last_same(numberlist):
    print("Given list", numberlist)

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

number_x = [10 , 20 , 45 , 30 , 10]
print("Result is", first_last_same(number_x))

print("Divisible by 5:")

for num in number_x:
    if num % 5 == 0:
        print(num)

