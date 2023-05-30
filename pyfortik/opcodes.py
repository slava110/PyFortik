commands = [
    'push',
    'op',
    'call',
    'is',
    'to',
    'exit'
]


def not_implemented():
    pass


operators = {
    '+': not_implemented(),  # сложение
    '-': not_implemented(),  # вычитание
    '*': not_implemented(),  # умножение
    '/': not_implemented(),  # целочисленное деление
    '%': not_implemented(),  # остаток от деления
    '&': not_implemented(),  # AND
    '|': not_implemented(),  # OR
    '^': not_implemented(),  # XOR
    '<': not_implemented(),  # больше чем
    '>': not_implemented(),  # меньше чем
    '=': not_implemented(),  # равно
    '<<': not_implemented(),  # побитовый сдвиг влево
    '>>': not_implemented(),  # побитовый сдвиг вправо
    'if': not_implemented(),  # условный оператор
    'for': not_implemented(),  # цикл
    '.': not_implemented(),  # вывод значения на экран
    'emit': not_implemented(),  # вывод символа на экран
    '?': not_implemented(),  # ввод из консоли
    'array': not_implemented(),  # выделить массив и вернуть ссылку на него
    '@': not_implemented(),  # чтение элемента из массива по индексу
    '!': not_implemented()  # запись элемента в массив по индексу
}
