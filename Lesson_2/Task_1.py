# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

print(f"\n\n{'-' * 50} Вар1\n")

examples = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for i in examples:
    print(i, type(i))


print(f"\n\n{'-' * 50} Вар2\n")

print(15 * 3, type(15 * 3))
print(15 / 3, type(15 / 3))
print(15 // 2, type(15 // 2))
print(15 ** 2, type(15 ** 2))

# easy