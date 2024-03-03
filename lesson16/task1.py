"""1 завдання. Напишіть адаптер, який конвертує json в csv. тобто робить зворотню конвертацію від тієї,
що ми реалізували на уроці. Приклад з уроку, а також json і csv додано, формат запису даних той самий."""
import json
import csv


class JsonConverter:
    def __init__(self):
        self.lines = []

    def read_json_file(self, file_name):
        with open(file_name, 'r') as json_file:
            self.lines = json.load(json_file)

    def write_csv_file(self, file_name):
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.lines[0].keys())
            for value in self.lines:
                writer.writerow(value.values())
                self.cleanup()

    def cleanup(self):
        self.lines = []


json1 = JsonConverter()
json1.read_json_file('example.json')
json1.write_csv_file('csv_from_json.csv')
