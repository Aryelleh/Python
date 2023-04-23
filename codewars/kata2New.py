# displays the amount of characters that are repeated in a string
def duplicate_count(passed_string):
    # returns 0 if string is empty
    if not passed_string or not any(char.isalnum() for char in passed_string):
        return 0                      
    
    # returns 0 for every non-alphanumeric character
    char_count = {}
    for char in passed_string.lower():
        if not char.isalnum():
            return 0                  
        
        # everytime a character from the char_count dictionary appears in a string, increase count by one     
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1   

    # remove all 0's and subtract each count by 1
    for key in char_count:
        char_count[key] -= 1
    
    char_count = {key: value for key, value in char_count.items() if value > 0}

    #returns the amount of characters that repeat
    return len(char_count) 

print("Characters that repeat:", duplicate_count("Excellent"))
print("Characters that repeat:", duplicate_count("Pokemon"))
print(duplicate_count(" "))