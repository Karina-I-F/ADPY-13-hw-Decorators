from logger import logger


@logger('/home/karina/PycharmProjects/ADPY-13-hw-Decorators/')
def polish_notation(operator, operand1, operand2):
    """
    Принимает выражение в Польской нотации для двух положительных чисел
    """
    assert operator in ['+', '-', '*', '/'], 'Вы ввели неверную операцию'
    try:
        if float(operand1) > 0 and float(operand2) > 0:
            if operator == '+':
                return float(operand1) + float(operand2)
            elif operator == '-':
                return float(operand1) - float(operand2)
            elif operator == '*':
                return float(operand1) * float(operand2)
            elif operator == '/':
                return float(operand1) / float(operand2)
        else:
            return 'Введите положительные числа.'
    except ValueError:
        return 'Вы ввели строку вместо числа.'


if __name__ == '__main__':
    prefix_notation = input('Введите выражение в Польской нотации: ').split()

    try:
        result = polish_notation(*prefix_notation)
    except TypeError:
        print('Введено недопустимое количество аргументов. '
              'Введите оператор и два операнда через пробел.')
    else:
        print(result)
