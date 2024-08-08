# Create function to calculate with +.
def addition():
    result = num1 + num2 

    # Open file equations.txt.
    with open("equations.txt", "a") as file:
        # Write result to file.
        file.write(f"\n{num1} + {num2} = {result}")

    # Print result to user.
    print(f"\n{num1} + {num2} = {result}\n")

# Create function to calculate with -.
def minus():
    result = num1 - num2

    # Open file, write data to file.
    with open("equations.txt", "a") as file:
        file.write(f"\n{num1} - {num2} = {result}")

    # Print result to user.
    print(f"{num1} - {num2} = {result}\n")

# Create function to calculate with *.
def multiply():
    result = num1 * num2

    # Open file, write data to file.
    with open("equations.txt", "a") as file:
        file.write(f"\n{num1} * {num2} = {result}")

    # Print result to user.
    print(f"{num1} * {num2} = {result}\n")

# Create function to calculate with /.
def divide():

    # Try block to catch error.
    try:
        result = num1 / num2

        # Open file, write data to file.
        with open("equations.txt", "a") as file:
            file.write(f"\n{num1} / {num2} = {result:.2f}")

        # Print result to user.
        print(f"{num1} / {num2} = {result:.2f}\n")

    # Exception to catch dividion by zero error.
    except Exception:
        print("Zero division error!\nCannot divide by 0\n")


# Start loop for user entry.
while True:

    # Print menu options to user.
    print("Welcome to Calc_app.py, Please choose an option below to continue:")
    print("1 to calculate new equations.\n2 to view previous equations.\n3 to exit.\n")

    # Try block to catch unexpected errors.
    try:
        # Request user to choose from menu options.
        user_choice = int(input("Enter the number of which you wish to proceed : "))

        # If user chooses 1 next loop starts.
        if user_choice == 1:

            # Try block to catch user errors.
            try:
                # Request first number of equation from user.
                num1 = int(input("Please enter your first number : "))

                # Request operator for equation from user.
                operation= input("Please enter an operator [+ to add - to minus * to multiply / to divide : ]")

                # Start loop for different operator choices.
                if operation in ("+", "-", "*", "/"):
                
                    # Try block to catch user errors.
                    try:
                        # Request second number of equation from user.
                        num2 = int(input("Please enter your second number : "))
                        print()
                    
                        # Call function for + equation.
                        if operation == "+":
                            addition()
                    
                        # Call function for - equation.
                        elif operation == "-":
                            minus()

                        # Call function for * equation.
                        elif operation == "*":
                            multiply()

                        # Call function for / equation.
                        elif operation == "/":
                            divide()
                   
                    # Error message if user does not enter a valid number.
                    except ValueError:
                        print("Invalid entry, Please enter a number.\n")

                # Error message if user didn't enter a valid operator. 
                else:
                    print("Invalid option please enter one of the following opperators [+, -, *, /]\n")

            # Error message if user does not enter a valid number.
            except ValueError:
                print("Invalid entry, Please enter a number\n")

        # If user chooses 2 from menu options.
        elif user_choice == 2:

            # Try block to catch File not found error.
            try:
                # Open file and read through data.
                with open("equations.txt", "r") as file:
                
                    # Print title to user.
                    print("Previous equations : \n")

                    # Print extracted data from file to user.
                    for line in file:
                        print(line.strip())
                        print()

            # Error message if file does not exist.            
            except FileNotFoundError:
                print("File does not exist!")

        # If user chooses 3 from menu options.
        elif user_choice == 3:

            # Print sign off message to user.
            print("Goodbye!!!\n")
            # Break code to exit.
            break

        # Error message if user does not enter a valid menu option.
        else:
            print("Invalid entry , please try again.\n")
     
    # ValueError message if user enters incorrectly.    
    except Exception:
        print("Invalid entry, Enter a number from the options above, Please try again... ")
    
# End code.
           