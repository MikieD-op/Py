Name = input("Hiya, what should I refer to you as? ")
print(f"Nice to meet you {Name}")
Age = int(input("You even an adult yet? How old are you? "))
if Age < 18:
    print("Piss off")
else:
    print(f"Neat, you're {Age} years of age, nice")
Colour = input("What's your favourite colour? ")
print (f"Oh {Colour} is rather lovely, if i do say so myself :D")
if Colour == "Blue":
    print("You basic af")
Show = input("Anyways, what's your fav TV show?")
print(f"{Show} is aight, I haven't seen it myself lol, but I loved watching Top Gear")
print("----------------------")
print(f"So, If i'm right, you're Name is {Name}, you're about {Age} years old, your favourite colour is {Colour}, and your favourite TV show is {Show}. Neat")
Yuh = input("Would you like to be friends? (Y/N) ")
if Yuh == "Y":
    print("Yippeeeeeeee :D")
if Yuh == "N":
    print("Begone")
