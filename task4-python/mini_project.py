# Автор: [твои ФИО]
# Дата: [дата]
# Описание: Итоговая мини-программа. Вариант 1. Калькулятор рентабельности.

def calculate_profit(revenue, costs):
    """Возвращает прибыль компании."""
    return revenue - costs


def calculate_profitability(profit, revenue):
    """Возвращает рентабельность продаж в процентах."""
    if revenue == 0:
        return 0
    return profit / revenue * 100


def get_profitability_level(profitability):
    """Возвращает качественную оценку рентабельности."""
    if profitability > 20:
        return "высокая рентабельность"
    if profitability >= 10:
        return "средняя рентабельность"
    return "низкая рентабельность"


def print_report(company_name, revenue, costs):
    """Формирует и выводит отчёт о финансовом результате компании."""
    profit = calculate_profit(revenue, costs)
    profitability = calculate_profitability(profit, revenue)
    profitability_level = get_profitability_level(profitability)

    print("\nФинансовый отчёт")
    print("-" * 40)
    print(f"Компания: {company_name}")
    print(f"Выручка: {revenue} руб.")
    print(f"Затраты: {costs} руб.")
    print(f"Прибыль: {profit} руб.")
    print(f"Рентабельность продаж: {round(profitability, 2)}%")
    print(f"Оценка: {profitability_level}")


# Ввод исходных данных
company_name = input("Введите наименование компании: ")
revenue = float(input("Введите выручку компании: "))
costs = float(input("Введите затраты компании: "))

# Список контрольных показателей для демонстрации цикла for
indicators = ["выручка", "затраты", "прибыль", "рентабельность"]
print("\nВ программе будут рассчитаны показатели:")

for indicator in indicators:
    print(f"- {indicator}")

# Формирование итогового отчёта
print_report(company_name, revenue, costs)
