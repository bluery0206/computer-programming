
questions = [
    {
        "question": "What keyword defines a function in Python?",
        "choices": {
            "A": "func",
            "B": "def",
            "C": "function",
            "D": "define"
        },
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "choices": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set"
        },
        "answer": "C"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "choices": {
            "A": "//",
            "B": "#",
            "C": "--",
            "D": "/* */"
        },
        "answer": "B"
    }
]

student_name = input("Enter your name: ")

score = 0
exam_taken = False

while True:
    print("\n=== Exam Menu ===")
    print("1. Start Exam")
    print("2. View Score")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        if exam_taken:
            print("You have already taken the exam.")
            continue

        print("\nStarting exam...\n")

        for q in questions:
            print(q["question"])

            for key in q["choices"]:
                print(key + ".", q["choices"][key])

            answer = input("Enter your answer: ").upper()

            if answer == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print("Wrong! Correct answer:", q["answer"], "\n")

        exam_taken = True
        print("Exam finished.")

    elif choice == "2":
        if not exam_taken:
            print("You haven't taken the exam yet.")
        else:
            print("\nStudent:", student_name)
            print("Score:", score, "/", len(questions))

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid option")