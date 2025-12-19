# tasks/task1.py



def solve():
# # Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    try:
    num1_input = input("Введите первое число: ")
    num2_input = input("Введите второе число: ")

    # Преобразуем введенные строки в целые числа
    num1 = int(num1_input)
    num2 = int(num2_input)

    total_sum = num1 + num2

    print(f"Сумма: {total_sum}")
    Ыexcept ValueError:
    print("Ошибка: Пожалуйста, введите целые числа.")




# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()