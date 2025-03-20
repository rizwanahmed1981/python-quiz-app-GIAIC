dictioneries = [
    {
        "question": "How do you create an empty dictionary?",
        "options": ["dict = {}", "dict = []", "dict = ()", "dict = ''"],
        "answer": "dict = {}"
    },
    {
        "question": "Which of the following is a correct way to define a dictionary?",
        "options": ["{'name': 'John', 'age': 25}", "['name', 'John', 'age', 25]", "{('name', 'John'), ('age', 25)}", "dict('name': 'John', 'age': 25)"],
        "answer": "{'name': 'John', 'age': 25}"
    },
    {
        "question": "What is the output of `len({'a': 1, 'b': 2})`?",
        "options": ["1", "2", "3", "Error"],
        "answer": "2"
    },
    {
        "question": "Which method is used to get the value of a key safely?",
        "options": ["get()", "find()", "lookup()", "fetch()"],
        "answer": "get()"
    },
    {
        "question": "What happens when you try to access a key that does not exist in a dictionary?",
        "options": ["Returns None", "Throws KeyError", "Returns 0", "Adds the key with None value"],
        "answer": "Throws KeyError"
    },
    {
        "question": "How do you add a new key-value pair to a dictionary?",
        "options": ["dict['new_key'] = value", "dict.add('new_key', value)", "dict.append('new_key', value)", "dict.insert('new_key', value)"],
        "answer": "dict['new_key'] = value"
    },
    {
        "question": "How do you remove a key-value pair from a dictionary?",
        "options": ["del dict[key]", "dict.pop(key)", "dict.remove(key)", "Both A and B"],
        "answer": "Both A and B"
    },
    {
        "question": "Which method removes a key and returns its value?",
        "options": ["pop()", "delete()", "remove()", "discard()"],
        "answer": "pop()"
    },
    {
        "question": "Which method returns all keys in a dictionary?",
        "options": ["keys()", "values()", "items()", "getkeys()"],
        "answer": "keys()"
    },
    {
        "question": "Which method returns all values in a dictionary?",
        "options": ["keys()", "values()", "items()", "getvalues()"],
        "answer": "values()"
    },
    {
        "question": "Which method returns all key-value pairs as tuples?",
        "options": ["keys()", "values()", "items()", "pairs()"],
        "answer": "items()"
    },
    {
        "question": "What does `dict.update({'a': 3, 'b': 4})` do?",
        "options": ["Replaces existing keys and adds new ones", "Clears the dictionary", "Removes keys", "Throws an error"],
        "answer": "Replaces existing keys and adds new ones"
    },
    {
        "question": "How do you check if a key exists in a dictionary?",
        "options": ["key in dict", "dict.contains(key)", "dict.has_key(key)", "exists(key, dict)"],
        "answer": "key in dict"
    },
    {
        "question": "Which method removes all items from a dictionary?",
        "options": ["clear()", "delete()", "removeAll()", "reset()"],
        "answer": "clear()"
    },
    {
        "question": "What is the output of `dict.get('missing_key', 'default')` if the key does not exist?",
        "options": ["None", "default", "Error", "0"],
        "answer": "default"
    },
    {
        "question": "Can dictionary keys be mutable?",
        "options": ["No", "Yes", "Only strings", "Only numbers"],
        "answer": "No"
    },
    {
        "question": "Which data type cannot be used as a dictionary key?",
        "options": ["List", "String", "Tuple", "Integer"],
        "answer": "List"
    },
    {
        "question": "Can a dictionary contain another dictionary?",
        "options": ["Yes", "No", "Only in Python 3", "Only if empty"],
        "answer": "Yes"
    },
    {
        "question": "How do you loop through dictionary keys?",
        "options": ["for key in dict", "for key in dict.keys()", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "How do you loop through dictionary values?",
        "options": ["for value in dict.values()", "for value in dict", "for value in dict.getValues()", "for value in dict.values"],
        "answer": "for value in dict.values()"
    },
    {
        "question": "What does `dict.popitem()` do?",
        "options": ["Removes a random key-value pair", "Removes the first key-value pair", "Removes the last key-value pair", "Removes a specific key"],
        "answer": "Removes a random key-value pair"
    },
    {
        "question": "How do you merge two dictionaries in Python 3.9+?",
        "options": ["dict1 | dict2", "dict1 + dict2", "dict1.merge(dict2)", "dict1.append(dict2)"],
        "answer": "dict1 | dict2"
    },
    {
        "question": "How do you create a dictionary with default values?",
        "options": ["dict.fromkeys(keys, default_value)", "dict.create(keys, default_value)", "dict.default(keys, default_value)", "dict(keys, default_value)"],
        "answer": "dict.fromkeys(keys, default_value)"
    },
    {
        "question": "What is the result of `len({})`?",
        "options": ["0", "1", "None", "Error"],
        "answer": "0"
    },
    {
        "question": "How do you convert a list of tuples into a dictionary?",
        "options": ["dict(list_of_tuples)", "list_of_tuples.to_dict()", "convert(list_of_tuples)", "map(dict, list_of_tuples)"],
        "answer": "dict(list_of_tuples)"
    },
    {
        "question": "Which function returns a shallow copy of a dictionary?",
        "options": ["copy()", "clone()", "duplicate()", "deepcopy()"],
        "answer": "copy()"
    },
    {
        "question": "Which method returns the value for a given key, or a default value if the key is not found?",
        "options": ["get()", "find()", "lookup()", "search()"],
        "answer": "get()"
    },
    {
        "question": "How do you check the type of a dictionary?",
        "options": ["type(dict)", "dict.type()", "typeof(dict)", "checktype(dict)"],
        "answer": "type(dict)"
    },
    {
        "question": "Which method is used to create a dictionary from two lists?",
        "options": ["zip()", "dict()", "combine()", "merge()"],
        "answer": "zip()"
    },
    {
        "question": "What is the default return value of `dict.get(key)` if the key is missing?",
        "options": ["None", "Error", "0", "''"],
        "answer": "None"
    },
    {
        "question": "How do you access a nested dictionary value?",
        "options": ["dict['key']['subkey']", "dict.get('key')['subkey']", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "Which method is used to set a key only if it does not exist?",
        "options": ["setdefault()", "insert()", "assign()", "create()"],
        "answer": "setdefault()"
    }
]