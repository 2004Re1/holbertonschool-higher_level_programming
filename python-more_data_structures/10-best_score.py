#!/usr/bin/python3

def best_score(a_dictionary):
    # Initialize variables to keep track of the best score and corresponding key
    best_key = None
    best_score = float('-inf')  # Initialize with negative infinity to handle negative scores
    
    # Iterate over the dictionary to find the key with the highest score
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key
    
    return best_key
