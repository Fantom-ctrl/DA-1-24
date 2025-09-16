import pandas as p
import matplotlib.pyplot as plt


def chart(count_frequency):
    """Построение графика"""
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
    
    # Построение таблицы
    table = p.DataFrame(data)

    # Подсчитываем частоту
    count_frequency = table["Category"].value_counts(normalize=True)

    #Построение графика
    chart(count_frequency)


if __name__ == "__main__":
    main()