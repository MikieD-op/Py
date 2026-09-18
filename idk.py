Age = int(input("What's your age bud? "))
Student= input("Are you a student? (y/n) ").strip().lower()
if Age <= 12:
    price = 5
    print("You're ticket costs £5")
elif Age > 12 and Age <= 18:
    price = 7
    print("You're ticket costs £7")
elif Age > 18 and Age <= 64 and Student == 'n':
    price = 10
    print("You're ticket costs £10")
elif Age >= 65:
    price = 6
    print("You're ticket costs £6")
elif Age >18 and Student == 'y':
    print("you get a £2 discount, you cheeky bastard :3")
    student_discount = price - 2
    print(f"Your ticket costs £{student_discount}")

