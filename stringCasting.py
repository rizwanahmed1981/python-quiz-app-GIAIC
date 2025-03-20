stringCasting = [
    {
        "question": "Which function is used to convert an integer to a string in Python?",
        "options": ["int()", "str()", "float()", "bool()"],
        "answer": "str()"
    },
    {
        "question": "What is the output of str(100)?",
        "options": ["100", "'100'", "100.0", "Error"],
        "answer": "'100'"
    },
    {
        "question": "Which function is used to convert a floating-point number to a string?",
        "options": ["int()", "float()", "str()", "bool()"],
        "answer": "str()"
    },
    {
        "question": "What will be the type of str(10.5)?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },
    {
        "question": "How do you convert a boolean value True to a string?",
        "options": ["str(True)", "string(True)", "toString(True)", "convert(True)"],
        "answer": "str(True)"
    },
    {
        "question": "What is the output of str(False)?",
        "options": ["0", "False", "'False'", "None"],
        "answer": "'False'"
    },
    {
        "question": "What is the result of str(None)?",
        "options": ["None", "'None'", "Error", "''"],
        "answer": "'None'"
    },
    {
        "question": "What will be the output of str(3 + 4j)?",
        "options": ["'3 + 4j'", "3 + 4j", "'3+4j'", "Error"],
        "answer": "'(3+4j)'"
    },
    {
        "question": "What happens when you call str() with no arguments?",
        "options": ["Returns an empty string", "Raises an error", "Returns None", "Returns '0'"],
        "answer": "Returns an empty string"
    },
    {
        "question": "Which function is used to convert a list to a string?",
        "options": ["str()", "list()", "join()", "cast()"],
        "answer": "str()"
    },
    {
        "question": "What will be the output of str([1, 2, 3])?",
        "options": ["'1, 2, 3'", "'[1, 2, 3]'", "[1, 2, 3]", "Error"],
        "answer": "'[1, 2, 3]'"
    },
    {
        "question": "Which function is used to concatenate an integer with a string?",
        "options": ["str()", "int()", "float()", "bool()"],
        "answer": "str()"
    },
    {
        "question": "What is the result of 'Age: ' + str(25)?",
        "options": ["Age: 25", "'Age: 25'", "Error", "'Age: ' + 25"],
        "answer": "'Age: 25'"
    },
    {
        "question": "Which method converts an object to a string representation?",
        "options": ["__repr__()", "__str__()", "str()", "repr()"],
        "answer": "__str__()"
    },
    {
        "question": "What is the output of str(0.0)?",
        "options": ["'0.0'", "0.0", "'0'", "Error"],
        "answer": "'0.0'"
    },
    {
        "question": "What happens when str() is used with a dictionary?",
        "options": ["Raises an error", "Converts to a string", "Returns a list", "Returns None"],
        "answer": "Converts to a string"
    },
    {
        "question": "Which function is used to convert an integer string back to an integer?",
        "options": ["int()", "str()", "float()", "bool()"],
        "answer": "int()"
    },
    {
        "question": "What is the output of str(0)?",
        "options": ["0", "'0'", "None", "Error"],
        "answer": "'0'"
    },
    {
        "question": "How do you convert a list of characters into a string?",
        "options": ["str(list)", "list.join()", "' '.join(list)", "join(list)"],
        "answer": "' '.join(list)"
    },
    {
        "question": "What is the result of str(10) + str(5)?",
        "options": ["15", "105", "'15'", "'105'"],
        "answer": "'105'"
    },
    {
        "question": "What is the output of str(True) + ' world'?",
        "options": ["True world", "'True world'", "Error", "None"],
        "answer": "'True world'"
    },
    {
        "question": "Which function is used to convert a tuple to a string?",
        "options": ["tuple()", "str()", "join()", "convert()"],
        "answer": "str()"
    },
    {
        "question": "What will be the type of str({1, 2, 3})?",
        "options": ["set", "str", "list", "tuple"],
        "answer": "str"
    },
    {
        "question": "What will be the output of str({'a': 1, 'b': 2})?",
        "options": ["{'a': 1, 'b': 2}", "'{'a': 1, 'b': 2}'", "Error", "None"],
        "answer": "'{'a': 1, 'b': 2}'"
    },
    {
        "question": "Which method converts an object into a printable string?",
        "options": ["repr()", "str()", "format()", "print()"],
        "answer": "repr()"
    },
    {
        "question": "What will be the output of str(3.14)?",
        "options": ["3.14", "'3.14'", "Error", "None"],
        "answer": "'3.14'"
    },
    {
        "question": "Which function is used to explicitly convert a boolean to a string?",
        "options": ["str()", "bool()", "int()", "float()"],
        "answer": "str()"
    },
    {
        "question": "What is the result of str('100')?",
        "options": ["'100'", "100", "Error", "None"],
        "answer": "'100'"
    },
    {
        "question": "What is the result of str(['apple', 'banana'])?",
        "options": ["'['apple', 'banana']'", "'apple, banana'", "Error", "None"],
        "answer": "'['apple', 'banana']'"
    },
    {
        "question": "How can you check the type of a variable after casting it to a string?",
        "options": ["type(var)", "str(type(var))", "var.str()", "isinstance(var, str)"],
        "answer": "type(var)"
    },
    {
        "question": "What will be the type of str(5 + 2.3)?",
        "options": ["int", "float", "str", "Error"],
        "answer": "str"
    },
    {
        "question": "Which function is best for converting objects into human-readable strings?",
        "options": ["str()", "repr()", "format()", "print()"],
        "answer": "str()"
    },
    {
        "question": "What is the output of str(2.5e3)?",
        "options": ["2500", "'2500'", "'2.5e3'", "Error"],
        "answer": "'2500.0'"
    },
    {
        "question": "How can you convert a set into a string?",
        "options": ["set()", "str()", "convert()", "join()"],
        "answer": "str()"
    },
    {
        "question": "What happens if you try to convert an object that doesn’t support string conversion?",
        "options": ["Raises an error", "Returns 'None'", "Returns 'Unsupported'", "Returns an empty string"],
        "answer": "Raises an error"
    }
]