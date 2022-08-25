# -*- coding: utf-8 -*-
'''На языке Python (2.7) реализовать минимум по 2 класса реализовывающих
циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.'''

from collections import deque


class Buffer0:
    '''Данный вариант ограничивается встроенными инструментами Python,
    поэтому плюсом можно считать то, что вся работа буфера понятна
    из самого кода, нет необходимости обращаться к сторонней документации.
    К минусам можно отнести не лучшую производительность'''

    def __init__(self, size=10):
        self.size = size
        self.content = []

    def add_el(self, el):
        while len(self.content) >= self.size:
            del self.content[0]
        self.content.append(el)


class Buffer1:
    '''Данный вариант реализуется через двухстороннюю очередь из библиотеки
    collections. Благодаря этому код лучше оптимизирован по эффективности и
    скорости работы, так как deque создан на более низкоуровневом языке, чем
    Python. С другой стороны, доступ к элементам в середине структуры
    у deque не столь быстрый'''

    def __init__(self, size=10):
        self.size = size
        self.content = deque(maxlen=size)

    def add_el(self, el):
        self.content.append(el)
