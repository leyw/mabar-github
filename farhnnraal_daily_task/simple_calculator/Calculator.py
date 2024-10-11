class Calculator:
    def addition(self, first_number, second_number):
        return first_number + second_number
    
    def subtraction(self, first_number, second_number):
        return first_number - second_number

    def multiplication(self, first_number, second_number):
        return first_number * second_number
    
    def division(self, first_number, second_number):
        return first_number / second_number
    
calc = Calculator()

first_number = 10
second_number = 5
operation = "+"

while True:
    # first_number = float(input("First number: "))
    # second_number = float(input("Second number: "))
    # operation = str(input("What is the operation? [+, -, *, /]: "))

    if operation == "+":
        print(
            calc.addition(first_number, second_number)
        )
    
    elif operation == "-":
        print(
            calc.subtraction(first_number, second_number)
        )
    
    elif operation == "*":
        print(
            calc.multiplication(first_number, second_number)
        )
    
    elif operation == "/":
        print(
            calc.division(first_number, second_number)
        )
    
    else:
        print("There is no operation like that!")

    # restart_program = str(input("Still want to count? [Yes] "))

    # if restart_program != "Yes":
    #     break

    break