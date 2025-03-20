import streamlit as st
import random
import time
from style import *
from variables import *
from operators import *
from stringCasting import *
from controlFlow import *
from lists import *
from tuples import *
from dictioneries import *
from sets import *
from modules import *
from functions import *
from exceptionHandling import *
from fileHandling import *
from oops import *
from asynchronousProgramming import *


# st.set_page_config(page_title="Python Quiz App", page_icon="🧠", layout="wide")

st.markdown("<h1 style='text-align:center;'>PYTHON QUIZ APP </h1>", unsafe_allow_html=True)


menu_options = {
    "Home Page": "🏠 Home Page",
    "Variables": "Variables",
    "Operators": "Operators",
    "String Casting": "Srting Casting",
    "Control Flow": "Control Flow",
    "Lists": "Lists",
    "Tuples": "Tuples",
    "Dictioneries": "Dictioneries",
    "Sets": "Sets",
    "Modules": "Modules",
    "Functions": "Functions",
    "Exception Handling": "Exception Handling",
    "File Handling": "File Handling",
    "Object Oriented Programming": "Object Oriented Programming",
    "Asynchronous Programming": "Asynchronous Programming",
}

menu = st.sidebar.selectbox("Choose a Topic For Quiz", list(menu_options.values()))


# home Page
if menu == menu_options["Home Page"]:
    st.markdown(f"""<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>
    This App is Created For Python Quiz Practice



</h2>""", unsafe_allow_html=True)
    
    st.markdown(f"""<h3>
    The Topics I Tried To Cover Are \n
    1...Variables\n
    2...Operators\n
    3...String Casting\n
    4...Control Flow\n
    5...Lists\n
    6...Tuples\n
    7...Dictioneries\n
    8...Sets\n
    9...Modules\n
    10...Functions\n
    11...Exception Handling\n
    12...File Handling\n
    13...Object Oriented Programming (Ooop)\n
    14...Asynchronous Programming\n


</h3>""",unsafe_allow_html=True)
    st.markdown(f"<h4 style='background-color:#FFEB55; color:#640D5F; border-radius:30px; text-align:center; padding:2px;'>Created by 💐Rizwan Ahmed 💐\n NovaNex Innovations 💐\n Special Thanks to 🌹Sir Zia, 🌹🌹Sir Arif Rozani🌹 </h4>", unsafe_allow_html=True)
    st.write(f"<p style='background0color:#EE66A6; color:#FFEB55; border-radius:30px; text-align:start; padding:3px;'>* there are more topics to come in updates</p>", unsafe_allow_html=True)





# for variables
if menu == menu_options["Variables"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Variables</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(variables)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(variables)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")

# for Operators in python
if menu == menu_options["Operators"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Operators</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(operators)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(operators)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")

# for String Casting in python
if menu == menu_options["String Casting"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>String Casting</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(stringCasting)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(stringCasting)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")

# for Control flow in python
if menu == menu_options["Control Flow"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Control Flow</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(controlflow)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(controlflow)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")


# for Lists in python
if menu == menu_options["Lists"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Lists</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(lists)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(lists)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")



# for Tuples in python
if menu == menu_options["Tuples"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Tuples</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(tuples)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(tuples)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")




# for Dictioneries in python
if menu == menu_options["Dictioneries"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Dictioneries</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(dictioneries)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(dictioneries)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")





# for Sets in python
if menu == menu_options["Sets"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Sets</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(sets)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(sets)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")






# for Modules in python
if menu == menu_options["Modules"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Modules</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(modules)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(modules)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")







# for Functions in python
if menu == menu_options["Functions"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Functions</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(functions)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(functions)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")








# for Exception Handling in python
if menu == menu_options["Exception Handling"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Exception Handling</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(exceptionHandlings)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(exceptionHandlings)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")









# for File Handling in python
if menu == menu_options["File Handling"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>File Handling</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(fileHandling)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(fileHandling)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")









# for Object Oriented Programming in python
if menu == menu_options["Object Oriented Programming"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Object Oriented Programming</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(oops)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(oops)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")







# for Asynchronous Programming in python
if menu == menu_options["Asynchronous Programming"]:
    st.markdown(f"<h2 style='background-color:#640D5F; color:#FFEB55; border-radius:30px; text-align:center; padding:6px;'>Asynchronous Programming</h2>", unsafe_allow_html=True)
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(asyncp)

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    question = st.session_state.current_question

    st.subheader(question["question"])

    selected_option = st.radio("Choose Your Answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.session_state.total_score += 5
            st.success(f"✅ Correct! Your Score is {st.session_state.total_score}")

        else:
            st.error(f"❌ Incorrect! The Correct Answer is {question['answer']}. Score is {st.session_state.total_score}")

        time.sleep(3)
        st.session_state.current_question = random.choice(asyncp)
        st.rerun()

    st.success(f"Total Score: {st.session_state.total_score}")

