# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


networks = str(input())

address = networks.split('/')

network = address[0]



rip = network.split(".")

ip_template = '''
Network:
{:<8}  {:<8}  {:<8}  {:<8}
{:>08b}  {:>08b}  {:>08b}  {:>08b}
'''

network_done = (ip_template.format(int(rip[0]), int(rip[1]), int(rip[2]), int(rip[3]), int(rip[0]), int(rip[1]), int(rip[2]), int(rip[3])))

mask = address[1]

bin_mask_network = 32 - int(mask)


bin_mask = "1" * ( 32 - int(bin_mask_network)) + "0" * int(bin_mask_network)

octet_1 = (bin_mask[0:8])
octet_2 = (bin_mask[8:16])
octet_3 = (bin_mask[16:24])
octet_4 = (bin_mask[24:32])

bin_octet_1 = int(octet_1, 2)
bin_octet_2 = int(octet_2, 2)
bin_octet_3 = int(octet_3, 2)
bin_octet_4 = int(octet_4, 2)

print(network_done, f'''
Mask:
/{mask}
{bin_octet_1:<9} {bin_octet_2:<9} {bin_octet_3:<9} {bin_octet_4:<9}
{octet_1}  {octet_2}  {octet_3}  {octet_4}''')


