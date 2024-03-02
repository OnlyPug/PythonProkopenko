import pytest
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lesson15.homework15 import TrainCar, Train, Passenger


@pytest.fixture()
def train_creation():
    print("And again i creating this **** train")
    yield Train('Kiev-Crime')


@pytest.fixture()
def passenger_creation():
    yield TrainCar()


@pytest.fixture()
def passenger_anastasia():
    yield Passenger('Anastassiia Prokopenko', 'Crimea')


@pytest.fixture()
def passenger_oleh():
    yield Passenger('Oleh Vershynin', 'Crimea')


@pytest.fixture()
def passenger_anna():
    yield Passenger('Anna Okruhina', 'Kyiv')
