import pytest

from lesson24.task_2_api.swapi import StarshipService
from lesson24.task_2_api.swapi import SpeciesService


@pytest.fixture
def starships_service():
    yield StarshipService()

@pytest.fixture
def species_service():
    yield SpeciesService()