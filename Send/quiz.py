def run_quiz(question_list):
    score = 0
    for q in question_list:
        answer = input(q["question"] + " ")
        if answer.strip().lower() == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Lol, lmao even, The answer was {q['answer']}.\n")
            
    print(f"Quiz finished! You scored {score}/{len(question_list)}.")