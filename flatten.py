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
