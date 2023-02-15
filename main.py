from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(0, len(question_data)):
    question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()
    quiz.check_answer()
    print(f"Score: {quiz.score}/{quiz.question_number}")