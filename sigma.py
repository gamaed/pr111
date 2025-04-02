def kvitok(level, v):
    k = int(input('Скільки продано квитків класу ' + level + ': '))
    suma = v * k
    return suma

a = int(input('Вартість квитка класу A: '))
b = int(input('Вартість квитка класу B: '))
c = int(input('Вартість квитка класу C: '))

s_a = kvitok('A', a)
s_b = kvitok('B', b)
s_c = kvitok('C', c)

suma = s_a + s_b + s_c
print('Загальна сума', suma, 'грн')
