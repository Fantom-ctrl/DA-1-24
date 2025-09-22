import pandas as p
import matplotlib.pyplot as plt


def creat_chart(count_frequency: p.Series) -> None:
    """
    Построение горизонтальной столбчатой диаграммы частоты категориальных значений.

    Аргументы:
    count_frequency(p.Series): Индексы Series — категории, значения — частота в долях
    
    Возврат:
    Функция отображает график, но не возвращает значения.
    """
    # Проверка на правильный тип данных 
    if not isinstance(count_frequency, p.Series):
        print("В функцию передан не тот тип данных")
        return
    
    count_frequency.plot(kind="barh", color="blue", edgecolor="black")
    plt.title("Частота значений")
    plt.xlabel("Доля")
    plt.ylabel("Категория")
    plt.show()

    return


def main():
    column_name = input("Введите название категории: ")

    # Создание синтетических данных
    data = {"Colors": 
            ["Blue", "Red", "Green", "Orange",
            "Red", "Red", "Red", "Green",
            "Green", "Blue", "Blue", "Blue"]}

    # Проверка на существование категории
    if column_name not in data.keys():
        print("Такой категории нет.")
        return
    
    # Проверкана то, что словарь не пуст
    if not data:
        print("Нет данных")
        return
    
    # Построение таблицы
    table = p.DataFrame(data)

    # Проверка на то, что таблица не пустая
    if table.empty:
        print("Таблица пуста")
        return
    
    # Проверка существования нужного столбца
    if column_name not in table.columns:
        print(f"Ошибка: столбец '{column_name}' отсутствует в данных")
        return

    # Подсчитываем частоту
    count_frequency = table[column_name].value_counts(normalize=True)

    #Построение графика
    creat_chart(count_frequency)

    return


if __name__ == "__main__":
    main()