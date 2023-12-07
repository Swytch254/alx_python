def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        sorted_values = a_dictionary.values()
        return (sorted(sorted_values, reverse=True))[0]
    else:
        return None
    