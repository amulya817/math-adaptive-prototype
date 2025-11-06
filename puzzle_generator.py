import random

def generate_puzzle(level):
    """Generate a simple math puzzle based on difficulty level."""
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-"])
    elif level == "Medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
        op = random.choice(["+", "-", "*"])
    else:
        a, b = random.randint(10, 100), random.randint(1, 10)
        op = random.choice(["+", "-", "*", "/"])

    question = f"{a} {op} {b}"
    try:
        answer = round(eval(question), 2)
    except ZeroDivisionError:
        answer = None
    return question, answer
