# Автор: Теленик Владимир Николаевич
# Дата: 02.06.2026
# Описание: Модуль 3. Функции.

def calculate_profit(revenue, costs):
    """Возвращает прибыль как разницу между выручкой и затратами."""
    return revenue - costs


def calculate_vat(price, vat_rate=20):
    """Возвращает сумму НДС для заданной цены и ставки налога."""
    return price * vat_rate / 100


def get_business_category(annual_revenue):
    """Возвращает категорию бизнеса по размеру годовой выручки."""
    if annual_revenue < 1_000_000:
        return "микро"
    if annual_revenue < 10_000_000:
        return "малый"
    if annual_revenue < 100_000_000:
        return "средний"
    return "крупный"


def compound_interest(initial_capital, interest_rate, years):
    """Возвращает итоговую сумму по формуле сложного процента."""
    return initial_capital * (1 + interest_rate / 100) ** years


def apply_discount(price, discount_percent):
    """Возвращает цену товара после применения скидки."""
    return price * (1 - discount_percent / 100)


# Упражнение 1. calculate_profit()
print("Упражнение 1. Расчёт прибыли")
profit_1 = calculate_profit(150_000, 90_000)
profit_2 = calculate_profit(240_000, 175_000)
profit_3 = calculate_profit(80_000, 95_000)
print(f"Прибыль 1: {profit_1} руб.")
print(f"Прибыль 2: {profit_2} руб.")
print(f"Прибыль 3: {profit_3} руб.")
print("-" * 40)

# Упражнение 2. calculate_vat()
print("Упражнение 2. Расчёт НДС")
vat_default = calculate_vat(10_000)
vat_custom = calculate_vat(10_000, 10)
print(f"НДС по ставке 20%: {vat_default} руб.")
print(f"НДС по ставке 10%: {vat_custom} руб.")
print("-" * 40)

# Упражнение 3. get_business_category()
print("Упражнение 3. Категория бизнеса")
revenues = [500_000, 5_000_000, 50_000_000, 150_000_000]

for revenue in revenues:
    category = get_business_category(revenue)
    print(f"Выручка {revenue} руб. — {category} бизнес")

print("-" * 40)

# Упражнение 4. compound_interest()
print("Упражнение 4. Сложный процент")
capital = 100_000
rate = 12

for years in [3, 5, 10]:
    final_amount = compound_interest(capital, rate, years)
    print(f"Срок {years} лет: итоговая сумма = {round(final_amount, 2)} руб.")

print("-" * 40)

# Упражнение 5. apply_discount()
print("Упражнение 5. Применение скидки")
product_prices = [1200, 2500, 4300, 890, 15000]
discount = 15

for price in product_prices:
    discounted_price = apply_discount(price, discount)
    print(f"Исходная цена: {price} руб.; цена со скидкой: {round(discounted_price, 2)} руб.")
