print("Welcome to DSA quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Which sorting algorithm has a time complexity of O(n^2) in its worst-case scenario? ")
if answer.lower() == "bubble sort":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What traversal method visits nodes level by level in a binary tree? ")
if answer.lower() == "bfs":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("In graph theory, what is a cycle? ")
if answer.lower() == "loop":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is a data structure that follows the Last-In-First-Out (LIFO) principle? ")
if answer.lower() == "stack":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")