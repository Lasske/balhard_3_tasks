"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Банковский вклад
Пользователь делает вклад в размере a рублей сроком на какое-то кол-во лет
под 10% годовых (каждый год размер его вклада увеличивается на 10%.
Эти деньги прибавляются к сумме вклада,
и на них в следующем году тоже будут проценты).

Отредактировать функцию calculate_deposit, которая принимает 2 аргумента:
    - summa - первоначальная сумма на вкладе
    - years - кол-во лет
таким образом, чтобы функция возвращала сумму, которая будет на счете через
years лет

Формула сложных процентов: S = Р((1 + i)**n), где
    - S - итоговая сумма
    - P - первоначальный взнос
    - i - процентная ставка (если 20%, то 0.2)
    - n - кол-во лет

ПРИМЕРЫ
--------------------------------------------------------------------------------
- calculate_deposit(100, 5) -> 161.05100000000004
- calculate_deposit(1000, 2) -> 1210.0000000000002
- calculate_deposit(552, 13) -> 1905.6537103449932
- calculate_deposit(321, 7) -> 625.5381891000004
"""
# Процентная ставка
DEPOSIT_RATE = 10


def calculate_deposit(summa: float, years: int) -> float:
    """Рассчитывает итоговую сумму по вкладу

    :param summa: первоначальная сумма на вкладе

    :param years: количество лет вклада

    :return: итоговая сумма на вкладе
    """
    result = (summa * ((1 + DEPOSIT_RATE / 100) ** years))
    return result


if __name__ == '__main__':
    print('Программа расчета суммы на депозите после некоторого кол-ва лет')
    sum_val = float(input('Введите сумму для вклада: '))
    years_val = int(input('Введите количество лет: '))
    print(f"После {years_val} лет сумма на депозите будет равна: "
          f"{calculate_deposit(sum_val, years_val)}")
