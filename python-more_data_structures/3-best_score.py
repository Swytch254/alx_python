def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        sorted_values = a_dictionary.values()
        for key,value in a_dictionary.items():
            if (sorted(sorted_values, reverse=True))[0] == value:
                return key
    else:
        return None
