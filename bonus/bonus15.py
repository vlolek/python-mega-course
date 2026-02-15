import json

filepath = "bonus/questions.json"
with open(filepath, "r") as file:
    content = file.read()
   
data = json.loads(content)
score = 0
for question in data:
    print(question["question text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer:"))
    if user_choice == question["correct_answer"]:
        score = score + 1

for index, question in enumerate(data):
    message = f"{index + 1} - Your answer: {question['alternatives'][user_choice - 1]} | Correct answer: {question['alternatives'][question['correct_answer'] - 1]}"
    print(message)
print(score, "/", len(data))