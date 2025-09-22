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


def main():
    column_name = "Category"

    # Создание синтетических данных
    data = {column_name: 
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
    
    # Проверка существования нужного столбца
    if column_name not in table.columns:
        print(f"Ошибка: столбец '{column_name}' отсутствует в данных")
        return

    # Подсчитываем частоту
    count_frequency = table[column_name].value_counts(normalize=True)

    #Построение графика
    creat_chart(count_frequency)


if __name__ == "__main__":
    main()