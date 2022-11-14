def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    direction = directions()
    for i in range(len(direction)):
        print(f"{i}: {direction[i]}")
    user_direction = int(input())
    return direction[user_direction]


def run():
    route = []
    print("Working out escape route...\n")
    for i in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


run()


'''"We wish to create a variation of our previous program to help Beep and Bop escape the cave.
The program should consist of the following three functions:

The first function should be named directions and should have no parameters.
The function should create a list named directions.
The function should populate the list with the following items: "Move Forward", "Move Backward", "Turn Left" and "Turn Right". 
Finally, the function should return the list directions.

The second function should be named menu and should have no parameters.
The function should start by displaying the message "Please select a direction:".
The function should then call the first function and store the returned list in a local variable
The function should then use a loop to display each direction in the list with an index number.  This should be displayed in the format "{index}: {direction}" where {index} is the index number of the list and {direction} is the direction from the list.
The function should then read in the user's response.
Finally, the function should return the direction corresponding to user's response.
The third function should be named run and should have no parameters.
The function should create an empty list named route.
The function should start be displaying the message "Working out escape route...".
The function should then use a loop to do the following 5 times:
    Call the function menu and append the returned direction to the list route.
Finally, the function should display the message "Escape route: {route}" where {route} is the content of the list route."
'''