def letter_combinations(digits):
    # Check if the input string is empty.
    if digits == "":
        return []
    
    # Define a mapping of digits to corresponding letters.
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    
    # Initialize the result list with an empty string.
    result = [""]
    
    # Iterate through each digit in the input string.
    for num in digits:
        # Create a temporary list to store new combinations.
        temp = []
        
        # Iterate through each existing combination in the result list.
        for an in result:
            # Append each letter corresponding to the current digit to create new combinations.
            for char in string_maps[num]:
                temp.append(an + char)
        
        # Update the result list with the new combinations.
        result = temp
    
    # Return the final list of letter combinations.
    return result

# Define input digit strings and print the corresponding letter combinations.
digit_string = "47"
print(letter_combinations(digit_string));l