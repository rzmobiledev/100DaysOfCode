from data import question_data
from quiz_brain import QuizBrain

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"]
#     },
# ]
class Question:
    def __init__(self, text: str, category: str, answer: bool):
        self.text = text
        self.answer = answer
        self.category = category


question_list = []

for i in question_data:
    answer = i['correct_answer']
    question = i['question']
    category = i['category']
    questions = Question(question, category, answer)
    question_list.append(questions)

quiz = QuizBrain(question_list)

while quiz.still_has_question():
    quiz.next_question()
