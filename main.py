from first_task import fib
from fourth_task import main as fourth_task
from second_task import generator_numbers, sum_profit
from third_task import main as third_task

if __name__ == "__main__":
    task = input("Введіть номер завдання, яке хочете перевірити")
    if task == 1:
        print(fib(int(input("Введіть який номер числа послідовності Фібоначчі вас цікавить"))))

    elif task == 2:
        text = input("Введіть текст")
        total_income = sum_profit(text, generator_numbers)
        print(f"Загальний дохід: {total_income}")

    elif task == 3:
        third_task()

    elif task == 4:
        fourth_task()


