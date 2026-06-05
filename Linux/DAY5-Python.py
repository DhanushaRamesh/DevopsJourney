#Lets learn python basics

#Part 1 — Variables -> Stores values in memory and variables help us reuse data
name = "name"
experience = 5

print(name)
print(experience)

#Part 2 — User Input -> Takes input from user and Stores it in a variable
name = input("Enter your name: ")
print("Hello", name)

#Part 3 — Conditions -> Makes decisions
experience = 5

if experience >= 5:
    print("Experienced Professional")
else:
    print("Learning Stage")

#Part 4 — Loops -> it does Repeats tasks
for i in range(5):
    print(i)

#Part 5 — Lists -> helps to Stores multiple values
tools = ["Git", "Linux", "Python"]

for tool in tools:
    print(tool)

#Part 6 — Functions -> Groups reusable code
def greet():
    print("Welcome to DevOps Journey")

greet()

#Mini Project --> Get name and goal from the user and check the condition - if its devops it prints great choice else keep learning
name = input("Enter your name: ")
goal = input("What are you learning? ")

print("Name:", name)
print("Learning:", goal)

if goal.lower() == "devops":
    print("Great choice!")
else:
    print("Keep learning!")