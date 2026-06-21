questions = [
    {
        "question": "Q1.What is the capital of India?",
        "options": ["a. Mumbai", "b. Delhi", "c. Bengaluru"],
        "answer": "b",
        "textAns": "Delhi"
    },
    {
        "question": "Q2.Which language is commonly used in Data Analysis?",
        "options": ["a. Java", "b. CSS", "c. Python"],
        "answer": "c",
        "textAns": "Python"
    },
    {
        "question": "Q3.Who developed Python?",
        "options": ["a. Guido van Rossum", "b. James Gosling", "c. Dennis Ritchie"],
        "answer": "a",
        "textAns": "Guido Van Rossum"
    },
    {
        "question": "Q4.Which keyword is used to define a function in Python?",
        "options": ["a. function", "b. def", "c. fun"],
        "answer": "b",
        "textAns": "def"
    },
    {
        "question": "Q5.Which symbol is used for comments in Python?",
        "options": ["a. //", "b. #", "c. /*"],
        "answer": "b",
        "textAns": "#"
    },
    {
        "question": "Q6.How many days are there in a week?",
        "options": ["a. 5", "b. 6", "c. 7"],
        "answer": "c",
        "textAns": "7"
    },
    {
        "question": "Q7.Which planet is known as the Red Planet?",
        "options": ["a. Mars", "b. Venus", "c. Jupiter"],
        "answer": "a",
        "textAns": "Mars" 
    },
    {
        "question": "Q8.What does CPU stand for?",
        "options": ["a. Central Processing Unit", "b. Computer Power Unit", "c. Central Program Utility"],
        "answer": "a",
        "textAns": "Central Processing Unit" 
    },
    {
        "question": "Q9.Which data type stores True or False values?",
        "options": ["a. int", "b. bool", "c. str"],
        "answer": "b",
        "textAns": "bool" 
    },
    {
        "question": "Q10.Which loop is used when the number of iterations is known?",
        "options": ["a. while", "b. if", "c. for"],
        "answer": "c",
        "textAns": "for" 
    }
]
score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Answer: ").lower()

    if(user_answer == q["answer"]):
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! Correct answer is {q['textAns']}")
    print( )

percentage = (score/len(questions))*100

print("Quiz is Finished!")
if percentage >= 90:
    print("Excellent!")
elif percentage >= 70:
    print("Good Job!")
elif percentage >= 50:
    print("Keep Practicing!")
else:
    print("Study More!")

print(f"your score: {score}")
print(f"Your percentage: {percentage:.2f}%")