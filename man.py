
def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_lines = []
    bottom_lines = []
    dash_lines = []
    result_lines = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(operand1), len(operand2))
        width = max_len + 2

        top_line = operand1.rjust(width)
        bottom_line = operator + ' ' + operand2.rjust(max_len)
        dash_line = '-' * width

        top_lines.append(top_line)
        bottom_lines.append(bottom_line)
        dash_lines.append(dash_line)

        if display_answers:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            result_str = str(result).rjust(width)
            result_lines.append(result_str)

    arranged = []
    arranged.append('    '.join(top_lines))
    arranged.append('    '.join(bottom_lines))
    arranged.append('    '.join(dash_lines))

    if display_answers:
        arranged.append('    '.join(result_lines))

    return '\n'.join(arranged)
