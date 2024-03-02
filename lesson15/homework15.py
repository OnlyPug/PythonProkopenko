class Train:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars) - 1

    def __str__(self):
        return f'"traincart" : {len(self.cars)}'


class TrainCar:
    def __init__(self):
        self.passenger = dict()

    def __len__(self):
        return len(self.passenger)

    def __setitem__(self, key, value):
        if len(self.passenger) < 2:
            self.passenger[key] = value
        else:
            print("Car is full! Cannot add more passengers.")

    def __getitem__(self, item: int):
        return self.passenger[item]

    """не буду лукавити, тут мені допоміг інтернет бо щось я і недопетрила як зробити це по 'людскі',
    а не через пень-колоду як я"""

    def __str__(self):
        passenger_str = ',\n'.join([f'\n\t "passenger_name": "{p.passenger_name}",\n\t "destination": "{p.destination}"'
                                    f'\n\t "place": {place}' for place, p in self.passenger.items()])
        return passenger_str


class Passenger:
    def __init__(self, passenger_name: str, destination: str):
        self.passenger_name = passenger_name
        self.destination = destination


if __name__ == '__main__':
    train1 = Train("Kiev-Crime")
    train1.add_car(1)
    train1.add_car(1)
    train1.add_car(1)
    train1.add_car(1)
    train1.add_car(1)
    car1 = TrainCar()
    passenger1 = Passenger('Anastassiia Prokopenko', 'Crimea')
    passenger2 = Passenger('Anna Okruhina', 'Kyiv')
    passenger3 = Passenger('Oleh Vershynin', 'Crimea')
    passenger4 = Passenger('Viktoria Olenuk', 'Mykolaiv')
    passenger5 = Passenger('Ivan Kolko', 'Kherson')
    # Check logic for over 10 passengers
    # passenger6 = Passenger('Anastassiia Prokopenko', 'Crimea')
    # passenger7 = Passenger('Anna Okruhina', 'Kyiv')
    # passenger8 = Passenger('Oleh Vershynin', 'Crimea')
    # passenger9 = Passenger('Viktoria Olenuk', 'Mykolaiv')
    # passenger10 = Passenger('Ivan Kolko', 'Kherson')
    # passenger11 = Passenger('None', 'Kyiv')

    car1[1] = passenger1
    car1[2] = passenger2
    car1[3] = passenger3
    car1[4] = passenger4
    car1[5] = passenger5
    # Check logic for over 10 passengers
    # car1[6] = passenger6
    # car1[7] = passenger7
    # car1[8] = passenger8
    # car1[9] = passenger9
    # car1[10] = passenger10
    # car1[11] = passenger11
    print(train1)
    print(car1)
    print(passenger1.passenger_name)
