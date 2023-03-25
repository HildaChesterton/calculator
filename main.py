from input_handler import get_input
from calculator import calculate
from output_handler import display_result

if __name__ == '__main__':
    expression = get_input()
    result = calculate(expression)
    display_result(result)
