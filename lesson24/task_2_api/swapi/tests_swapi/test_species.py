import pytest


def test_get_species_page(species_service):
    response = species_service.get_species_page()
    assert response.status_code == 200


def test_get_species_page_not_found(species_service):
    species = species_service.get_all_species(page=8)
    assert species.status_code == 404
    assert species.json()["detail"] == "Not found"


@pytest.mark.parametrize('current,previous,next',
                         [(1, None, "https://swapi.dev/api/species/?page=2"),
                          (2, "https://swapi.dev/api/species/?page=1", "https://swapi.dev/api/species/?page=3"),
                          (3, "https://swapi.dev/api/species/?page=2", "https://swapi.dev/api/species/?page=4"),
                          (4, "https://swapi.dev/api/species/?page=3", None)])
def test_get_species_with_parameters(species_service, current, previous, next):
    species = species_service.get_all_species(current)
    assert species.json()['previous'] == previous
    assert species.json()['next'] == next


def test_get_single_species(species_service):
    single_species = species_service.get_single_species(31)
    assert single_species.status_code == 200
    assert single_species.json()['name'] == "Besalisk"


def test_negative_single_species(species_service):
    response = species_service.get_single_species(100)
    assert response.status_code == 404
    assert response.json() == species_service.compare_for_negative()


def test_save_one_species(species_service):
    single_species = species_service.get_single_species(31)
    species_service.save_single_species()
    assert single_species.status_code == 200
    assert single_species.json()['name'] == "Besalisk"


def test_save_species_page(species_service):
    response = species_service.get_all_species()
    assert response.status_code == 200
    species_service.save_current_page()
    assert response.json()["previous"] is None


# Тут хотіла щоб кожна сторінка додавалась в вже існуючий json але трішки каряво вийшло на жаль

# @pytest.mark.parametrize('current,previous,next',
#                          [(1, None, "https://swapi.dev/api/species/?page=2"),
#                           (2, "https://swapi.dev/api/species/?page=1", "https://swapi.dev/api/species/?page=3"),
#                           (3, "https://swapi.dev/api/species/?page=2", "https://swapi.dev/api/species/?page=4"),
#                           (4, "https://swapi.dev/api/species/?page=3", None)])
# def test_get_species_with_parameters(species_service, current, previous, next):
#     species = species_service.get_all_species(current)
#     assert species.json()['previous'] == previous
#     assert species.json()['next'] == next
#     species_service.save_all_pages(current)


@pytest.mark.parametrize('current,previous,next',
                         [(1, None, "https://swapi.dev/api/species/?page=2"),
                          (2, "https://swapi.dev/api/species/?page=1", "https://swapi.dev/api/species/?page=3"),
                          (3, "https://swapi.dev/api/species/?page=2", "https://swapi.dev/api/species/?page=4"),
                          (4, "https://swapi.dev/api/species/?page=3", None)])
def test_get_species_with_parameters(species_service, current, previous, next):
    species = species_service.get_all_species(current)
    assert species.json()['previous'] == previous
    assert species.json()['next'] == next
    species_service.save_all_pages_test(current)

