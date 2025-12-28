
class InvalidMathOpError(Exception):
    """A custom exception for Mathematics Operation error conditions."""
    pass

while True:
    question_mathop = input("Select an operation (+, -, *, /): ") 
    try:
        if question_mathop != '+' and question_mathop != '-' and question_mathop != '*'and question_mathop != '/':
            raise InvalidMathOpError("Please enter a valid Math operator")
        
    except InvalidMathOpError as j: 
        print(f"Error:{j}")
    except KeyboardInterrupt:
        print("Program terminated by user.")
    continue


