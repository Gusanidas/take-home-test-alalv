"""
Python Module for the prefix and infix calculator.
"""

from typing import Callable

operations = {
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "/": lambda a, b: a/b,
    "*": lambda a, b: a*b}

digits = set([str(i) for i in range(10)])

incorrect_input_message = "Incorrect Input Format"

def eval_prefix_expr(expr: str) -> int:
    """ Evaluates a prefix formated expression"""
    total, last_index = _eval_prefix_subexpr(expr, 0)
    if last_index != len(expr)-1:
        raise ValueError(incorrect_input_message)
    return total


def eval_infix_expr(expr: str) -> int:
    """ Evaluates a infix formated expression"""
    total, last_index = _eval_infix_subexpr(expr, 0)
    if last_index != len(expr)-1:
        raise ValueError(incorrect_input_message)
    return total


def compute(expr: str, func: Callable) -> str:
    """
    Evaluates an expression with the appropiate function.
    If there is a value error, returns the error message.
    """
    try:
        output = func(expr)
        return str(output)
    except ValueError as e:
        return str(e)


def interactive():
    """
    Function for the command line, will read standard input and try to compute it as an expression.
    The format to be used can be changed by printing either "Prefix" or "Infix"
    """
    formats = ["Prefix", "Infix"]
    format_index = 1
    while True:
        print("Current reading format is {}, to change enter {}".format(formats[format_index], formats[(format_index+1)%2]))
        inp = input("Enter input:")
        if inp in formats:
            if inp!=formats[format_index]:
                format_index = (format_index+1)%2
        else:
            if format_index>0:
                output = compute(inp, eval_infix_expr)
            else:
                output = compute(inp, eval_prefix_expr)
            print("Output: ", output)


def _eval_prefix_subexpr(expr: str, index: int) -> tuple[int, int]:
    if index >= len(expr):
        raise ValueError(incorrect_input_message)
    if expr[index] in operations:
        op = operations[expr[index]]
        first_term, last_index = _eval_prefix_subexpr(expr, index+2)
        second_term, last_index = _eval_prefix_subexpr(expr, last_index+2)
        return op(first_term, second_term), last_index
    else:
        return _read_number(expr, index)


def _eval_infix_subexpr(expr: str, index: int) -> tuple[int, int]:
    if index >= len(expr):
        raise ValueError(incorrect_input_message)
    if expr[index] == "(":
        first_term, last_index = _eval_infix_subexpr(expr, index+2)
        op = operations[expr[last_index+2]]
        second_term, last_index = _eval_infix_subexpr(expr, last_index+4)
        return op(first_term, second_term), last_index+2
    else:
        return _read_number(expr, index)


def _read_number(expr: str, index: int) -> tuple[int, int]:
    if index >= len(expr):
        raise ValueError(incorrect_input_message)
    start = index
    while index < len(expr) and expr[index] in digits:
        index += 1
    try:
        number = int(expr[start:index])
    except Exception:
        raise ValueError(incorrect_input_message)
    return number, index-1

            
if __name__ == "__main__":
    interactive()
                
            
            
            
            
        
    
