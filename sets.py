sets = [
    {
        "question": "How do you create an empty set in Python?",
        "options": ["set = {}", "set = []", "set = set()", "set = ()"],
        "answer": "set = set()"
    },
    {
        "question": "Which of the following is a valid way to create a set?",
        "options": ["{1, 2, 3}", "set([1, 2, 3])", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "What is the main characteristic of a set?",
        "options": ["Ordered and allows duplicates", "Unordered and does not allow duplicates", "Ordered and does not allow duplicates", "Unordered and allows duplicates"],
        "answer": "Unordered and does not allow duplicates"
    },
    {
        "question": "How do you add an element to a set?",
        "options": ["set.add(value)", "set.append(value)", "set.insert(value)", "set.push(value)"],
        "answer": "set.add(value)"
    },
    {
        "question": "Which method is used to remove a specific element from a set?",
        "options": ["remove()", "discard()", "Both A and B", "pop()"],
        "answer": "Both A and B"
    },
    {
        "question": "Which method removes a random element from a set?",
        "options": ["pop()", "remove()", "discard()", "delete()"],
        "answer": "pop()"
    },
    {
        "question": "What happens if you try to remove a non-existing element using `remove()`?",
        "options": ["Throws a KeyError", "Ignores the error", "Removes the first element", "Removes the last element"],
        "answer": "Throws a KeyError"
    },
    {
        "question": "What happens if you try to remove a non-existing element using `discard()`?",
        "options": ["Throws a KeyError", "Ignores the error", "Removes the first element", "Removes the last element"],
        "answer": "Ignores the error"
    },
    {
        "question": "Which method removes all elements from a set?",
        "options": ["clear()", "removeAll()", "empty()", "deleteAll()"],
        "answer": "clear()"
    },
    {
        "question": "What is the output of `len(set([1, 2, 2, 3]))`?",
        "options": ["3", "4", "2", "None"],
        "answer": "3"
    },
    {
        "question": "How do you check if an element exists in a set?",
        "options": ["value in set", "set.contains(value)", "set.has(value)", "exists(value, set)"],
        "answer": "value in set"
    },
    {
        "question": "What will `{1, 2} | {2, 3}` return?",
        "options": ["{1, 2, 3}", "{2}", "{1, 3}", "{1, 2}"],
        "answer": "{1, 2, 3}"
    },
    {
        "question": "Which method is used to find the union of two sets?",
        "options": ["union()", "|", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "Which method is used to find the intersection of two sets?",
        "options": ["intersection()", "&", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "Which method is used to find the difference between two sets?",
        "options": ["difference()", "-", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "What does `{1, 2, 3}.intersection({2, 3, 4})` return?",
        "options": ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{}"],
        "answer": "{2, 3}"
    },
    {
        "question": "Which method checks if one set is a subset of another?",
        "options": ["issubset()", "subset()", "is_subset()", "checksubset()"],
        "answer": "issubset()"
    },
    {
        "question": "Which method checks if one set is a superset of another?",
        "options": ["issuperset()", "superset()", "is_superset()", "checksuperset()"],
        "answer": "issuperset()"
    },
    {
        "question": "What does `{1, 2, 3}.difference({2, 3, 4})` return?",
        "options": ["{1, 2, 3, 4}", "{2, 3}", "{1}", "{}"],
        "answer": "{1}"
    },
    {
        "question": "What will `{1, 2, 3} & {2, 3, 4}` return?",
        "options": ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{}"],
        "answer": "{2, 3}"
    },
    {
        "question": "Which method returns elements that are in one of the sets but not both?",
        "options": ["symmetric_difference()", "^", "Both A and B", "None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "Which operator performs set difference?",
        "options": ["-", "/", "*", "+"],
        "answer": "-"
    },
    {
        "question": "Which operator performs symmetric difference?",
        "options": ["^", "|", "&", "-"],
        "answer": "^"
    },
    {
        "question": "What will `{1, 2, 3} ^ {2, 3, 4}` return?",
        "options": ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{}"],
        "answer": "{1, 4}"
    },
    {
        "question": "Can a set contain duplicate elements?",
        "options": ["No", "Yes", "Only in Python 2", "Only if defined as a list"],
        "answer": "No"
    },
    {
        "question": "Can a set contain a list as an element?",
        "options": ["No", "Yes", "Only empty lists", "Only if converted to a string"],
        "answer": "No"
    },
    {
        "question": "Can a set contain a tuple?",
        "options": ["Yes", "No", "Only empty tuples", "Only if converted to a string"],
        "answer": "Yes"
    },
    {
        "question": "How do you copy a set?",
        "options": ["set.copy()", "set.clone()", "set.duplicate()", "set.deepcopy()"],
        "answer": "set.copy()"
    },
    {
        "question": "Which function converts a list into a set?",
        "options": ["set()", "list()", "tuple()", "dict()"],
        "answer": "set()"
    },
    {
        "question": "What is the result of `set('hello')`?",
        "options": ["{'h', 'e', 'l', 'o'}", "['h', 'e', 'l', 'o']", "'hello'", "None"],
        "answer": "{'h', 'e', 'l', 'o'}"
    },
    {
        "question": "What is the result of `set([1, 2, 2, 3])`?",
        "options": ["{1, 2, 3}", "{1, 2, 2, 3}", "[1, 2, 3]", "None"],
        "answer": "{1, 2, 3}"
    }
]