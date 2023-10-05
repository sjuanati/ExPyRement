from v1.quiz.data import question_data
from v1.quiz.question_model import Question
from v1.quiz.quiz_brain import QuizBrain


def quiz():
    questions = []
    for q in question_data:
        questions.append(Question(q["text"], q["answer"]))

    new_quiz = QuizBrain(questions)
    new_quiz.ask_questions()