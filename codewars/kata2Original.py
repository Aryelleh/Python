# displays the amount of characters that are repeated in a string
def duplicate_count(passed_string):
    if not passed_string or not any(char.isalnum() for char in passed_string):
        # returns 0 if string is empty
        return 0                      
    
    char_count = {}
    for char in passed_string.lower():
        if not char.isalnum():
            # returns 0 for every non-alphanumeric character
            return 0                  
             
        if char in char_count:
            char_count[char] += 1
        else:
            # everytime a character from the char_count dictionary appears in a string, increase count by one
            char_count[char] = 1   

    duplicate_count = {}
    for char, count in char_count.items():
        if count != 1:
            # if any characters in the string have a count greater than 1, display count
            duplicate_count[char] = count

    # returns the amount of characters that repeat
    return len(duplicate_count) 

test1_string = "Excellent"
test2_string = "Pokemon"

print("Characters that repeat:", duplicate_count(test1_string))
print("Characters that repeat:", duplicate_count(test2_string))
print(duplicate_count(" "))