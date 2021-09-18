incorrect_sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(incorrect_sentence):
    if v.isdigit():
        incorrect_sentence[i] = f"'{int(v):02}'"
    elif v[1:].isdigit():
        incorrect_sentence[i] = f"'{v[0]}{int(v[1:]):02}'"

print(' '.join(incorrect_sentence))

# impossible