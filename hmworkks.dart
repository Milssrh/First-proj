import 'dart:io';
import 'dart:math';

void main() {
  print('Калькулятор');
  print('Доступные операции:');
  print('+ : Сложение');
  print('- : Вычитание');
  print('* : Умножение');
  print('/ : Деление');
  print('~/ : Целочисленное деление');
  print('% : Остаток от деления');
  print('pow : Возведение в степень (pow)');
  print('== : Равно');
  print('!= : Не равно');
  print('> : Больше');
  print('< : Меньше');
  print('>= : Больше или равно');
  print('<= : Меньше или равно');
  print('&& : Логическое И');
  print('|| : Логическое ИЛИ');
  print('! : Логическое НЕ');
  print('');

  stdout.write('Введите операцию: ');
  String? operation = stdin.readLineSync();

  dynamic num1, num2;
  
  if (operation != null && operation.isNotEmpty) {
    switch (operation) {
      case '+':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          print('Результат: ${num1 + num2}');
        }
        break;
        
      case '-':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          print('Результат: ${num1 - num2}');
        }
        break;
        
      case '*':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          print('Результат: ${num1 * num2}');
        }
        break;
        
      case '/':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num2 != 0) {
            print('Результат: ${num1 / num2}');
          } else {
            print('Ошибка: Деление на ноль!');
          }
        }
        break;
        
      case '~/':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num2 != 0) {
            print('Результат: ${num1 ~/ num2}');
          } else {
            print('Ошибка: Деление на ноль!');
          }
        }
        break;
        
      case '%':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num2 != 0) {
            print('Результат: ${num1 % num2}');
          } else {
            print('Ошибка: Деление на ноль!');
          }
        }
        break;
        
      case 'pow':
        stdout.write('Введите число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите степень: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          print('Результат: ${pow(num1, num2)}');
        }
        break;
        
      case '==':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num1 == num2) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '!=':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num1 != num2) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '>':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num1 > num2) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '<':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num1 < num2) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '>=':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num1 >= num2) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '<=':
        stdout.write('Введите первое число: ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число: ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = double.tryParse(input1) ?? 0;
          num2 = double.tryParse(input2) ?? 0;
          if (num1 <= num2) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '&&':
        stdout.write('Введите первое число (0 = false, другое = true): ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число (0 = false, другое = true): ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = int.tryParse(input1) ?? 0;
          num2 = int.tryParse(input2) ?? 0;
          if (num1 != 0 && num2 != 0) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '||':
        stdout.write('Введите первое число (0 = false, другое = true): ');
        String? input1 = stdin.readLineSync();
        stdout.write('Введите второе число (0 = false, другое = true): ');
        String? input2 = stdin.readLineSync();
        if (input1 != null && input2 != null) {
          num1 = int.tryParse(input1) ?? 0;
          num2 = int.tryParse(input2) ?? 0;
          if (num1 != 0 || num2 != 0) {
            print('Результат: true');
          } else {
            print('Результат: false');
          }
        }
        break;
        
      case '!':
        stdout.write('Введите число (0 = false, другое = true): ');
        String? input = stdin.readLineSync();
        if (input != null) {
          num1 = int.tryParse(input) ?? 0;
          if (num1 == 0) {
            print('Результат: true');  // !false = true
          } else {
            print('Результат: false'); // !true = false
          }
        }
        break;
        
      default:
        print('Неизвестная операция!');
    }
  } else {
    print('Операция не введена!');
  }
  
  print('\n Спасибо за использование калькулятора!');
}