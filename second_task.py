# import re
# from typing import Callable, Generator
#
#
# # Визначення функції generator_numbers
# def generator_numbers(text: str) -> Generator:
#     # Використання регулярного виразу для пошуку всіх дійсних чисел у тексті
#     for match in re.finditer(r'\b\d+\.\d+\b', text):
#         yield float(match.group())
#
#
# # Визначення функції sum_profit
# def sum_profit(text: str, func: Callable) -> float:
#     # Виклик функції generator_numbers і підсумовування всіх значень
#     return sum(func(text))
#
#
# if __name__ == "__main__":
#     text = input("Введіть текст")
#     total_income = sum_profit(text, generator_numbers)
#     print(f"Загальний дохід: {total_income}")


import re
from typing import Callable, Generator


# Визначення функції generator_numbers
def generator_numbers(text: str) -> Generator:
    # Використання регулярного виразу для пошуку всіх дійсних чисел у тексті,
    # які чітко відокремлені пробілами з обох боків

    for match in re.finditer(r'(?<=\s)\d+(\.\d+)?(?=\s)', text):

        yield float(match.group())


# Визначення функції sum_profit
def sum_profit(text: str, func: Callable) -> float:
    # Виклик функції generator_numbers і підсумовування всіх значень
    return sum(func(text))


if __name__ == "__main__":
    text = input("Введіть текст: ")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
