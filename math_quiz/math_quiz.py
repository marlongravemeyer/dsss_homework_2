import random


def randomInt(min, max):
    """
    Compute a random integer.

    Args:
        min (int): Infimum of the random number.
        max (int): Supremum of the random number.

    Returns:
        int: Random integer N such that a <= N <= b.
    """
    # Check if input of min and max is valid
    if not isinstance(min, int):
        raise TypeError(f"Argument 'min' must be of type int, but got {type(min).__name__}")
    if not isinstance(max, int):
        raise TypeError(f"Argument 'min' must be of type int, but got {type(max).__name__}")

    return random.randint(min, max)


def randomMathOperand():
    """
        Compute a random math operand (+, -, *).

        Returns:
            str: Random math operand.
        """
    return random.choice(['+', '-', '*'])


def mathQuiz(firstNumber, secondNumber, operand):
    """
        Compute a math quiz by defining a math problem and the corresponding solution.

        Args:
            firstNumber (int): First number of the math quiz.
            secondNumber (int): Second number of the math quiz.
            operand (str): Math operand.

        Returns:
            tuple: The math problem (str) and the corresponding solution (int).
        """
    # Define the Math Problem as a string
    problem = f"{firstNumber} {operand} {secondNumber}"

    # Compute the solution depending on the operand
    if operand == '+':
        solution = firstNumber + secondNumber
    elif operand == '-':
        solution = firstNumber - secondNumber
    else:
        solution = firstNumber * secondNumber
    return problem, solution


def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        # Compute the necessary numbers and the operand for the math quiz
        firstNumber = randomInt(1, 10)
        secondNumber = randomInt(1, 5.5)
        operand = randomMathOperand()

        # Compute the problem and answer to the math quiz
        problem, answer = mathQuiz(firstNumber, secondNumber, operand)

        # Print Problem in terminal
        print(f"\nQuestion: {problem}")
        # Get user answer
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        # Check if answer is correct and increase score if it is
        if useranswer == answer:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # End game and print final score
    print(f"\nGame over! Your score is: {s}/{t_q}")


if __name__ == "__main__":
    math_quiz()
