from algopy import ARC4Contract, Box, Bytes, String
from algopy.arc4 import abimethod


class HelloWorld(ARC4Contract):
    def __init__(self) -> None:
        # Initialize the hello box as a bytes type
        self.hello_box = Box(Bytes, key=b'FutureHireGreeting')

    @abimethod()
    def hello(self, name: String) -> String:
        """
        This method takes a string of name, creates a greeting of "Hello, {name}" and saves to box storage.
        """

        # Initialize hello string
        hello_string = "Hello, " + name

        # Assign the hello string to the box storage
        self.hello_box.value = hello_string.bytes

        return hello_string