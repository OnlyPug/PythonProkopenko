from lesson16.work_with_csv import WorkWithCsv


class TestScv:
    def setup_method(self):
        self.csv = WorkWithCsv('example.csv')

    def test_delete_row(self):
        count = self.csv.count_row()
        if count == 0:
            print('We don`t have what delete')
        else:
            self.csv.delete_row()
            count_line = count - 1
            assert count_line == self.csv.count_row()

    def test_add_row(self):
        count1 = self.csv.count_row()
        result = count1 + 1
        self.csv.add_row_to_csv(['Vika', 'Chin', '25', 'Female', '3000'])
        count2 = self.csv.count_row()
        assert result == count2


