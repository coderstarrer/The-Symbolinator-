print("Welcome the National Temperature Center!")
print("We will examine temperatures and tell you if it is hot or cold.")
temp = float(input("What is the temperature today?"))
print("You said it is", str(temp), "celsius")

if 10 <= temp <= 30:
    print("The weather seems good today.")
    print("How about you go outside?")

elif -10 <= temp <= 1:
    print("The weather is very cold today")
    print("Do not go outside")

elif 30 >= temp <= 60:
    print("It's very hot today.")
    print("Under only severe circumstances must you go outside.")

elif 60 >= temp:
    print("It must be anarchy where you are.")

elif -30 >= temp:
    print("Do you live in Antarctica?")


else:
    print("It is cold.")
