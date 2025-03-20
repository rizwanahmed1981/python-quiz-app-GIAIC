asyncp = [
    {
        "question": "Which Python module is primarily used for asynchronous programming?",
        "options": ["threading", "asyncio", "multiprocessing", "concurrent"],
        "answer": "asyncio"
    },
    {
        "question": "Which keyword is used to define an asynchronous function in Python?",
        "options": ["async", "await", "future", "coroutine"],
        "answer": "async"
    },
    {
        "question": "Which keyword is used to pause execution inside an async function?",
        "options": ["await", "yield", "pause", "stop"],
        "answer": "await"
    },
    {
        "question": "What does an async function return?",
        "options": ["A coroutine object", "A thread", "A normal function", "A generator"],
        "answer": "A coroutine object"
    },
    {
        "question": "Which function is used to run an async function in Python?",
        "options": ["asyncio.run()", "asyncio.start()", "asyncio.call()", "run()"],
        "answer": "asyncio.run()"
    },
    {
        "question": "What is a coroutine?",
        "options": ["A special function that can be paused and resumed", "A type of class", "A synchronous function", "A function that only runs once"],
        "answer": "A special function that can be paused and resumed"
    },
    {
        "question": "Which Python versions fully support asyncio?",
        "options": ["3.3+", "3.4+", "3.5+", "3.6+"],
        "answer": "3.5+"
    },
    {
        "question": "What is the main advantage of asynchronous programming?",
        "options": ["Improves CPU-bound task performance", "Improves I/O-bound task performance", "Uses more memory", "Reduces code complexity"],
        "answer": "Improves I/O-bound task performance"
    },
    {
        "question": "What does `asyncio.sleep(2)` do?",
        "options": ["Pauses execution for 2 seconds", "Blocks the entire program", "Creates a thread", "Stops execution permanently"],
        "answer": "Pauses execution for 2 seconds"
    },
    {
        "question": "Which method is used to run multiple async tasks concurrently?",
        "options": ["asyncio.gather()", "asyncio.run_all()", "asyncio.execute()", "asyncio.multi_run()"],
        "answer": "asyncio.gather()"
    },
    {
        "question": "Which of the following is true about async functions?",
        "options": ["They must always use 'await' inside them", "They must return a list", "They can only run in a separate thread", "They require Python 2.x"],
        "answer": "They must always use 'await' inside them"
    },
    {
        "question": "What is the purpose of `asyncio.create_task()`?",
        "options": ["Schedules an async function to run concurrently", "Creates a new thread", "Stops an async function", "Deletes a coroutine"],
        "answer": "Schedules an async function to run concurrently"
    },
    {
        "question": "Which statement is true about `asyncio.run()`?",
        "options": ["It can be called multiple times in the same program", "It can only be used once", "It runs in a new thread", "It is deprecated"],
        "answer": "It can only be used once"
    },
    {
        "question": "How do you properly call an async function inside a synchronous function?",
        "options": ["Use asyncio.run()", "Use await", "Use yield", "Use async with"],
        "answer": "Use asyncio.run()"
    },
    {
        "question": "Which of the following does `asyncio.gather()` do?",
        "options": ["Runs multiple async tasks concurrently", "Runs multiple async tasks sequentially", "Stops all running tasks", "Creates multiple threads"],
        "answer": "Runs multiple async tasks concurrently"
    },
    {
        "question": "What is an event loop in asyncio?",
        "options": ["A mechanism to manage asynchronous tasks", "A loop inside an async function", "A type of Python thread", "A built-in method"],
        "answer": "A mechanism to manage asynchronous tasks"
    },
    {
        "question": "Which function gets the current event loop?",
        "options": ["asyncio.get_event_loop()", "asyncio.run()", "asyncio.loop()", "asyncio.current_loop()"],
        "answer": "asyncio.get_event_loop()"
    },
    {
        "question": "How do you cancel an async task?",
        "options": ["task.cancel()", "task.stop()", "asyncio.cancel_task()", "await task.cancel()"],
        "answer": "task.cancel()"
    },
    {
        "question": "What is a Future in asyncio?",
        "options": ["A placeholder for an eventual result", "A function that runs forever", "A type of generator", "A built-in Python function"],
        "answer": "A placeholder for an eventual result"
    },
    {
        "question": "How do you handle exceptions in async functions?",
        "options": ["Using try-except", "Using await", "Using async handler", "Using event loop"],
        "answer": "Using try-except"
    },
    {
        "question": "What does `await` do?",
        "options": ["Pauses execution until the awaited task completes", "Creates a new thread", "Runs a task in a loop", "Stops the execution permanently"],
        "answer": "Pauses execution until the awaited task completes"
    },
    {
        "question": "Can you use `await` outside of an async function?",
        "options": ["No", "Yes", "Only in threads", "Only in Python 2.x"],
        "answer": "No"
    },
    {
        "question": "What happens if you call an async function without `await`?",
        "options": ["It returns a coroutine object", "It executes immediately", "It throws an error", "It blocks the program"],
        "answer": "It returns a coroutine object"
    },
    {
        "question": "Which method is used to run a coroutine inside an existing event loop?",
        "options": ["asyncio.ensure_future()", "asyncio.run()", "asyncio.call()", "asyncio.start()"],
        "answer": "asyncio.ensure_future()"
    },
    {
        "question": "What is `asyncio.run_forever()` used for?",
        "options": ["Keeps the event loop running indefinitely", "Runs multiple async functions", "Stops an async function", "Blocks all tasks"],
        "answer": "Keeps the event loop running indefinitely"
    },
    {
        "question": "What is the difference between `asyncio.create_task()` and `asyncio.gather()`?",
        "options": ["`create_task()` schedules individual tasks, `gather()` runs multiple at once", "`gather()` is deprecated", "`create_task()` can only run once", "They perform the same function"],
        "answer": "`create_task()` schedules individual tasks, `gather()` runs multiple at once"
    },
    {
        "question": "Which of the following is an example of an I/O-bound task?",
        "options": ["Reading a file", "Sorting a list", "Calculating Fibonacci numbers", "Processing a large dataset"],
        "answer": "Reading a file"
    },
    {
        "question": "Can you mix async and threading in Python?",
        "options": ["Yes, but carefully", "No", "Only in Python 3.9+", "Only in Jupyter Notebooks"],
        "answer": "Yes, but carefully"
    },
    {
        "question": "What is the difference between threading and asyncio?",
        "options": ["Threading uses multiple OS threads, asyncio is single-threaded", "Threading is faster than asyncio", "Asyncio is better for CPU-bound tasks", "Threading does not support concurrency"],
        "answer": "Threading uses multiple OS threads, asyncio is single-threaded"
    },
    {
        "question": "Which function in `asyncio` allows a synchronous function to run in an async context?",
        "options": ["loop.run_in_executor()", "asyncio.run()", "asyncio.call()", "asyncio.future()"],
        "answer": "loop.run_in_executor()"
    },
    {
        "question": "What is the primary purpose of async functions in Python?",
        "options": ["To handle I/O-bound tasks efficiently", "To improve CPU-bound operations", "To create new processes", "To use multiple threads"],
        "answer": "To handle I/O-bound tasks efficiently"
    },
    {
        "question": "Which keyword is required to define an async function?",
        "options": ["async", "await", "coroutine", "yield"],
        "answer": "async"
    },
    {
        "question": "What does the `await` keyword do in an async function?",
        "options": ["Pauses execution until the awaited task completes", "Creates a new thread", "Blocks the entire program", "Stops execution"],
        "answer": "Pauses execution until the awaited task completes"
    },
    {
        "question": "Can async functions be executed directly like normal functions?",
        "options": ["No, they return coroutine objects", "Yes, they work like normal functions", "Only in Python 2.x", "Only with threads"],
        "answer": "No, they return coroutine objects"
    },
    {
        "question": "Which module provides support for async programming in Python?",
        "options": ["asyncio", "concurrent", "threading", "multiprocessing"],
        "answer": "asyncio"
    },
    {
        "question": "How do you execute an async function from a synchronous function?",
        "options": ["Use asyncio.run()", "Use await", "Use threading.run()", "Use async.execute()"],
        "answer": "Use asyncio.run()"
    },
    {
        "question": "What type of object does an async function return?",
        "options": ["Coroutine object", "Future", "Thread", "List"],
        "answer": "Coroutine object"
    },
    {
        "question": "Which function is used to run multiple async functions concurrently?",
        "options": ["asyncio.gather()", "asyncio.create_task()", "asyncio.multi_run()", "asyncio.thread_run()"],
        "answer": "asyncio.gather()"
    },
    {
        "question": "What happens if you call an async function without `await`?",
        "options": ["It returns a coroutine object", "It executes immediately", "It throws an error", "It blocks the program"],
        "answer": "It returns a coroutine object"
    },
    {
        "question": "Which of the following is a valid async function definition?",
        "options": [
            "async def my_function(): pass",
            "def async my_function(): pass",
            "def my_function() async: pass",
            "async function my_function(): pass"
        ],
        "answer": "async def my_function(): pass"
    },
    {
        "question": "What is the purpose of `asyncio.sleep(2)`?",
        "options": ["Pauses execution without blocking", "Blocks the entire program", "Creates a new thread", "Stops execution"],
        "answer": "Pauses execution without blocking"
    },
    {
        "question": "Which Python version introduced async/await syntax?",
        "options": ["3.5", "3.6", "3.3", "3.8"],
        "answer": "3.5"
    },
    {
        "question": "What is `asyncio.create_task()` used for?",
        "options": ["Schedules an async function to run concurrently", "Creates a thread", "Stops an async function", "Deletes a coroutine"],
        "answer": "Schedules an async function to run concurrently"
    },
    {
        "question": "Can you mix async functions and threading?",
        "options": ["Yes, but carefully", "No", "Only in Python 3.9+", "Only in Jupyter Notebooks"],
        "answer": "Yes, but carefully"
    },
    {
        "question": "Which of the following can be awaited?",
        "options": ["Coroutines, Tasks, and Futures", "Only coroutines", "Only functions", "Only generators"],
        "answer": "Coroutines, Tasks, and Futures"
    },
    {
        "question": "How do you properly call an async function inside another async function?",
        "options": ["await function_name()", "async function_name()", "call function_name()", "function_name.await()"],
        "answer": "await function_name()"
    },
    {
        "question": "Which function starts the event loop?",
        "options": ["asyncio.run()", "asyncio.start()", "asyncio.execute()", "eventloop.run()"],
        "answer": "asyncio.run()"
    },
    {
        "question": "What is an event loop?",
        "options": ["A mechanism to manage async tasks", "A function inside an async function", "A type of Python thread", "A built-in method"],
        "answer": "A mechanism to manage async tasks"
    },
    {
        "question": "Which function gets the current event loop?",
        "options": ["asyncio.get_event_loop()", "asyncio.run()", "asyncio.loop()", "asyncio.current_loop()"],
        "answer": "asyncio.get_event_loop()"
    },
    {
        "question": "How do you run an async function in an already running event loop?",
        "options": ["asyncio.create_task()", "asyncio.run()", "await function_name()", "async function_name()"],
        "answer": "asyncio.create_task()"
    },
    {
        "question": "Can an async function contain regular `def` functions?",
        "options": ["Yes", "No", "Only if they use await", "Only in Python 3.8+"],
        "answer": "Yes"
    },
    {
        "question": "What is the purpose of `asyncio.ensure_future()`?",
        "options": ["Runs a coroutine as a Task", "Stops an async function", "Creates a thread", "Executes synchronous code"],
        "answer": "Runs a coroutine as a Task"
    },
    {
        "question": "What is a Future in asyncio?",
        "options": ["A placeholder for an eventual result", "A function that runs forever", "A type of generator", "A built-in Python function"],
        "answer": "A placeholder for an eventual result"
    },
    {
        "question": "How do you handle exceptions inside an async function?",
        "options": ["Using try-except", "Using await", "Using async handler", "Using event loop"],
        "answer": "Using try-except"
    },
    {
        "question": "Which method is used to stop an async task?",
        "options": ["task.cancel()", "task.stop()", "asyncio.cancel_task()", "await task.cancel()"],
        "answer": "task.cancel()"
    },
    {
        "question": "Can an async function return a normal value?",
        "options": ["Yes", "No", "Only if wrapped in await", "Only in Python 3.10+"],
        "answer": "Yes"
    },
    {
        "question": "What is `asyncio.wait()` used for?",
        "options": ["Waits for multiple async tasks to complete", "Blocks a single function", "Runs tasks sequentially", "Stops execution"],
        "answer": "Waits for multiple async tasks to complete"
    },
    {
        "question": "How do you define an asynchronous context manager?",
        "options": [
            "Using `async with`",
            "Using `with async`",
            "Using `await with`",
            "Using `with await`"
        ],
        "answer": "Using `async with`"
    },
    {
        "question": "What is the purpose of `asyncio.shield()`?",
        "options": [
            "Prevents a coroutine from being cancelled",
            "Cancels a coroutine",
            "Runs a coroutine immediately",
            "Stops an event loop"
        ],
        "answer": "Prevents a coroutine from being cancelled"
    }
]