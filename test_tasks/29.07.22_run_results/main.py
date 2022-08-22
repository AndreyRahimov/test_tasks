'''Задача: обработав исходные данные,
вывести таблицу с первыми результатами бегунов'''

import os
import json
import datetime

# Определим абсолютный путь до файла со спорсменами на компьютере пользователя
dirname = os.path.dirname(__file__)
competitors_file = os.path.join(dirname, 'competitors2.json')

# Загрузим данные из файла со спортсменами в словарь origin_athletes
with open(competitors_file, encoding='utf-8-sig') as f:
    origin_athletes = json.load(f)

# В исходных данных путаница: вместо имени спортсмена указана его фамилия,
# а вместо фамилии - имя.
# На основе данных оригинального словаря создадим новый - исправленный
athletes = {}
for number in origin_athletes:
    athletes[number] = {}
    name = origin_athletes[number]['Surname']
    surname = origin_athletes[number]['Name']
    athletes[number]['Name'] = name
    athletes[number]['Surname'] = surname

# В файле со спортсменами используется BOM,
# который перекочевал в один из ключей нашего списка в виде '\ufeff'.
# Так как мы можем не знать, в каком ключе проблема, воспользуемся перебором
for number in athletes:
    if '\ufeff' in number:
        athletes[number.lstrip('\ufeff')] = athletes[number]
        del athletes[number]
        break  # BOM-метка одна на весь файл

# Определим абсолютный путь до файла с результатами первых забегов
results_file = os.path.join(dirname, 'results_RUN.txt')

# Загрузим данные и составим из них список results
with open(results_file, encoding='utf-8-sig') as f:
    results = f.readlines()
results = [i.strip().split() for i in results]

# Дополним наш список athletes информацией из results:
# временем начала (Start), и временем окончания (Finish)
# первого забега спортсмена
for number, position, timer in results:
    timer = timer.replace(',', '.')
    if position == 'start':
        athletes[number]['Start'] = datetime.time.fromisoformat(timer)
    if position == 'finish':
        athletes[number]['Finish'] = datetime.time.fromisoformat(timer)
        # Так как просто посчитать разницу между объектами time нельзя,
        # то воспользуемся их преобразованием.
        # Полученная разница будет результатом забега спортсмена
        athletes[number]['Result'] = datetime.datetime.combine(datetime.date.min, athletes[number]['Finish']) - datetime.datetime.combine(datetime.date.min, athletes[number]['Start'])

# Спортсмен с номером 266 отсутствует в файле с результатами.
# Вероятно, это ошибка, возможно, связанная с тем,
# что этот спортсмен первый в списке спортсменов и перед ним стоит BOM-метка.
# Удалим данного спортсмена
del athletes['266']

# Создадим список собранной информации,
# отсортированный по результатам забегов от лучшего к худшему
rating = sorted(athletes.items(), key=lambda x: x[1]['Result'])

# Оформим результат в более-менее симпатичную табличку
print('Занятое место   Нагрудный номер     Имя         Фамилия      Результат')
for i, athlete in enumerate(rating, 1):
    print(str(i).rjust(8), end='')
    print(athlete[0].rjust(19).ljust(27), end='')
    print(athlete[1]['Name'].ljust(13), end='')
    print(athlete[1]['Surname'].ljust(14), end='')
    print(str(athlete[1]['Result'])[2:10].ljust(8))
