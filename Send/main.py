import counties
import pm
import constituency
import quiz

if __name__ == "__main__":
    name = input("Welcome to the program, what's your name? ")
    print(f"Hello, {name}!\n")

    print("========CATEGORIES========")
    print("1. Counties")
    print("2. Prime Ministers")
    print("3. Constituencies")

    choice = input("Please select a category (1-3): ")
    
    if choice == "1":
        quiz.run_quiz(counties.questions)
    elif choice == "2":
        quiz.run_quiz(pm.questions)
    elif choice == "3":
        quiz.run_quiz(constituency.questions)
    else:
        print("Invalid choice. Please select a valid category.")