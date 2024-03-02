import pytest

from lesson15.homework15 import Passenger


@pytest.mark.smoke
def test_train(train_creation):
    train_creation.add_car(1)
    train_creation.add_car(1)
    assert len(train_creation) == 1


@pytest.mark.negative
def test_negative_train(train_creation):
    try:
        train_creation.add_car(1)
        assert len(train_creation) == 1
    except AssertionError:
        print("We have only 'lokomotuv', please add 1 more car")


@pytest.mark.smoke
def test_passenger(passenger_creation, passenger_anastasia, passenger_oleh):
    car1 = passenger_creation
    car1[1] = passenger_anastasia
    car1[2] = passenger_oleh
    assert len(passenger_creation) == 2


@pytest.mark.smoke
def test_car_full(passenger_creation, passenger_anastasia, passenger_oleh, passenger_anna):
    car1 = passenger_creation
    car1[1] = passenger_anastasia
    car1[2] = passenger_oleh
    car1[3] = passenger_anna
    print(car1)


@pytest.mark.negative
@pytest.mark.xfail(reason="Parametrize", condition=True)
@pytest.mark.parametrize('name_creation,expected_name', [('Kiev-Crimea', 'Kiev-Crimea'), ('Kiev-Crimea', 'Kiev')])
def test_car_parametrize(passenger_creation, name_creation, expected_name):
    train1 = name_creation
    assert train1 == expected_name


@pytest.mark.negative
@pytest.mark.xfail(reason="Parametrize", condition=True)
@pytest.mark.parametrize('passenger,expected_passenger_name,destination_creation,expected_destination',
                         [(Passenger('Anastasiia Prokopenko', 'Crimea'), 'Anastasiia Prokopenko', 'Crimea','Crimea'),
                          (Passenger('Oleh Vershynin', 'Crimea'), 'Oleh Vershynin', 'Crimea', 'Kiev')])
def test_passenger_parametrize(passenger, expected_passenger_name, destination_creation, expected_destination):
    assert passenger.passenger_name == expected_passenger_name
    assert passenger.destination == expected_destination
