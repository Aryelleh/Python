def duplicate_count(passed_string):
    if not passed_string or not any(char.isalnum() for char in passed_string):
        return 0                      
    # returns 0 if string is empty
    
    char_count = {}
    for char in passed_string.lower():
        if not char.isalnum():
            return 0                  
        # returns 0 for every non-alphanumeric character
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        # everytime a character from the char_count dictionary appears in a string, increase count by one

    duplicate_count = {}
    for char, count in char_count.items():
        if count != 1:
            duplicate_count[char] = count
    # if any characters in the string have a count greater than 1, display count

    return len(duplicate_count) # returns the amount of characters that repeat

test1_string = "Excellent"
test2_string = "Pokemon"

print("Characters that repeat:", duplicate_count(test1_string))
print("Characters that repeat:", duplicate_count(test2_string))
print(duplicate_count(" "))