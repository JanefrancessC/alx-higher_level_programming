#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best_val = list(a_dictionary.keys())[0]
    big_val = a_dictionary[best_val]
    for k, v in a_dictionary.items():
        if v > big_val:
            big_val = v
            best_val = k
    return (best_val)
