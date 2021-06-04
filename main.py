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
    :return: 1 if it is correct and 0 if it is incorrect (True dedicate correct and False dedicate incorrect)
    """
    if correct_answer.lower() == user_answer.lower():
        print("Good job! You answer correctly\n")
        return 1
    else:
        print("Sorry! It is incorrect, Try harder!!!!\n")
        return 0


def update_score(score, total_question):
    score = (score / total_question) * 100
    if score == 100.0:
        return f"Fantastic You're a genius\nYou scored {score}/100.0"
    elif score > 90:
        return f"Well done! You're rock\nYou scored {score}/100.0"
    elif score > 70:
        return f'Great! You made it\nYou scored {score}/100.0'
    elif score > 50:
        return f'Gooood! You pass the test\nYou scored {score}/100.0'
    else:
        return f"You almost made it, keep up the hard work!!!\nYou scored {score}/100.0"


def generate_answer(question, question_type):
    """
    Function get question and question type then compute possible answer and ask user for
    their answer to the question.
    :param question:
    :param question_type:
    :return: 1 if the user answer correctly 0 if it wrong
    """
    if question_type == 'multiple':
        for i in range(len(question['answer'])):
            ans = question['answer']
            print(str(i + 1) + '. ' + html.unescape(ans[i]))
        user_answer = input("Please enter your answer: ")
        return check_answer(question['correct_answer'], user_answer)
    else:
        user_answer = input("Please enter True or False: ")
        return check_answer(question['correct_answer'], user_answer)


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
    # generate question data
    question_data = Generate(difficulty, question_type)
    data = question_data.get_data()
    question_type = question_data.get_question_type()
    question_data = get_question_data(data, question_type)

    # Loop through question and ask the user
    for i in range(len(question_data)):
        question = question_data[i]
        print("Q" + str(i + 1) + ". " + html.unescape(question["question"]))
        score += generate_answer(question, question_type)

    # Print the result for the user
    print(update_score(score, len(question_data)))


if __name__ == "__main__":
    print(text_art.welcome_text)
    print(text_art.to)
    print(text_art.quiziness)
    main()
