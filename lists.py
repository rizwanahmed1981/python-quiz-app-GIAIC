lists = [
    {
        "question": "How do you create an empty list in Python?",
        "options": ["list = {}", "list = []", "list = ()", "list = ''"],
        "answer": "list = []"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": ["append()", "add()", "insert()", "extend()"],
        "answer": "append()"
    },
    {
        "question": "What will be the output of `len([1, 2, 3, 4])`?",
        "options": ["3", "4", "5", "Error"],
        "answer": "4"
    },
    {
        "question": "How can you access the last element of a list?",
        "options": ["list[-1]", "list[last]", "list[len(list)]", "list[0]"],
        "answer": "list[-1]"
    },
    {
        "question": "Which method is used to remove a specific element from a list?",
        "options": ["delete()", "remove()", "pop()", "discard()"],
        "answer": "remove()"
    },
    {
        "question": "Which method removes the last item from a list?",
        "options": ["pop()", "remove()", "del()", "discard()"],
        "answer": "pop()"
    },
    {
        "question": "What is the output of `list(range(5))`?",
        "options": ["[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4]", "[0, 1, 2, 3, 4, 5]", "Error"],
        "answer": "[0, 1, 2, 3, 4]"
    },
    {
        "question": "Which method is used to insert an element at a specific position in a list?",
        "options": ["insert()", "append()", "extend()", "add()"],
        "answer": "insert()"
    },
    {
        "question": "What does `list1 + list2` do in Python?",
        "options": ["Adds elements numerically", "Combines lists", "Multiplies lists", "Throws an error"],
        "answer": "Combines lists"
    },
    {
        "question": "Which method returns the index of a specified element?",
        "options": ["find()", "search()", "index()", "position()"],
        "answer": "index()"
    },
    {
        "question": "How do you sort a list in ascending order?",
        "options": ["list.sort()", "sorted(list)", "sort(list)", "Both A and B"],
        "answer": "Both A and B"
    },
    {
        "question": "How do you reverse a list?",
        "options": ["list.reverse()", "reversed(list)", "list[::-1]", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Which function creates a copy of a list?",
        "options": ["list.copy()", "list.clone()", "list.duplicate()", "copy(list)"],
        "answer": "list.copy()"
    },
    {
        "question": "How do you check if an item exists in a list?",
        "options": ["in", "exists()", "contains()", "find()"],
        "answer": "in"
    },
    {
        "question": "What is the output of `sum([1, 2, 3, 4])`?",
        "options": ["10", "9", "Error", "1234"],
        "answer": "10"
    },
    {
        "question": "Which method removes all elements from a list?",
        "options": ["clear()", "remove()", "delete()", "discard()"],
        "answer": "clear()"
    },
    {
        "question": "How do you get the number of occurrences of an element in a list?",
        "options": ["count()", "find()", "index()", "occurrence()"],
        "answer": "count()"
    },
    {
        "question": "How can you concatenate two lists?",
        "options": ["list1.extend(list2)", "list1 + list2", "Both A and B", "list1 * list2"],
        "answer": "Both A and B"
    },
    {
        "question": "What does `list[1:3]` return?",
        "options": ["First three elements", "Second and third elements", "Third element", "Error"],
        "answer": "Second and third elements"
    },
    {
        "question": "Which function returns the largest element in a list?",
        "options": ["max()", "highest()", "top()", "biggest()"],
        "answer": "max()"
    },
    {
        "question": "What happens when you try to access an index that doesn't exist?",
        "options": ["Returns None", "Returns empty list", "Throws IndexError", "Ignores it"],
        "answer": "Throws IndexError"
    },
    {
        "question": "What does `list[::-1]` do?",
        "options": ["Reverses the list", "Sorts the list", "Clears the list", "Duplicates the list"],
        "answer": "Reverses the list"
    },
    {
        "question": "Which function returns the smallest element in a list?",
        "options": ["min()", "smallest()", "low()", "bottom()"],
        "answer": "min()"
    },
    {
        "question": "What is the result of `['a', 'b'] * 3`?",
        "options": ["['a', 'b', 'a', 'b', 'a', 'b']", "Error", "['aaa', 'bbb']", "['a', 'b', 3]"],
        "answer": "['a', 'b', 'a', 'b', 'a', 'b']"
    },
    {
        "question": "Which method adds multiple elements to a list?",
        "options": ["append()", "extend()", "insert()", "addAll()"],
        "answer": "extend()"
    },
    {
        "question": "What is the default sorting order of `list.sort()`?",
        "options": ["Ascending", "Descending", "Random", "None"],
        "answer": "Ascending"
    },
    {
        "question": "What is `list1 = list2` doing?",
        "options": ["Copying list", "Creating reference", "Merging lists", "Cloning list"],
        "answer": "Creating reference"
    },
    {
        "question": "How do you remove an item at a specific index?",
        "options": ["remove(index)", "del list[index]", "pop(index)", "Both B and C"],
        "answer": "Both B and C"
    },
    {
        "question": "What does `list.sort(reverse=True)` do?",
        "options": ["Sorts in ascending", "Sorts in descending", "Throws error", "Does nothing"],
        "answer": "Sorts in descending"
    },
    {
        "question": "What does `list.append([5, 6])` do?",
        "options": ["Adds 5 and 6 separately", "Adds [5, 6] as a sublist", "Throws error", "Ignores it"],
        "answer": "Adds [5, 6] as a sublist"
    },
    {
        "question": "Which function removes an element by index and returns it?",
        "options": ["remove()", "pop()", "del()", "discard()"],
        "answer": "pop()"
    },
    {
        "question": "What is the correct way to iterate over a list?",
        "options": ["for i in list:", "while i < len(list):", "Both A and B", "None"],
        "answer": "Both A and B"
    },
    {
        "question": "What is the result of `sorted([3, 1, 4, 1, 5, 9])`?",
        "options": ["[1, 1, 3, 4, 5, 9]", "[9, 5, 4, 3, 1, 1]", "None", "Error"],
        "answer": "[1, 1, 3, 4, 5, 9]"
    }
]