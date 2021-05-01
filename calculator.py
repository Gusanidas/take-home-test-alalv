operations = {
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "/": lambda a, b: a/b,
    "*": lambda a, b: a*b}

digits = set([str(i) for i in range(10)])

incorrect_input_message = "Incorrect Input Format"


def eval_prefix_subexpr(expr: str, index: int) -> tuple[int, int]:
    if index >= len(expr):
        raise ValueError(incorrect_input_message)
    if expr[index] in operations:
        op = operations[expr[index]]
        first_term, last_index = eval_prefix_subexpr(expr, index+2)
        second_term, last_index = eval_prefix_subexpr(expr, last_index+2)
        return op(first_term, second_term), last_index
    else:
        return read_number(expr, index)


def eval_infix_subexpr(expr: str, index: int) -> tuple[int, int]:
    if index >= len(expr):
        raise ValueError(incorrect_input_message)
    if expr[index] == "(":
        first_term, last_index = eval_infix_subexpr(expr, index+2)
        op = operations[expr[last_index+2]]
        second_term, last_index = eval_infix_subexpr(expr, last_index+4)
        return op(first_term, second_term), last_index+2
    else:
        return read_number(expr, index)


def read_number(expr: str, index: int) -> tuple[int, int]:
    if index >= len(expr):
        raise ValueError(incorrect_input_message)
    start = index
    while index < len(expr) and expr[index] in digits:
        index += 1
    return int(expr[start:index]), index-1


def eval_prefix_expr(expr: str) -> int:
    total, last_index = eval_prefix_subexpr(expr, 0)
    if last_index != len(expr)-1:
        raise ValueError(incorrect_input_message)
    return total


def eval_infix_expr(expr:str) -> int:
    total, last_index = eval_infix_subexpr(expr, 0)
    if last_index != len(expr)-1:
        raise ValueError(incorrect_input_message)
    return total
