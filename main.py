import re

print("Our Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def perform_math():
    global run
    global previous

    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()]"', '', equation)
        previous = eval(equation)

        print("You typed", equation)


while run:
    perform_math()