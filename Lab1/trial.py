"""
trial.py - Demonstrates Python basics for Lab Assignment 1.
Includes variables, functions, loops, classes, and Pylint workflow testing.
"""

NAME = "Alice"
AGE = 25


def greet_user(user_name: str) -> str:
    """
    Return a greeting message for the given name.

    Args:
        user_name (str): The name of the user.

    Returns:
        str: Greeting message including the user's name and age.
    """
    return f"Hello, {user_name}! You are {AGE} years old."


def arithmetic_operations(num1: int, num2: int) -> None:
    """
    Perform basic arithmetic operations on two numbers and print the results.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    """
    print("Sum:", num1 + num2)
    print("Difference:", num2 - num1)
    print("Product:", num1 * num2)
    print("Division:", num2 / num1)


def display_fruits(fruit_list: list) -> None:
    """
    Display the list of fruits.

    Args:
        fruit_list (list): A list of fruits to display.
    """
    print("\nFruits list:")
    for fruit in fruit_list:
        print(f"- {fruit}")


class Animal:
    """Represent an animal with a name and a sound."""

    def __init__(self, animal_name: str, sound: str) -> None:
        """
        Initialize the Animal class.

        Args:
            animal_name (str): The name of the animal.
            sound (str): The sound the animal makes.
        """
        self.animal_name = animal_name
        self.sound = sound

    def make_sound(self) -> None:
        """Print the sound of the animal."""
        print(f"The {self.animal_name} says {self.sound}!")

    def change_name(self, new_name: str) -> None:
        """
        Change the name of the animal.

        Args:
            new_name (str): The new name of the animal.
        """
        self.animal_name = new_name
        print(f"The animal's name has been changed to {self.animal_name}.")


if __name__ == "__main__":
    print(greet_user(NAME))

    # Perform arithmetic operations
    NUM1, NUM2 = 10, 20
    arithmetic_operations(NUM1, NUM2)

    # Display fruits
    FRUITS = ["apple", "banana", "cherry"]
    display_fruits(FRUITS)

    # Demonstrate class usage
    dog = Animal("dog", "woof")
    dog.make_sound()

    # Changing the animal's name
    dog.change_name("puppy")
    dog.make_sound()
