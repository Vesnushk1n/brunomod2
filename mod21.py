n1 = float(input('Введите первое число: '))
n2 = float(input('Введите второе число: '))
n3 = float(input('Введите третье число: '))
if n1 == n2 and n1 == n3:
  print('3')
elif n1 != n2 and n1 == n3 or n1 != n3 and n1 == n2 or n2 == n3 and n2 != n1:
  print('2')
elif n1 != n2 and n2 != n3:
  print('0')