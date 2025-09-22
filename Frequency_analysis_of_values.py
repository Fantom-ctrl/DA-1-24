import pandas as pd
import matplotlib.pyplot as plt


def generate_synthetic_data() -> pd.DataFrame:
    """Генерация синтетических данных для категорий.

    Аргументы:
        Никаких.
    
    Возврат:
        table (pd.DataFrame) - таблица или None, если таблица не создалась.
        """
    data = {
        "Colors": ["Blue", "Red", "Green", "Orange", "Red", "Red",
                   "Red", "Green", "Green", "Blue", "Blue", "Blue"]
    }
    
    # Проверка на то, что словарь не пуст
    if not data:
        print("Нет данных")
        return
    
    table = pd.DataFrame(data)
    
    return table


def create_chart(count_frequency: pd.Series) -> None:
    """
    Построение горизонтальной столбчатой диаграммы частоты категориальных значений.
    
    Аргументы:
        count_frequency (pd.Series): Индексы Series — категории, значения — частота в долях.
    
    Возврат:
        (fig, ax) - кортеж содержащий фигуру и оси или None, если тип данных аргумента не правильный
    """
    # Проверка на правильный тип данных 
    if not isinstance(count_frequency, pd.Series):
        print("В функцию передан не тот тип данных")
        return
    
    # Создаем фигуру и оси
    fig, ax = plt.subplots()
    count_frequency.plot(kind="barh", color="blue", edgecolor="black", ax=ax)
    ax.set_title("Частота значений")
    ax.set_xlabel("Доля")
    ax.set_ylabel("Категория")
    plt.tight_layout()
    
    return fig, ax


def main():
    column_name = input("Введите название категории: ")

    # Генерация синтетических данных с проверкой на то, пуста ли таблица
    table = generate_synthetic_data()
    
    # Проверка на существование категории
    if column_name not in table.keys():
        print("Такой категории нет.")
        return

    # Проверка на то, что таблица не пустая
    if table.empty or table is None:
        print("Таблица пуста")
        return
    
    # Проверка существования нужного столбца
    if column_name not in table.columns:
        print(f"Ошибка: столбец '{column_name}' отсутствует в данных")
        return

    # Подсчитываем частоту
    count_frequency = table[column_name].value_counts(normalize=True)
    
    # Сохранение данных
    try:
        with open("count_category.txt", "w") as f:
            for category, value in count_frequency.items():
                f.write(f"{category} {value}\n")
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")
        return

    # Построение графика
    fig, ax = create_chart(count_frequency)
    plt.show()

    return


if __name__ == "__main__":
    main()