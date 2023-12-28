def unpack_nested_list(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(unpack_nested_list(element))
        else:
            result.append(element)
    return result
