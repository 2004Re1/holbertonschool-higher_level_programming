#!/usr/bin/python3

def roman_to_int(roman_string):
    sum = 0
    a_dic = {'X': 10, 'V': 5, 'I': 1, 'C': 100, 'D': 500, 'M': 1000}
    
    # Iterate over each character in the roman_string
    for i in range(len(roman_string)):
        # Get the current character
        current_char = roman_string[i]
        
        # Check if the next character is greater than the current one
        if i < len(roman_string) - 1 and a_dic[roman_string[i + 1]] > a_dic[current_char]:
            # If it is, subtract the value of the current character
            sum -= a_dic[current_char]
        else:
            # Otherwise, add the value of the current character
            sum += a_dic[current_char]
    
    return sum
