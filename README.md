# Calc_app.py

## Overview

**Calc_app.py** is a simple command-line calculator application written in Python. It allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division. The results of these calculations are saved to a file called `equations.txt` for future reference.

## Features

- **Addition, Subtraction, Multiplication, Division**: Perform basic arithmetic operations.
- **Result Logging**: All calculations are automatically saved in `equations.txt`.
- **View Past Equations**: Users can view all previously saved equations.
- **Error Handling**: Includes basic error handling for invalid inputs and division by zero.

## Usage

### Running the Program

1. Run the `Calc_app.py` file in your terminal or command prompt:

   
   python3 Calc_app.py

Follow the on-screen prompts:

Option 1: Perform a new calculation.
Option 2: View previously saved calculations.
Option 3: Exit the program.

Sample Interaction

Welcome to Calc_app.py, Please choose an option below to continue:
1 to calculate new equations.
2 to view previous equations.
3 to exit.

Enter the number of which you wish to proceed : 1
Please enter your first number : 5
Please enter an operator [+ to add - to minus * to multiply / to divide : ] +
Please enter your second number : 10

5 + 10 = 15

Welcome to Calc_app.py, Please choose an option below to continue:
1 to calculate new equations.
2 to view previous equations.
3 to exit.

Enter the number of which you wish to proceed : 2
Previous equations : 

5 + 10 = 15

Welcome to Calc_app.py, Please choose an option below to continue:
1 to calculate new equations.
2 to view previous equations.
3 to exit.

File Structure
Calc_app.py: The main Python script containing all the logic for the calculator.
equations.txt: A text file where all the results of the calculations are saved. This file is created automatically when the first calculation is made.

Error Handling
Invalid Number Input: The program will prompt the user to enter a valid number if the input is invalid.
Invalid Operator Input: The program will prompt the user to enter a valid operator (+, -, *, /).
Division by Zero: If the user attempts to divide by zero, the program will catch the error and notify the user.
File Not Found: If equations.txt does not exist when trying to view past equations, the program will handle the error gracefully.

Requirements
Python 3.x