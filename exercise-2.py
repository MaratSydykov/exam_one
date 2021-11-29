depositbank = int(input('Сумма депозита :'))
procent = int(input('Введите сумму:'))
rate = int(input('Годовой процент:'))

month=0

while depositbank < procent:
    month=month+1
    deposit = (depositbank*(rate/100)/12)+depositbank

print(f'Количество месяцев накопления нужной суммы :{month}')
