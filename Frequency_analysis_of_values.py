import pandas as p
import matplotlib.pyplot as plt


def chart(count_frequency):
    """
    Построение горизонтальной столбчатой диаграммы частоты категориальных значений.

    Аргументы:
    count_frequency(pandas.Series): Индексы Series — категории, значения — частота в долях
    
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


def main():
    # Создание синтетических данных
    data = {"Category": 
            ["Blue", "Red", "Green", "Orange",
            "Red", "Red", "Red", "Green",
            "Green", "Blue", "Blue", "Blue"]}
    
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

    # Подсчитываем частоту
    count_frequency = table["Category"].value_counts(normalize=True)

    #Построение графика
    chart(count_frequency)


if __name__ == "__main__":
    main()