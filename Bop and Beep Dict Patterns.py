def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    print("Analysing patterns...")
    results = {}
    results["short sequence"] = short_pattern()
    results["medium sequence"] = medium_pattern()
    results["long sequence"] = long_pattern()

    for k, v in results.items():
        print(f"{k}: {v}")


run()


# Solution with Class
class Paterns():
    def __init__(self,name, sequence, occurrences):
        self.name = name
        self.sequence = sequence
        self.occurrences = occurrences

    def __str__(self):
        return f"{self.name}: {self.sequence}=> {self.occurrences} "


short_pattern = Paterns("short", 101, 5)
medium_pattern = Paterns("medium", 111000, 25)
long_pattern = Paterns("long", 1100110011001100, 50)

list_patterns = [short_pattern, medium_pattern, long_pattern]

print([x.__str__() for x in list_patterns])


# Task Requarments
'''We wish to create a program to help Beep and Bop identify the patterns.

The program should consist of the following four functions:
The first function should be named short_pattern and should have no parameters.
The function should create a dictionary named pattern.
The function should populate the dictionary with the following key-value pairs:
"sequence":"101"
"occurrences":5
Finally, the function should return the dictionary.

The second function should be named medium_pattern and should have no parameters.
The function should create a dictionary named pattern.
The function should populate the dictionary with the following key-value pairs:
"sequence":"111000"
"occurrences": 25
Finally, the function should return the dictionary

The third function should be named long_pattern and should have no parameters.
The function should create a dictionary named pattern.
The function should populate the dictionary with the following key-value pairs:
"sequence":"1100110011001100"
"occurrences":50
The fourth function should be named run and should have no parameters.
The function should start by displaying the message "Analysing patterns...".
The function should then create a dictionary with the following key-value pairs:
"short sequence": value returned from first function
"medium sequence": value returned from second function
"long sequence": value returned from third function
Finally, the function should display the content of the dictionary as key-value pairs using an appropriate loop

'''