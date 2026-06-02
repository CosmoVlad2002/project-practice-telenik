# Автор: Теленик Владимир Николаевич
# Дата: 02.06.2026
# Описание: Модуль 2. Условные конструкции и циклы.

# Упражнение 1. Финансовый результат периода
print("Упражнение 1. Финансовый результат периода")
monthly_profit = float(input("Введите итоговую прибыль за месяц: "))

if monthly_profit > 0:
    print("Прибыль")
elif monthly_profit < 0:
    print("Убыток")
else:
    print("Безубыточность")

print("-" * 40)

# Упражнение 2. Классификация субъекта по выручке
print("Упражнение 2. Классификация субъекта по выручке")
annual_revenue = float(input("Введите годовую выручку предприятия: "))

if annual_revenue < 1_000_000:
    business_category = "Микробизнес"
elif annual_revenue < 10_000_000:
    business_category = "Малый бизнес"
elif annual_revenue < 100_000_000:
    business_category = "Средний бизнес"
else:
    business_category = "Крупный бизнес"

print(f"Категория предприятия: {business_category}")
print("-" * 40)

# Упражнение 3. Расчёт налога на доходы физических лиц
print("Упражнение 3. Расчёт НДФЛ")
monthly_salary = float(input("Введите ежемесячную заработную плату: "))

if monthly_salary <= 50_000:
    tax_rate = 13
else:
    tax_rate = 15

tax_amount = monthly_salary * tax_rate / 100
net_salary = monthly_salary - tax_amount

print(f"Ставка НДФЛ: {tax_rate}%")
print(f"Сумма налога: {tax_amount} руб.")
print(f"Зарплата на руки: {net_salary} руб.")
print("-" * 40)

# Упражнение 4. Таблица доходности по ставке
print("Упражнение 4. Таблица доходности по ставке")
rate = float(input("Введите процентную ставку годовых: "))
initial_capital = 100_000

for month in range(1, 13):
    interest = initial_capital * rate / 100 / 12 * month
    print(f"{month} месяц: начисленные проценты = {round(interest, 2)} руб.")

print("-" * 40)

# Упражнение 5. Анализ ценового диапазона
print("Упражнение 5. Анализ ценового диапазона")
prices = [1200, 850, 1600, 2400, 990]
average_price = sum(prices) / len(prices)

print(f"Средняя цена: {average_price} руб.")

for price in prices:
    if price > average_price:
        print(f"{price} руб. — ВЫШЕ СРЕДНЕГО")
    else:
        print(f"{price} руб.")
