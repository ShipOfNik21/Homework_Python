# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([i for i in src if src.count(i) == 1])


print(f'\n{50*"*"} \n')


my_dict = {i: 0 for i in src}

for i in src:
    my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])