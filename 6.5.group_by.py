def group_by(f, itr):
    # pass each item in itr to f by using a generator expression
    # then create a set() from the result in order to delete the duplicates.
    keys = set(f(item) for item in itr)
    # For each key, the following dictionary comprehension creates a list comprehension that
    # iterates over each item in itr and adds the item to the list only if f(item) == key.
    groups_dict = {key: [item for item in itr if f(item) == key] for key in keys}
    return groups_dict


print(group_by(len, ["hi", "bye", "yo", "try"]))
