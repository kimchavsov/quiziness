""""
Requirement: requests package
A Quiz Game that fetch quiz from Open Trivia Database api
This game have 3 difficulties, {how many} Categories, Type of question
"""

from question_generate import Generate
import random
import text_art
import html


def get_question_data(data, question_type):
    """
    Get data from api
    return: question list consist of dictionary witb question and answer
    """
    question_data = []

    for question in data:
        text = question['question']
        correct_answer = question['correct_answer']
        answer = []

        # Check if multiple choice or true or false question
        if question_type == 'multiple':
            answer.append(correct_answer)
            for ans in question['incorrect_answers']:
                answer.append(ans)
            random.shuffle(answer)
            new_quest = {'question': text, "correct_answer": correct_answer, "answer": answer}
        else:
            new_quest = {'question': text, "correct_answer": correct_answer}

        question_data.append(new_quest)

    return question_data

def check_answer(correct_answer, user_answer):
    """
    Function to compare answer with user_answer and correct_answer
    :param correct_answer:
    :param user_answer:
    :return: True or False (True dedicate correct and False dedicate incorrect)
    """
    if correct_answer.lower() == user_answer.lower():
        return True
    else:
        return False


def update_score(score):


def main():
    difficulty = input("""Please Select your difficulty: 
    + Enter 1 or easy for Easy mode with 8 questions
    + Enter 2 or medium for Medium mode with 16 questions
    + Enter 3 or hard for Hard mode with 24 questions
    >>> """)
    question_type = input("""Please Select your question type:
    + Enter 1 for True/False questions
    + Enter 2 for multiple choice questions 
    >>> """)

    score = 0

    question_data = Generate(difficulty, question_type)
    data = question_data.get_data()
    question_type = question_data.get_question_type()

    print(data)
    question_data = get_question_data(data, question_type)

    for i in range(len(question_data)):
        question = question_data[i]
        print("Q" + str(i + 1) + ". " + html.unescape(question["question"]))
        if question_type == 'multiple':
            for i in range(len(question['answer'])):
                ans = question['answer']
                print(str(i + 1) + '. ' + html.unescape(ans[i]))
            user_answer = input("Please enter your answer: ")
            if check_answer(question['correct_answer'], user_answer):
                score += 1
                print("Good job! You answer correctly")
            else:
                print("Sorry! It is incorrectly, Try harder!!!!")

    update_score(score)



if __name__ == "__main__":
    print(text_art.welcome_text)
    print(text_art.to)
    print(text_art.quizinese)
    main()
