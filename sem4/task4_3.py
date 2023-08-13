"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список
"""

log_dct = {}
opper_count = 0
balance = 20000

def menu():
    print('*' * 20)
    print(f'Баланс: 1')
    print(f'Снятие наличных: 2')
    print(f'Внесение наличных: 3')
    print(f'История операций: 4')
    print(f'Выход: 0')
    print('*' * 20)

def log(log_dct, bool, opperation_count, cash):
    if bool:
        log_dct[opperation_count] = f'Внесено {cash}'
    else:
        log_dct[opperation_count] = f'Снято {cash}'
    return log_dct

def take_money(balance, opperation_count):
    print_balance(balance)
    rich_comission(balance)
    summ_out = int(input("Введите сумму снятия: "))
    comission = summ_out * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600
    if summ_out + comission >= balance:
        print("Недостаточно средств.")
        print(print_balance(balance))
    else:
        if summ_out % 50 == 0:
            balance -= summ_out + comission
            opperation_count += 1
            if opperation_count % 3 == 0:
                balance *= 1.03
        else:
            print("Введена некорректная сумма.")
    log(log_dct, False, opperation_count, summ_out)
    return balance, opperation_count

def put_money(balance, opperation_count):
    while True:
        if opperation_count % 3 == 0:
            balance *= 1.03
        print(f'Сколько хотите положить? (кратно 50)')
        sum_add = int(input(' ->> '))
        if sum_add % 50 != 0:
            print(f'Введите сумму кратную 50 ')
            continue
        elif sum_add % 50 == 0:
            balance = balance + sum_add
            opperation_count += 1
            break
    log(log_dct, True, opperation_count, sum_add)
    return balance, opperation_count

def rich_comission(balance):
    if balance > 5_000_000:
        balance -= balance * 0.1
        print(f"С Вас сняли налог: {balance * 0.1}")
        print(f"Баланс: {balance}")
    return balance

def print_balance(balance):
    print(f'На Вашем счету: {round(balance, 2)}')

def print_log(log_dct):
    for k, v in log_dct.items():
        print(k, v)

while True:
    menu()
    button = input(' ->> ')
    if button == '1':
        print_balance(balance)
    elif button == '2':
        balance, opper_count = take_money(balance, opper_count)
    elif button == '3':
        balance, opper_count = put_money(balance, opper_count)
    elif button == '4':
        print_log(log_dct)
    elif button == '0':
        break
    else:
        print(f'Вы ввели неизвестную команду!')