"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""


class HuffmanCode:
    def __init__(self, probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if value >= self.probability[j]:
                return j
        return index - 1

    def characteristics_huffman_code(self, code):
        length_of_code = [len(k) for k in code]

        mean_length = sum([a * b for a, b in zip(length_of_code, self.probability)])

        print("Average length of the code: %f" % mean_length)
        # print("Efficiency of the code: %f" % (entropy_of_code / mean_length))

    def compute_code(self):
        # получаем необходимое число кодов
        num = len(self.probability)
        # заполняем массив нужным кол-вом пустых строк
        huffman_code = [''] * num

        # перебираем элементы списка по два
        for i in range(num - 2):
            # ищем сумму вероятностей двух крайних элементов
            val = self.probability[num - i - 1] + self.probability[num - i - 2]
            if huffman_code[num - i - 1] != '' and huffman_code[num - i - 2] != '':
                # к каждому элементу списка последнего элемента клеим '1'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                # к каждому элементу списка предпоследнего элемента клеим '0'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif huffman_code[num - i - 1] != '':
                # предпоследний элемент проставляем как '0'
                huffman_code[num - i - 2] = '0'
                # у последнего элемента, к каждому элементу добавляем '1' слева
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif huffman_code[num - i - 2] != '':
                # последний элемент проставляем как '1'
                huffman_code[num - i - 1] = '1'
                # у предпоследнего(который список), к каждому элементу добавляем '0' слева
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:  # проставляем '1' последнему элементу, '0' предпоследнему
                huffman_code[num - i - 1] = '1'
                huffman_code[num - i - 2] = '0'

            # ищем позицию для вставки в первоначальный список вероятностей
            position = self.position(val, i)
            # отсекаем от изначального списка 2 последних элемента
            probability = self.probability[0:(len(self.probability) - 2)]
            # вставляем полученное значение в нужную позицию
            probability.insert(position, val)
            if isinstance(huffman_code[num - i - 2], list) and isinstance(huffman_code[num - i - 1], list):
                # последний и предпоследний элементы списки, тогда клеим в общий список
                complete_code = huffman_code[num - i - 1] + huffman_code[num - i - 2]
            elif isinstance(huffman_code[num - i - 2], list):
                # предпоследний элемент - список, клеим список + значение последнего элемента
                complete_code = huffman_code[num - i - 2] + [huffman_code[num - i - 1]]
            elif isinstance(huffman_code[num - i - 1], list):
                # последний элемент - список, клеим список + значение предпоследнего элемента
                complete_code = huffman_code[num - i - 1] + [huffman_code[num - i - 2]]
            else:  # формируем итоговый код, как список из значений двух последних элементов списка
                complete_code = [huffman_code[num - i - 2], huffman_code[num - i - 1]]

            # отсекаем крайний элемента из списка строк кодов
            huffman_code = huffman_code[0:(len(huffman_code) - 2)]
            # вставляем получившийся код в нужную позицию
            huffman_code.insert(position, complete_code)

        # клеим строки для первого и второго элементов
        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        # если длина второго элемента 0, то вписываем туда '1'
        if len(huffman_code[1]) == 0:
            huffman_code[1] = '1'

        count = 0
        # финальные коды
        final_code = [''] * num

        # в huffman_code должно остаться 2 элемента
        for i in range(2):
            for j in range(len(huffman_code[i])):
                # последовательно вытаскиваем элементы из первого элемента(список)
                final_code[count] = huffman_code[i][j]
                count += 1

        # сортируем полученный массив по длине строк по возрастанию
        final_code = sorted(final_code, key=len)
        return final_code


# генерирует по строке словарь символов с кол-вом повторений символа в строке
def generate_frequencies(str):
    freq = {}
    for c in str:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq


string = input("Enter the string to compute Huffman Code: ")

# словарь, где ключ это символ, а значение кол-во повторений
freq = generate_frequencies(string)
# сортируем словарь по значениям(частотам) в порядке убывания
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# длина строки
length = len(string)
# подсчет вероятностей для каждого символа - частота появления, деленная на длину строки
probabilities = [float("{:.2f}".format(frequency[1] / length)) for frequency in freq]
# сортируем по убыванию
probabilities = sorted(probabilities, reverse=True)
# создаем объект
huffmanClassObject = HuffmanCode(probabilities)
# создаем метод, который строит список кодов
huffman_code = huffmanClassObject.compute_code()

print(' Char | Huffman code ')
print('----------------------')

for id, char in enumerate(freq):
    if huffman_code[id] == '':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman_code[id]))

huffmanClassObject.characteristics_huffman_code(huffman_code)
