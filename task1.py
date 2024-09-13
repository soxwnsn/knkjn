import random
try:
    name_one =input('Введите имя первого волшебника:')
    name_two =input('Введите имя второго волшебника:')
    stage1 = int(input('Введите кол-во использованных заклинаний первым волшебником:'))
    stage1_points = random.randint(3,10)*stage1
    print(f"За первый этап первый волшебник получил {stage1_points} очков")
    stage1_name2 = int(input('Введите кол-во использованных заклинаний вторым волшебником:'))
    stage1_points2 = random.randint(3, 10) * stage1_name2
    print(f"За первый этап второй волшебник получил {stage1_points2} очков")

    stage2_name1 = input('Кто из волшебников разгадал загадку?:')
    if stage2_name1 == name_one:
      stage2_points = random.randint(30,50 )
    print(f"За второй этап волшебник получил {stage2_points} очков")

    stage3 = input('Кто из волшебников прошел полосу припятствий?:')
    if stage3 == name_one:
      stage_3_points = 40
      print(f'За третий этап волшебник получил {stage_3_points} очков')

    honesty_points = int(input('Введите кол-во баллов за честность:'))
    support_points = int(input('Введите кол-во баллов за поддержку друзей:'))
    total_points = stage1_points+stage2_points+stage_3_points+honesty_points+support_points
    if total_points > 100:
        print(f'Первый волшебник победил и заработал {total_points} очков ')
    else:
        print(f'Первый волшебник проиграл и заработал {total_points} очков')
except ValueError as e:
    print('Некорректный ввод')