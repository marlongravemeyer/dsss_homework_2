import unittest
from math_quiz import randomInt, randomMathOperand, mathQuiz


class TestMathGame(unittest.TestCase):

    def test_randomInt(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomMathOperand(self):
        # Test if random operands generated are +, -, *
        for _ in range(1000):  # Test a large number of random values
            rand_operand = randomMathOperand()
            self.assertTrue(rand_operand in ['+', '-', '*'])

    def test_mathQuiz(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (5, 7, '+', '5 + 7', 12),
                (5, 7, '-', '5 - 7', -2),
                (5, 7, '*', '5 * 7', 35)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = mathQuiz(num1, num2, operator)
                self.assertEqual(expected_problem, problem)
                self.assertEqual(expected_answer, answer)


if __name__ == "__main__":
    unittest.main()
