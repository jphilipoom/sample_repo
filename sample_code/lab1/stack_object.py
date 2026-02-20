# Defines a StackObject with functions is_empty, stack_push, stack_pop, and stack_peek

class StackObject:

    def __init__(self):
        # Initializes an empty list, this will be our stack object as python does not
        # have native stack objects
        self.stack = []

    def is_empty(self):
        # Returns True if empty, False if there is at least one element
        if len(self.stack) == 0:
            return True
        else:
            return False

    def stack_push(self, value):
        # Pushes a value to the top of the stack. In this implementation, appends to
        # the end of the list object, which is also the end we read from
        self.stack.append(value)
        return

    def stack_pop(self):
        # Checks if the stack is empty, raises an error if it is
        # Otherwise, removes last element (top of stack) and returns its value
        if StackObject.is_empty(self):
            raise TypeError("Cannot pop from an empty stack.")
        out_value = self.stack[-1]
        self.stack = self.stack[0:-1]
        return out_value

    def stack_peek(self):
        # Checks if the stack is empty, raises an error if it is
        # Otherwise, returns last element, leaves the stack unchanged
        if StackObject.is_empty(self):
            raise TypeError("Cannot pop from an empty stack.")
        return self.stack[-1]
