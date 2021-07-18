from random import randint as ri


def dice_roll():
    '''Кидаем кость с сотней граней.
       Если значение бросока больше значения кости,
       то колесо будет цело.
       Чем больше шанс прокола, тем меньше шанс успеха.'''
    value = 50
    roll = ri(0, 100)
    if roll > value:
        return True
    return False


class Track:
    def __init__(self):
        self.distance = 100


class Car(Track):
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


def debug_run():
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
    first_place_name = tuple(sorted_dict.keys())[0]
    first_place_passing_distance = tuple(sorted_dict.values())[0]
    second_place_name = tuple(sorted_dict.keys())[1]
    second_place_name_passing_distance = tuple(sorted_dict.values())[1]
    third_place_name = tuple(sorted_dict.keys())[2]
    third_place_passing_distance = tuple(sorted_dict.values())[2]

    print(f'Первое место занял {first_place_name}, результат {first_place_passing_distance} МИН!')
    print(f'Второе место занял {second_place_name}, результат {second_place_name_passing_distance} МИН!')
    print(f'Третье место занял {third_place_name}, результат {third_place_passing_distance} МИН!')


debug_run()
