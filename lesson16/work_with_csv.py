import csv

"""скористайтесь pytest. напишіть функцію, яка додає в csv один рядок. Напишіть функцію, яка видаляє з csv один рядок.
напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився. в якості перевірного csv можете
скористатись доданим до завдання файлом або будь-яким іншим."""


class WorkWithCsv:
    def __init__(self, name):
        self.name = name

    def add_row_to_csv(self, line):
        line = [item.strip() for item in line]
        with open(self.name, 'a', newline='') as file:
            writer_row = csv.writer(file)
            writer_row.writerow(line)

    def delete_row(self):
        with open(self.name, 'r', newline='') as file:
            reader = list(csv.reader(file))
            reader.pop()

        with open(self.name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

    def count_row(self):
        with open(self.name, 'r', newline='') as file:
            reader = csv.reader(file)
            row_count = 0
            for row in reader:
                row_count += 1
        return row_count
