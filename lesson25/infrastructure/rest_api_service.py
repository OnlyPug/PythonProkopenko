import random

import requests
import json
from .json_information import JsonInformation


class Phone:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.headers = {'Content-Type': 'application/json'}
        self.json_data = JsonInformation()

    # GET

    def get_list_of_objects(self):
        return requests.get(self.base_url)

    def get_single_phone(self, device_id):
        return requests.get(f'{self.base_url}/{device_id}')

    def save_list_of_objects(self):
        response = self.get_list_of_objects()
        with open(f'List_of_object.json', 'w') as starship_data:
            json.dump(response.json(), starship_data, indent=4)
        return response

    def save_single_phone(self, device_id=None):
        response = self.get_single_phone(device_id=device_id)
        with open(f'Single_phone_id_{device_id}.json', 'w') as starship_data:
            json.dump(response.json(), starship_data, indent=4)
        return response

    # https://api.restful-api.dev/objects?id=3&id=5&id=10

    def get_list_of_device_ids(self, list_number=(3, 4, 10)):
        if len(list_number) == 3:
            return requests.get(f'{self.base_url}?id={list_number[0]}&id={list_number[1]}&id={list_number[2]}')
        if len(list_number) == 2:
            return requests.get(f'{self.base_url}?id={list_number[0]}&id={list_number[1]}')
        else:
            return print("Maybe use another method")

    def save_list_of_device_ids(self):
        response = self.get_list_of_device_ids()
        with open(f'Phone_id.json', 'w') as starship_data:
            json.dump(response.json(), starship_data, indent=4)
        return response

    # POST

    def create_new_object(self):
        return requests.post(url=self.base_url, headers=self.headers, data=json.dumps(self.json_data.data_for_post))

    def create_new_object_negative(self):
        return requests.post(url=self.base_url, headers=self.headers)

    # PUT

    def update_single_default_object(self):
        response_of_single_phone_object = self.create_new_object()
        return requests.put(f'{self.base_url}/{response_of_single_phone_object.json()["id"]}',
                            headers=self.headers, data=json.dumps(self.json_data.data_for_put))

    # PATCH

    def path_single_default_object(self):
        response_of_single_phone_object = self.create_new_object()
        return requests.patch(f'{self.base_url}/{response_of_single_phone_object.json()["id"]}',
                              headers=self.headers, data=json.dumps(self.json_data.data_for_path))

    # DELETE

    def delete_single_default_object(self):
        response_of_single_created_object = self.create_new_object()
        obj_id = response_of_single_created_object.json()["id"]
        return requests.delete(f'{self.base_url}/{obj_id}'), obj_id


film_name = ['Opengamer', 'Shrek', 'Tetris', 'PoorThings', 'Duna']

genre = ['Biographic', 'Comedian', 'History', 'Drama', 'Action']

rating = [9, 10, 7, 9, 10]


class Films:
    base_url = 'https://api.restful-api.dev/objects'

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.film_data = {'name': random.choice(film_name),
                          'data': {
                              'genre': random.choice(genre),
                              'rating': random.choice(rating)
                          }}
        self.films_response = requests.post(url=self.base_url, headers=self.headers, data=json.dumps(self.film_data))
        self._id = self.films_response.json()["id"]
        self._created_time = self.films_response.json()["createdAt"]

    @classmethod
    def generate_films_pack(cls):
        list_of_films = []
        for i in range(random.randint(4,20)):
            list_of_films.append(cls())
        return list_of_films

    @classmethod
    def filter_only_films(cls, list_of_films):
        filtration_url = cls.base_url + '?'
        for film in list_of_films:
            if film != list_of_films[-1]:
                filtration_url += f"id={film._id}&"
            else:
                filtration_url += f"id={film._id}"
        print(filtration_url)
        return requests.get(filtration_url)
