# Asks user for operand values and solves the postfix equation

from stack_object import StackObject


def get_values(operand, postfix_str):
    op_val = input(f"For {postfix_str}, {operand}=")

    try:
        op_val = float(op_val)
    except ValueError:
        print(f'Please enter a float or integer.')
        op_val = input(f"For {postfix_str}, {operand}=")
        op_val = float(op_val)

    return op_val


def postfix_solver(postfix_str):
    operators = ['$', '*', '/', '+', '-']

    values = dict()
    solver_stack = StackObject()
    for next_char in postfix_str:
        if ord(next_char) >= 65 and ord(next_char) <= 90:
            solver_stack.stack_push(next_char)
        elif solver_stack.is_empty():
            raise ValueError(f'{postfix_str} is in an invalid format. Please ensure it is in '
                             f'postfix format.')
        elif next_char in operators:
            op1 = solver_stack.stack_pop()

            if solver_stack.is_empty():
                raise ValueError(f'{postfix_str} is in an invalid format. Please ensure it is in '
                                 f'postfix format.')

            op2 = solver_stack.stack_pop()

            if type(op1) == float:
                op1_val = op1
            elif op1 not in values:
                op1_val = get_values(op1, postfix_str)
                values[op1] = op1_val

            if type(op2) == float:
                op2_val = op2
            elif op2 not in values:
                op2_val = get_values(op2, postfix_str)
                values[op2] = op2_val

            if next_char == '$':
                ans = op2_val ** op1_val
            elif next_char == '*':
                ans = op2_val * op1_val
            elif next_char == '/':
                ans = op2_val / op1_val
            elif next_char == '+':
                ans = op2_val + op1_val
            elif next_char == '-':
                ans = op2_val - op1_val

            solver_stack.stack_push(ans)

    if solver_stack.is_empty():
        raise ValueError(f'{postfix_str} is in an invalid format. Please ensure there are'
                         f'operators and operands present')
    out_value = solver_stack.stack_pop()
    if solver_stack.is_empty():
        return str(out_value)
    else:
        raise ValueError(f'{postfix_str} has mismatched number of operators and operands. Please '
                         f'ensure there is exactly one less operator than operand.')
