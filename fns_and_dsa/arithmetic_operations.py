def perform_operation(num1, num2, operation):
    if operation == 'add':
        add = num1 + num2
        return add
    elif operation == 'subtract':
        subtract = num1 - num2
        return subtract
    elif operation == 'multiply':
        multiply = num1 * num2
        return multiply
    elif operation == 'divide':
        if num2 == 0:
            return "you can't divide by 0"
        else:
            divide = num1 / num2
            return divide
    else:
        return "Invalid operation"

