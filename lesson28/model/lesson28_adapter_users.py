import psycopg2
from lesson28.config import db_params


class NewSQLBase:
    def __init__(self):
        self.connect = psycopg2.connect(**db_params)

    def create_table(self):
        cursor = self.connect.cursor()
        cursor.execute("CREATE TABLE classwork28_sql_table(id varchar(50) primary key, "
                       "name varchar(50), "
                       "year integer,"
                       "price varchar(10),"
                       "color varchar(50),"
                       "description varchar(100));")
        self.connect.commit()
        self.connect.close()
        return print('New table created!')

    # Delete table
    def delete_table(self):
        cursor = self.connect.cursor()
        cursor.execute("DROP TABLE IF EXISTS classwork28_sql_table;")
        self.connect.commit()
        self.connect.close()

    # Insert data
    def insert_data(self):
        cursor = self.connect.cursor()
        cursor.execute("INSERT INTO classwork28_adapter_users2 (id, name, data) VALUES ('1','dddd', 'ccccc' );COMMIT;")

    # Select data
    def select_data(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT * FROM classwork28_adapter_users2;")
        self.connect.commit()
        for row in cursor.fetchall():
            print(row)
