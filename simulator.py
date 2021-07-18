from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from random import randint as ri


def dice_roll():
    ''' Кидаем кость с сотней граней.
       Если значение бросока больше значения кости,
       то колесо будет цело.
       Чем больше шанс прокола, тем меньше шанс успеха. '''
    value = 50
    roll = ri(0, 100)
    if roll > value:
        return True
    return False


class Track:
    ''' Создаём Класс трэка. '''
    def __init__(self):
        self.distance = 100


class Car(Track):
    ''' Создаём Класс легкового автомобиля. '''
    def __init__(self):
        self.name = 'Car'
        self.speed = 120
        self.number_of_people = ri(1, 5)
        self.speed -= self.number_of_people * 4
        track = Track()
        if dice_roll() is True:
            self.passing_distance_car = int(track.distance
                                            / self.speed * 60 + 10)
        else:
            self.passing_distance_car = int(track.distance / self.speed * 60)


class Truck(Track):
    ''' Создаём Класс грузового автомобиля. '''
    def __init__(self):
        self.name = 'Truck'
        self.speed = 100
        self.cargo_weight = ri(0, 10)
        self.speed -= self.cargo_weight * 2
        track = Track()
        if dice_roll() is False:
            self.passing_distance_truck = int(track.distance
                                              / self.speed * 60 + 10)
        else:
            self.passing_distance_truck = int(track.distance / self.speed * 60)


class Bike(Track):
    ''' Создаём Класс мотоцикла. '''
    def __init__(self):
        self.name = 'Bike'
        self.speed = 140
        self.stroller = ri(1, 2)
        self.speed /= self.stroller
        track = Track()
        if dice_roll() is False:
            self.passing_distance_bike = int(track.distance
                                             / self.speed * 60 + 10)
        else:
            self.passing_distance_bike = int(track.distance / self.speed * 60)


def run():
    ''' Запуск события. '''
    car = Car()
    truck = Truck()
    bike = Bike()
    results = []
    results = {car.name: car.passing_distance_car,
               truck.name: truck.passing_distance_truck,
               bike.name: bike.passing_distance_bike}
    sorted_values = sorted(results.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in results.keys():
            if results[k] == i:
                sorted_dict[k] = results[k]
                break
    first_place = insertText (f'Первое место занял {tuple(sorted_dict.keys())[0]}, результат {tuple(sorted_dict.values())[0]} МИН!')
    second_place = insertText (f'Второе место занял {tuple(sorted_dict.keys())[1]}, результат {tuple(sorted_dict.values())[1]} МИН!')
    third_place = insertText (f'Третье место занял {tuple(sorted_dict.keys())[2]}, результат {tuple(sorted_dict.values())[2]} МИН!')

    return first_place, second_place, third_place


root = Tk()

''' Размеры окна программы. '''
WIDTH = 1024
HEIGHT = 600

''' Создаём главное окно
Вычисляем координаты для размещения окна по центру. '''
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenwidth() // 2 - HEIGHT // 2

''' Установка заголовка. '''
root.title('ГОНКИ ПО КРУГУ')

''' Запрещаем изменение размеров. '''
root.resizable(False, False)

''' Устанавливаем ширину, высоту и позицию. '''
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

''' Загружаем изображение фона. '''
road_image = PhotoImage(file='road.png')

''' Устанавливаем изображение в Label. '''
road = Label(root, image=road_image)
road.place(x=0, y=17)

''' Создаём кнопку и выводим её на экран. '''
startButton = Button(text='СТАРТ',
                     font='arial 20',
                     width=61,
                     background='#37AA37')
startButton.place(x=20, y=370)
startButton['state'] = 'normal'

''' Создаём информационный чат виджетом Text. '''
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

''' Создаём и прикрепляем к тексту полосу прокрутки. '''
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary['yscrollcommand'] = scroll.set


def championship_table():
    ''' Отображение результатов. '''
    first_place = 0
    second_place = 0
    third_place = 0
    insertText(first_place)
    insertText(second_place)
    insertText(third_place)


def insertText(run):
    ''' Добавление строки в текстовый блок. '''
    textDiary.insert(INSERT, run)
    textDiary.see(END)


''' Назначаем метод, выполняющийся при нажатии на 'Старт'. '''
startButton['command'] = run

championship_table()

''' Выводим главное окно на экран. '''
root.mainloop()
