class Calculator:
    # Constructor
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    # Method for input1 + input2
    def adder(self):
        return input1 + input2

    # Method for input1 - input2
    def subtractor(self):
        return input1 - input2

    # Method for input1 * input2
    def multiplier(self):
        return input1 * input2

    # Method for input1 / input2
    def divider(self):
        return input1 // input2

    # Reset input 1 and input 2 to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0
        return self.input1, self.input2


if __name__ == '__main__':
    # User to input hours, minutes and seconds
    input1 = int(input("Enter a value for input1: "))
    input2 = int(input("Enter a value for input2: "))

    # Create Calculator object
    c = Calculator(input1, input2)

    # Call methods to calculate and return values
    print("input1 + input2 = " + str(c.adder()))
    print("input1 - input2 = " + str(c.subtractor()))
    print("input1 * input2 = " + str(c.multiplier()))
    print("input1 / input2 = " + str(c.divider()))

    # Call method reset values to 0
    print("input1 and input2 reset to 0: " + str(c.clear()))
