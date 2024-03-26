from requests import get
import json
from lesson24.task_2_api.conf import config


class SpeciesService:
    def __init__(self):
        self.__species_url = f'{config["host1"]}species/'

    def get_species_page(self):
        return get(self.__species_url)

    def get_all_species(self, page=1):
        return get(f'{self.__species_url}?page={page}')

    def get_single_species(self, id=31):
        return get(f'{self.__species_url}{id}/')

    def save_single_species(self):
        response = self.get_single_species()
        with open(f'{response.json()["name"]}_species.json', 'w') as starship_data:
            json.dump(response.json(), starship_data, indent=4)

    def save_current_page(self):
        response = self.get_all_species()
        with open(f'First_page_species.json', 'w') as starship_data:
            json.dump(response.json(), starship_data, indent=4)

    def save_all_pages(self, page=None):
        response = self.get_all_species(page=page)
        with open(f'All_page_species.json', 'a') as starship_data:
            json.dump(response.json(), starship_data, indent=4)
        return response

    def save_all_pages_test(self, page=None):
        response = self.get_all_species(page=page)
        with open(f'Its_{page}_page.json', 'a') as starship_data:
            json.dump(response.json(), starship_data, indent=4)
        return response


    def compare_for_negative(self):
        with open('../tests_swapi/Not_found_page.json') as data:
            data_converted = json.load(data)
            return data_converted
