def deep_flatten_list(nested_lst):
    flattened = []
    for item in nested_lst:
        if isinstance(item, type([])):
            flattened.extend(deep_flatten_list(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

flattened_list = deep_flatten_list(nested_list)
print(flattened_list)



def reverse_nested_list(nested_lst):
    reversed_list = []
    for item in reversed(nested_lst):
        if isinstance(item, type([])):
            reversed_list.append(reverse_nested_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

nested_list = [[1, 2], [3, 4], [5, 6, 7]]
reversed_list = reverse_nested_list(nested_list)
print(reversed_list)
