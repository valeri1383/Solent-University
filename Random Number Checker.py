import unittest

weight_beep = int(input("What is the weight of Beep? "))
weight_bob = int(input("What is the weight of Bob? "))
task_to_perform = input("What would you like to calculate (sum or average)?")
error_message = "Please enter valid operation"


def weight_sum(a, b):
    total = a + b
    return total


def weight_average(a, b):
    total = weight_sum(a, b) // 2
    return total


if task_to_perform == "sum":
    result = weight_sum(weight_beep, weight_bob)
elif task_to_perform == "average":
    result = weight_average(weight_beep, weight_bob)
else:
    with open("Error Log", "w") as file:
        file.write("Wrong command has been used")
    raise TypeError(error_message)

print(f"The {task_to_perform} of Beep and Bop's weight is {result}.")


# Unit Testing Scenarios
class test_weight_sum(unittest.TestCase):
    def test_sum_fuct(self):
        actual = weight_sum(5, 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_sum_all_are_digits(self):
        first_dig = 5
        sec_dig = 5
        self.assertIsInstance(first_dig, int)
        self.assertIsInstance(sec_dig, int)

    def test_sum_is_not_None(self):
        first_dig = 5
        sec_dig = 5
        self.assertIsNotNone(first_dig)
        self.assertIsNotNone(sec_dig)
