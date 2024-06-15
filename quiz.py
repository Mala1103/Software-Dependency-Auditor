import random

print("                     Welcome")
print("------------------------------------------------------")

quiz_questions = [
    {"question": "In Python, we use the ______ symbol to comment out a single line of code.", "answer": "#"},
    {"question": "The ______ method is used to add an element at the end of a list in Python.", "answer": "append()"},
    {"question": "In Python, the ______ function is used to get the length of a list.", "answer": "len()"},
    {"question": "To get user input in Python, we use the ______ function.", "answer": "input()"},
    {"question": "In Python, the ______ statement is used for decision-making and executing a block of code only if the condition is true.", "answer": "if"},
    {"question": "In Python, the ______ loop is used for iterating over a sequence.", "answer": "for"},
    {"question": "The ______ method is used to remove the last element from a list in Python.", "answer": "pop()"},
    {"question": "In Python, the ______ operator is used for exponentiation.", "answer": "**"},
    {"question": "The ______ method is used to convert a string to uppercase in Python.", "answer": "upper()"},
    {"question": "In Python, the ______ function is used to find the maximum value among the arguments passed.", "answer": "max()"},
    {"question": "The ______ method is used to reverse the elements of a list in Python.", "answer": "reverse()"}
]

def create_question():
    new_question = input("Enter the new question: ")
    new_answer = input("Enter the answer for the new question: ")
    quiz_questions.append({"question": new_question, "answer": new_answer})
    print("Question added successfully!")

def delete_question():
    question_to_delete = input("Enter the question number to delete: ")
    index_to_delete = int(question_to_delete) - 1

    if 0 <= index_to_delete < len(quiz_questions):
        del quiz_questions[index_to_delete]
        print("Question deleted successfully!")
    else:
        print("Invalid question number.")

def update_question():
    question_to_update = input("Enter the question number to update: ")
    index_to_update = int(question_to_update) - 1

    if 0 <= index_to_update < len(quiz_questions):
        quiz_questions[index_to_update]["question"] = input("Enter the new question: ")
        quiz_questions[index_to_update]["answer"] = input("Enter the new answer for the question: ")
        print("Question updated successfully!")
    else:
        print("Invalid question number.")

def display_questions():
    print("Quiz Questions:")
    for i, q in enumerate(quiz_questions, start=1):
        print(f"{i}. {q['question']}: {q['answer']}")

def run_quiz():
    score = 0
    questions = list(quiz_questions)  # Create a copy of quiz_questions
    random.shuffle(questions)

    for q in questions:
        user_answer = input(f"{q['question']} ")
        correct_answer = q['answer']

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")

    print(f"You scored {score}/{len(quiz_questions)}.")

# Main menu
while True:
    print("\nMenu:")
    print("1. Run Quiz")
    print("2. Create Question")
    print("3. Delete Question")
    print("4. Update Question")
    print("5. Display Questions")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        run_quiz()
    elif choice == "2":
        create_question()
    elif choice == "3":
        delete_question()
    elif choice == "4":
        update_question()
    elif choice == "5":
        display_questions()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break 
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
