print('Приветствую в  калькулятор!')
print('Доступные нам операции:')
print('1. Арифметические операторы: +, -, *, /, //, %, ** (возведение в степень)')
print('2. Операторы сравнения: ==, !=, >, <, >=, <=')
print('3. Логические операторы: and, or')
print('4. Побитовые операторы: &, |, ^, ~, <<, >>')
print('5. Операторы принадлежности: in, not in')
print('6. Операторы тождественности: is, is not')

act = input('Введите действие: ')

if act in ['+', '-', '*', '/', '//', '%', '**']:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    if act == '+':
        print(f'Результат: {num1+ num2}')
    elif act == '-':
        print(f'Результат: {num1 - num2}')
    elif act == '*':
        print(f'Результат: {num1 * num2}')
    elif act == '/':
        if num2 != 0:
            print(f'Результат: {num1 / num2}')
        else:
            print('Ошибка: Деление на ноль невозможно!')
    elif act == '//':
        if num2 != 0:
            print(f'Результат: {num1 // num2}')
        else:
            print('Ошибка: Деление на ноль невозможно!')
    elif act == '%':
        print(f'Результат: {num1 % num2}')
    elif act == '**':
        print(f'Результат: {num1 ** num2}')

elif act in ['==', '!=', '>', '<', '>=', '<=']:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    if act == '==':
        print(f'Результат: {num1 == num2}')
    elif act == '!=':
        print(f'Результат: {num1 != num2}')
    elif act == '>':
        print(f'Результат: {num1 > num2}')
    elif act == '<':
        print(f'Результат: {num1 < num2}')
    elif act == '>=':
        print(f'Результат: {num1 >= num2}')
    elif act == '<=':
        print(f'Результат: {num1 <= num2 }')

elif act in ['and', 'or']:
    num1 = int(input('Введите первое целое число: '))
    num2 = int(input('Введите второе целое число: '))
    num1_bool = bool(num1)
    num2_bool = bool(num2)
    if act == 'and':
        print(f'Результат: {num1_bool and num2_bool}')
    else:
        print(f'Результат: {num1_bool or num2_bool}')

elif act in ['&', '|', '^', '<<', '>>']:
    num1 = int(input('Введите первое целое число: '))
    num2 = int(input('Введите второе целое число: '))
    if act == '&':
        print(f'Результат: {num1 & num2}')
    elif act == '|':
        print(f'Результат: {num1 | num2}')
    elif act == '^':
        print(f'Результат: {num1 ^ num2}')
    elif act == '<<':
        print(f'Результат: {num1 << num2}')
    elif act == '>>':
        print(f'Результат: {num1 >> num2}')

elif act == '~':
    num1 = int(input('Введите целое число: '))
    print(f'Результат побитового NOT: {~num1}')

elif act in ['in', 'not in']:
    numbers = input("Введите числа через пробел: ").split()
    numbers = [int(n) for n in numbers]
    num2 = int(input("Введите число для проверки: "))
    if act == 'in':
        print(f'Число {num2} {"входит" if num2 in numbers else "не входит"} в список.')
    else:
        print(f'Число {num2} {"не входит" if num2 not in numbers else "входит"} в список.')

elif act in ['is', 'is not']:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    if act == 'is':
        print(f'Результат (сравнение идентичности): {num1 is num2}')
    else:
        print(f'Результат (сравнение идентичности): {num1 is not num2}')

else:
    print(' Данная операция не поддерживается.')
    
print('Спасибо за использование калькулятора!')