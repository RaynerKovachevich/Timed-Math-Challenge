import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    rigth = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(rigth)
    answer = eval(expr)
    return expr, answer

wrong = 0

input("Press Enter to Start")
print("_______________")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problema #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("_______________")
print("Nice Work! You finished in", total_time, "Seconds!")
