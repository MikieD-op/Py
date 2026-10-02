q1 = input("Who was the PM that succeeded Margaret Thatcher? ")
if q1.capitalise() == "John Major":
    print("Correct!")
elif q1.lower() == "john major":
    print("Correct!")
else:
    print("Incorrect!")
