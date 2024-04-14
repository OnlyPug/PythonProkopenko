import json

import psycopg2
import requests
from lesson28.config import db_params
from lesson28.infrastructure import JsonInformation


class ApiAdaptor:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.headers = {'Content-Type': 'application/json'}
        self.connect = psycopg2.connect(**db_params)
        self.json_data = JsonInformation()

    # POST+GET=>INSERT

    def create_new_object(self):
        post_response = requests.post(url=self.base_url, headers=self.headers,
                                      data=json.dumps(self.json_data.data_for_post))
        if post_response.status_code == 200:
            object_id = post_response.json()['id']
            print(object_id)
            get_response = requests.get(f"{self.base_url}/{object_id}")
            if get_response.status_code == 200:
                name = get_response.json()['name']
                year = str(get_response.json()['data']['year'])
                price = get_response.json()['data']['price']
                color = str(get_response.json()['data']['color'])
                description = str(get_response.json()['data']['description'])
                with self.connect.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO classwork28_sql_table (id, name, year, price, color, description) "
                        f"VALUES ('{object_id}','{name}','{year}','{price}','{color}','{description}');COMMIT;", )
            return print('New row on SQL created')

    # SELECT
    def select_data(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT * FROM classwork28_sql_table;")
        self.connect.commit()
        for row in cursor.fetchall():
            print(row)

    # PUT+GET=>UPDATE+SELECT

    def update_object(self, object_id):
        post_response = requests.put(f'{self.base_url}/{object_id}', headers=self.headers,
                                     data=json.dumps(self.json_data.data_for_put))
        if post_response.status_code == 200:
            name = str(post_response.json()['name'])
            year = str(post_response.json()['data']['year'])
            price = str(post_response.json()['data']['price'])
            with self.connect.cursor() as cursor:
                cursor.execute(f"UPDATE classwork28_sql_table SET name = '{name}', year = '{year}', price ='{price}' WHERE id ='{object_id}'")
                self.connect.commit()
        return print('Update row on SQL')

    # UPDATE+SELECT=>PUT+GET

    def update_from_object(self, object_id):
        with self.connect.cursor() as cursor:
            name = 'Cat'
            year = '2024'
            price = 'over-price'
            description = 'Warm, nice, sweet and sleepy'
            cursor.execute(
                f"UPDATE classwork28_sql_table SET name = '{name}', year = '{year}', price ='{price}', description='{description}' WHERE id ='{object_id}'")
            self.connect.commit()
            cursor.execute(f"SELECT * FROM classwork28_api_table_test WHERE id ='{object_id}';")
            self.connect.commit()
            for row in cursor.fetchall():
                print(row)
                result_sql = row
                object_id, name, year, price, color, description = result_sql
            data_for_put = {
                "name": name,
                "data": {
                    "year": year,
                    "price": price
                }
            }
            post_response = requests.put(f'{self.base_url}/{object_id}', headers=self.headers,
                                         data=json.dumps(data_for_put))
            return print(post_response.json())




