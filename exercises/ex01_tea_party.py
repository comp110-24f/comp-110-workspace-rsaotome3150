"""This program will help me plan a tea party where I will be able to calculate quantity of tea bags, treats, and expected costs"""

__author__: str = "730770150"


def main_planner(guests: int) -> None:
    """main_planner function gathers all of the functions listed below into one."""
    print("A Cozy Tea Party for " + str(guests), "People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# this gathers all function we created into one
# on top because it's the main function we gonna use


def tea_bags(people: int) -> int:
    """tea_bags function defines how many tea bags needed. 2 tea bags per person is needed."""
    return people * 2


# 2 teabags per person so multiplied by two


def treats(people: int) -> int:
    """treats function calculates the number of treats needed based on the number of teas guest are going to drink"""
    return int(tea_bags(people=people) * 1.5)


# treats equal 1.5 times per people.
# int() used to change float to integer because you cant order a decimal point amount of treats. Has to be rounded or an integer


def cost(tea_count: int, treat_count: int) -> float:
    """cost function will allow you to calculate the cost based on the amount of tea and treat"""
    return tea_count * 0.50 + treat_count * 0.75


# 1 tea = 50 cents, 1 treat = 75 cents


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

# allows the function to run on trailhead by asking the question and we put the number in
# on bottom so we allow the function to be read and used chronologically speaking
