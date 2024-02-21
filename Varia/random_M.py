import random

def get_answer():
    answers = ["No way", "Yes, but not sure", "Maybe", "No", "After lunch"]
    return random.choice(answers)

if __name__ == "__main__":
    user_guess = ""

    while user_guess != get_answer():
        question = "Will Marcus come to the class? (Enter Yes/No): "
        print(question)
        user_guess = input().strip().capitalize()

        if user_guess == get_answer():
            print("Congratulations! You've won!\n")
        else:
            print(f"Sorry, the correct answer was: {get_answer()}.\n")