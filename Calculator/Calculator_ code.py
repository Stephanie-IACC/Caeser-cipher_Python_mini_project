import os
import time
import sys
import calc_art

im_logo = calc_art.logo
class InvalidAnswerError(Exception):
    """A custom exception for Answer error conditions."""
    pass
class InvalidMathOpError(Exception):
    """A custom exception for Mathematics Operation error conditions."""
    pass
class ZeroDivisionError(Exception):
    """A custom exception for denominator being zero."""
    pass
def slow_print(text, delay=0.03):
    """Prints text slowly, character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces immediate printing to the console
        time.sleep(delay)
    print()  # Print a newline at the end

def slow_art_print(art_string, line_delay=0.1, char_delay=0.01):
    """Prints ASCII art slowly, line by line and character by character."""
    lines = art_string.splitlines()
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()  # Move to the next line after the line is complete
        time.sleep(line_delay)

def calculator_ascii_art():
    """Displays the calculator ASCII art slowly."""
    slow_art_print(im_logo)

def calc_main():
    ''' Math operators in dictionary'''
    math_operator = {
        "Subtraction": "-",
        "Addition": "+",
        "Multiplication": "*",
        "Division": "/",
        "Bracket":"()",
    }

    """Main function for the slow ASCII art calculator."""
    slow_print("Starting up the ASCII Calculator...", delay=0.05)
    calculator_ascii_art()
    slow_print("\nWelcome to the simple Python calculator.")

    current_number = 0
    while True:
        try:
            question1 = float(input("Enter a number:\n"))
        except ValueError:
            slow_print("Error:Ooops, Data must be a float or an integer. Try again")
            continue

        while True:
            while True: 
                question_mathop = input("Select an operation (+, -, *, /): ") 
                try:
                    if question_mathop != '+' and question_mathop != '-' and question_mathop != '*' and question_mathop != '/':
                        raise InvalidMathOpError("Please enter a valid Math operator")
                except InvalidMathOpError as j: 
                    print(f"Error:{j}")              
                    continue       
                    
                while True:  
                    if math_operator.get("Addition",None) == question_mathop:
                        current_number1 = current_number + question1                               
                        print(f"{current_number} {question_mathop} {question1} = {current_number1}")
                        current_number = current_number + question1
                        break

                    elif math_operator.get("Subtraction",None) == question_mathop:
                        print(question_mathop)
                        current_number1 = current_number - question1                               
                        print(f"{current_number} {question_mathop} {question1} = {current_number1}")                        
                        current_number = current_number - question1
                        break

                    elif math_operator.get("Multiplication",None) == question_mathop:
                        current_number1 = current_number * question1                               
                        print(f"{current_number} {question_mathop} {question1} = {current_number1}")
                        current_number = current_number * question1
                        break

                    elif math_operator.get("Division",None) == question_mathop:
                        try:
                            if question1 == 0:                                        
                                raise ZeroDivisionError("Cannot divide by zero")
                            
                            else:
                                current_number1 = current_number / question1                               
                                print(f"{current_number} {question_mathop} {question1} = {current_number1}")
                                current_number = current_number / question1 
                                break   
                        except ZeroDivisionError as i:
                            slow_print(f"Error:{i}")
                            print(f"{current_number} {question_mathop} {question1} = undefined")
                            break
               
                break    
            break

        question3 = input("Do you want to continue or start afresh? Y or N?\n").strip().upper()
        try:
            if question3 == "Y":
                continue
            
            elif question3 == "N":
                os.system('cls')
                continue
            else:
                raise InvalidAnswerError("Please enter a valid answer")
        except InvalidAnswerError as k:
            slow_print(f"Error:{k}")

        continue

if __name__ == "__main__":
    calc_main()