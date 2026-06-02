# Автор: Теленик Владимир Николаевич
# Дата: 02.06.2026
# Описание: Модуль 1. Переменные, типы данных, ввод и вывод.

# Упражнение 1. Карточка сотрудника
employee_name = "Иван Петров"
employee_age = 20
employee_salary = 55000.50
is_employed = True

print("Упражнение 1. Карточка сотрудника")
print(f"Имя сотрудника: {employee_name}")
print(f"Возраст: {employee_age}")
print(f"Заработная плата: {employee_salary} руб.")
print(f"Сотрудник трудоустроен: {is_employed}")
print("-" * 40)

# Упражнение 2. Приветствие сотрудника
print("Упражнение 2. Приветствие сотрудника")
name = input("Введите имя сотрудника: ")
city = input("Введите город: ")
print(f"Сотрудник {name} работает в офисе {city}")
print("-" * 40)

# Упражнение 3. Расчёт итоговой стоимости
print("Упражнение 3. Расчёт итоговой стоимости")
unit_price = float(input("Введите цену единицы товара: "))
quantity = int(input("Введите количество единиц товара: "))
total_cost = unit_price * quantity
print(f"Итоговая стоимость: {total_cost} руб.")
print("-" * 40)

# Упражнение 4. Доход по банковскому вкладу
print("Упражнение 4. Доход по банковскому вкладу")
deposit_amount = float(input("Введите сумму вклада: "))
interest_rate = float(input("Введите процентную ставку годовых: "))
annual_income = deposit_amount * interest_rate / 100
final_amount = deposit_amount + annual_income
print(f"Доход за один год: {annual_income} руб.")
print(f"Итоговая сумма вклада: {final_amount} руб.")
print("-" * 40)

# Упражнение 5. Конвертация валюты
print("Упражнение 5. Конвертация валюты")
usd_rate = float(input("Введите курс доллара к рублю: "))
rub_amount = float(input("Введите сумму в рублях: "))
usd_amount = rub_amount / usd_rate
print(f"Сумма в долларах: {round(usd_amount, 2)} USD")
