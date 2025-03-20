tuples = [
    {
        "question": "How do you create an empty tuple?",
        "options": ["tuple = {}", "tuple = []", "tuple = ()", "tuple = ''"],
        "answer": "tuple = ()"
    },
    {
        "question": "Which of the following is a correct way to define a tuple?",
        "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "tuple(1, 2, 3)"],
        "answer": "(1, 2, 3)"
    },
    {
        "question": "Can a tuple be modified after creation?",
        "options": ["Yes", "No", "Only if it contains mutable elements", "Only in Python 3"],
        "answer": "No"
    },
    {
        "question": "What happens when you try to change an element of a tuple?",
        "options": ["It changes", "Creates a new tuple", "Throws TypeError", "Deletes the tuple"],
        "answer": "Throws TypeError"
    },
    {
        "question": "How do you access the second element of a tuple?",
        "options": ["tuple[1]", "tuple(1)", "tuple.get(1)", "tuple[2]"],
        "answer": "tuple[1]"
    },
    {
        "question": "Which method is used to find the length of a tuple?",
        "options": ["size()", "len()", "count()", "length()"],
        "answer": "len()"
    },
    {
        "question": "What is the output of `len((5,))`?",
        "options": ["0", "1", "5", "Error"],
        "answer": "1"
    },
    {
        "question": "Which of the following creates a tuple with a single element?",
        "options": ["(5,)", "(5)", "[5]", "{5}"],
        "answer": "(5,)"
    },
    {
        "question": "How do you concatenate two tuples?",
        "options": ["tuple1 + tuple2", "tuple1.append(tuple2)", "tuple1.extend(tuple2)", "tuple1 * tuple2"],
        "answer": "tuple1 + tuple2"
    },
    {
        "question": "How do you repeat elements of a tuple?",
        "options": ["tuple * n", "tuple.repeat(n)", "tuple + tuple", "tuple.extend(n)"],
        "answer": "tuple * n"
    },
    {
        "question": "How do you check if an item exists in a tuple?",
        "options": ["in", "contains()", "exists()", "find()"],
        "answer": "in"
    },
    {
        "question": "Which method counts occurrences of an element in a tuple?",
        "options": ["count()", "index()", "find()", "size()"],
        "answer": "count()"
    },
    {
        "question": "Which method finds the index of an element in a tuple?",
        "options": ["index()", "find()", "position()", "search()"],
        "answer": "index()"
    },
    {
        "question": "How do you convert a list into a tuple?",
        "options": ["tuple(list)", "list(tuple)", "to_tuple(list)", "convert(list)"],
        "answer": "tuple(list)"
    },
    {
        "question": "What is the output of `tuple(range(3))`?",
        "options": ["(1, 2, 3)", "(0, 1, 2)", "(0, 1, 2, 3)", "Error"],
        "answer": "(0, 1, 2)"
    },
    {
        "question": "How can you unpack a tuple into variables?",
        "options": ["a, b = (1, 2)", "a, b = [1, 2]", "a = (1, 2)", "a = [1, 2]"],
        "answer": "a, b = (1, 2)"
    },
    {
        "question": "What is the output of `('a', 'b') + ('c',)`?",
        "options": ["('a', 'b', 'c')", "('a', 'b')", "('a', 'b', 'c', 'd')", "Error"],
        "answer": "('a', 'b', 'c')"
    },
    {
        "question": "What is the output of `tuple('abc')`?",
        "options": ["('a', 'b', 'c')", "['a', 'b', 'c']", "Error", "('abc')"],
        "answer": "('a', 'b', 'c')"
    },
    {
        "question": "How do you delete a tuple?",
        "options": ["del tuple", "tuple.remove()", "tuple.delete()", "tuple.pop()"],
        "answer": "del tuple"
    },
    {
        "question": "Can a tuple contain lists?",
        "options": ["Yes", "No", "Only in Python 3", "Only if lists are empty"],
        "answer": "Yes"
    },
    {
        "question": "How do you check the type of a tuple?",
        "options": ["type(tuple)", "tuple.type()", "tuple.getType()", "typeof(tuple)"],
        "answer": "type(tuple)"
    },
    {
        "question": "How do you slice a tuple?",
        "options": ["tuple[start:end]", "slice(tuple)", "tuple.slice()", "tuple.split()"],
        "answer": "tuple[start:end]"
    },
    {
        "question": "Which operator is used to merge tuples?",
        "options": ["+", "*", "-", "/"],
        "answer": "+"
    },
    {
        "question": "What happens if you multiply a tuple by 0?",
        "options": ["Creates an empty tuple", "Throws an error", "Returns None", "Duplicates the tuple"],
        "answer": "Creates an empty tuple"
    },
    {
        "question": "Which function finds the maximum element in a tuple?",
        "options": ["max()", "top()", "largest()", "highest()"],
        "answer": "max()"
    },
    {
        "question": "Which function finds the minimum element in a tuple?",
        "options": ["min()", "low()", "smallest()", "bottom()"],
        "answer": "min()"
    },
    {
        "question": "What is the output of `(3,) + (4, 5)`?",
        "options": ["(3, 4, 5)", "(3, 9)", "(4, 5)", "(3, [4, 5])"],
        "answer": "(3, 4, 5)"
    },
    {
        "question": "How do you sort a tuple?",
        "options": ["sorted(tuple)", "tuple.sort()", "sort(tuple)", "sorted_list(tuple)"],
        "answer": "sorted(tuple)"
    },
    {
        "question": "What is the output of `len(())`?",
        "options": ["0", "1", "None", "Error"],
        "answer": "0"
    },
    {
        "question": "What is the difference between a list and a tuple?",
        "options": ["Tuples are immutable, lists are mutable", "Lists are immutable, tuples are mutable", "Both are mutable", "Both are immutable"],
        "answer": "Tuples are immutable, lists are mutable"
    },
    {
        "question": "How do you convert a tuple into a list?",
        "options": ["list(tuple)", "tuple.list()", "convert(tuple)", "to_list(tuple)"],
        "answer": "list(tuple)"
    },
    {
        "question": "Can a tuple contain duplicate elements?",
        "options": ["Yes", "No", "Only numbers", "Only strings"],
        "answer": "Yes"
    }
]