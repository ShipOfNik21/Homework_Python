# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

prices = [57.08, 46, 51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

print(f"\n\n{'-' * 50} A\n")

for i in prices:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):02d} коп,", end=" ")

print(f"\n\n{'-' * 50} B\n")

print(f"ID base: {id(prices)} - {prices}")
prices.sort()
print(f"ID change: {id(prices)} - {prices}")

print(f"\n\n{'-' * 50} C and D\n")

n_list = sorted(prices, reverse=True)
print(f"ID chenge: {id(n_list)} - {n_list}\n{n_list[:5][::-1]}")

# impossible

