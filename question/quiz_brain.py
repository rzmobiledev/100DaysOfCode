# TODO: asking the questions
# TODO: checking if the answers was correct
# TODO: checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.attempt = len(self.question_list)
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q {self.question_number}. {current_question.text} (True/False): ")
        if current_answer != current_question.answer:
            print(f"Wrong answer.")
            print(f"The correct answer was: {current_question.answer}")
            print(f"Your current score is: {self.score}/{self.attempt}\n")
        else:
            self.score += 1
            print("you got it right!")
            print(f"The correct answer was: {current_question.answer}")
            print(f"Your current score is: {self.score}/{self.attempt}\n")

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False
