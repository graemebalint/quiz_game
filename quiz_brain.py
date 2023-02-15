class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # more_questions = True
        return self.question_number < len(self.question_list)


    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.guess = input(f"Q{self.question_number}: {self.current_question.text} (True/False): ")
        # input(f"Q{question_number}: {question_list[question_number].text}")

    def check_answer(self):
        if self.current_question.answer == self.guess:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong answer!")


