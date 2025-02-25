
def arithmetic_arranger(problems, show_answers=False):

    num_probs = len(problems)

    if num_probs > 5:
        return 'Error: Too many problems.'

    answers = []
    first_term = []
    operator = []
    second_term = []
    line = []

    for prob in problems:
        terms = prob.split()
        t_1 = terms[0]
        op = terms[1]
        t_2 = terms[2]

        if op not in '+-':
            return "Error: Operator must be '+' or '-'."

        if not (t_1.isdigit() and t_2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(t_1) > 4 or len(t_2) > 4:
            'Error: Numbers cannot be more than four digits.'

        if len(terms) != 3:
            return 'Error: Problem not in proper format.'

        width = max(len(t_1), len(t_2)) + 2

        if show_answers:
            ans = str(eval(prob))
            answers.append(ans.rjust(width))

        first_term.append(t_1.rjust(width))
        second_term.append(op + ' ' + t_2.rjust(width - 2))
        line.append('-' * width)

    formatted = '\n'.join([
        '    '.join(first_term),
        '    '.join(second_term),
        '    '.join(line),
    ])

    if show_answers:
        formatted += '\n' + '    '.join(answers)

    return formatted
