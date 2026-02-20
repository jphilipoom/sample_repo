# Converts a prefix equation to a postfix equation

from stack_object import StackObject


def prefix_to_postfix(prefix_str):
    operators = ['$', '*', '/', '+', '-']

    # We create a stack of the prefix, so we can iterate through it in reverse order in
    # the next code block
    prefix_stack = StackObject()
    for next_char in prefix_str:
        # Reads prefix_str left to right, pushing valid characters to the stack and raising
        # warnings for invalid ones.
        if next_char in operators or (ord(next_char) >= 65 and ord(next_char) <= 90):
            prefix_stack.stack_push(next_char)
        else:
            # We are using a print statement here to avoid interrupting the program by
            # raising an error, or importing the 'warnings' module
            print(f'Warning: {repr(next_char)} is not a valid character. Please use a capital '
                  f'letter A-Z or one of \'$\', \'*\', \'/\', \'+\', or \'-\'')

    interim_stack = StackObject()
    # If the prefix stack is empty, that means there were no operators or operands,
    # this loop will be skipped, and we will output just a blank string
    while not prefix_stack.is_empty():
        # Iterates through the entire prefix stack
        next_elem = prefix_stack.stack_pop()
        if ord(next_elem) >= 65 and ord(next_elem) <= 90:
            # If the element is a capital letter A-Z, pushes it onto our iterim_stack to
            # process once we encounter an operator
            interim_stack.stack_push(next_elem)
        elif next_elem in operators and interim_stack.is_empty():
            # If we encounter operators at the back of our expression, this likely indicates
            # a postfix expression not a prefix one.
            raise ValueError(f'{prefix_str} is in an invalid format. Please ensure your input '
                             f'strings are in prefix format not postfix or infix.')
        elif next_elem in operators:
            # If the element is an operator and our stack has at least two elements, pop them
            # and combine them with the operator, then push the result back onto the stack.
            op1 = interim_stack.stack_pop()

            if interim_stack.is_empty():
                raise ValueError(f'{prefix_str} is in an invalid format. Please ensure your input '
                                 f'strings are in prefix format and there is exactly one less '
                                 f'operator than operand.')

            op2 = interim_stack.stack_pop()
            interim_stack.stack_push(op1 + op2 + next_elem)
        else:
            # In theory everything in prefix_str should have already been checked, so nothing
            # should exist that isn't caught in the above if/else, but just in case
            print(f'Warning: {repr(next_elem)} is not a valid character. Please use a capital '
                  f'letter A-Z or one of \'$\', \'*\', \'/\', \'+\', or \'-\'')

    # I put all the returns down here, even though the first could have been placed higher,
    # for readability
    if interim_stack.is_empty():
        # Returns a blank string if there were no valid characters in prefix_str
        return ''
    out = interim_stack.stack_pop()
    if interim_stack.is_empty():
        # If there is only one element in interim_stack, return it
        return out
    else:
        # If there is more than one element in interim_stack, that normally means there
        # were not enough operators
        raise ValueError(f'{prefix_str} has mismatched number of operators and operands. Please '
                         f'ensure there is exactly one less operator than operand.')
