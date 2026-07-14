# Quiz Application

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "2. Which language is used for AI and Data Science?",
        "options": ["A. Java", "B. Python", "C. C", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "3. How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "5. What is 10 + 15?",
        "options": ["A. 20", "B. 25", "C. 30", "D. 35"],
        "answer": "B"
    }
]

score = 0

print("===================================")
print("      Welcome to Quiz App")
print("===================================")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", q["answer"])

print("\n===================================")
print("Quiz Finished")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")