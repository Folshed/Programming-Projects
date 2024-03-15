print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What Country has the highest life expectancy? ")
if answer == "Hong Kong":
    print('Correct!')
    score += 5
else:
    print("Incorrect!")

answer = input("What is the most common lastname in United States? ")
if answer == "Smith":
    print('Correct!')
    score += 5
else:
    print("Incorrect!")

answer = input("How many elements are on the periodic table? ")
if answer == "118":
    print('Correct!')
    score += 10
else:
    print("Incorrect!")

answer = input("Which planet in the Milky Way is the hottest? ")
if answer == "Venus":
    print('Correct!')
    score += 5
else:
    print("Incorrect!")

answer = input("What is the largest Spanish-speaking city in the world? ")
if answer == "Mexico City":
    print('Correct!')
    score += 10
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")