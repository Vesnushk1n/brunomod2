l = 109 #длина МКАД
v = int(input('Введите скорость велосипедиста: ')) #Скорость
t = int(input('Введите время (в минутах), которое ехал велосипедист: ')) #Время
t1 = t / 60 #Время в системе СИ (в часах)
S = (v*t) % 109
while S > 109:
  S1 = S - 109
  print('Велосипедист остановился на',S1 ,'километре мкад')
else:
  print('Велосипедист остановился на',S ,'километре мкад')