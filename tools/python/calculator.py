def main(args):
    num1 = int(args[0])
    num2 = int(args[1])
    operation = args[2]
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    else:
        raise ValueError("Invalid operation")
    print(result)
