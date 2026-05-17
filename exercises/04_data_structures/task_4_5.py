# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов, которые есть
и в команде command1 и в команде command2 (пересечение).

В данном случае, результатом должен быть такой список: ['1', '3', '8']

Записать итоговый список в переменную result. (именно эта переменная будет
проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1_split = (command1.split())
command2_split = (command2.split())
vlans1 = (command1_split[-1])
vlans2 = (command2_split[-1])
result1 = vlans1.split(",")
result2 = vlans2.split(",")
set_result1 = set(result1)
set_result2 = set(result2)

result3 = list(set_result1.intersection(set_result2))
result = sorted(result3)
print(result)
