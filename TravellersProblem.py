
# Cамостоятельно задать маршрут или использовать тестовый список с точками. 
# Ограничение по количеству точек маршрута 100.

checkpoints = {}
if  input(f'Cамостоятельно задать маршрут? y/n :') == 'y':
    for i in range(100):
        point_name = input('Введите пункт назначения: ')
        coord_x = input(f'Введите координату X {point_name} :')
        coord_y = input(f'Введите координату У {point_name} :')
        checkpoints[i] = [point_name, coord_x, coord_y]
        if input(f'Завершить ввод y/n? :') == 'y':
            break
else:
    checkpoints = {
        0: ['Почтовое отделение', 0, 2],
        1: ['Ул. Грибоедова 104/25', 2, 5],
        2: ['Ул. Бейкер стрит, 221б', 5, 2], 
        3: ['Ул. Большая Садовая, 302-бис', 6, 6],
        4: ['Вечнозелёная Аллея, 742', 8, 3]
        }

# Выводит все точки с координатами и номерами
for point in checkpoints:
    print(f'#{point} - {checkpoints[point]}')

# Задаёт точку отправления и прибытия.
start_point = '-1'
while True:
    # Если точки нет в словаре, тогда повторить ввод
    if start_point not in checkpoints.keys():
        start_point = int(input('Введите пункт отправления/прибытия:'))
    else:
        break

route_list = []  # Список возможных маршрутов
alphabet = [i for i in range(100)]
count_list = 0
# Количество возможных комбинаций маршрутов в коллекции из n+1 точек для тестового набора, 
# где первая и последняя точка заданы n^(n-1), где n это общее количество точек.
for count_list in range(len(checkpoints) ** (len(checkpoints)-1)):
    route_temp = []
    route_temp.append(start_point)  # Добавим точку отправления
    quotient = count_list
    while quotient  > 0:
        quotient, remainder = divmod(quotient , len(checkpoints))
        route_temp.append(alphabet[remainder])  # Запись точки в список
    while len(route_temp) < len(checkpoints):
        route_temp.append(0)  # Дополним список нулями до длины n
    uniq = set(route_temp)  
    # Если в списке точки не дублируются, тогда запишем их в список маршрутов
    if len(uniq) == len(checkpoints):
        route_temp.append(start_point)  # Добавим точку прибытия
        #print(route_temp)
        route_list.append(route_temp)

# Подсчёт длины для каждого маршрута из списка и нахождение кратчайшего
short_route = [0, '']
start_marker = True
for route in route_list:
    current_route = f'P{start_point}({checkpoints[start_point][1]};{checkpoints[start_point][2]})'
    current_dist = 0
    for k in range(len(checkpoints)):
        current_dist += ((checkpoints[route[k+1]][1] - checkpoints[route[k]][1]) ** 2
                        + (checkpoints[route[k+1]][2] - checkpoints[route[k]][2]) ** 2) ** 0.5
        current_route += f' -> P{route[k+1]}({checkpoints[route[k+1]][1]};\
{checkpoints[route[k+1]][2]}) [{current_dist}] '
        #print(f' -> P{route[k+1]}({checkpoints[route[k+1]][1]};\
#{checkpoints[route[k+1]][2]}) [{current_dist}] ', end = '')
    #print('\n')
    # Запись минимального маршрута
    if start_marker or current_dist < short_route[0]:
        short_route[0] = current_dist
        short_route[1] = current_route
        start_marker = False

print(f'\n{short_route[1]}= {short_route[0]}')