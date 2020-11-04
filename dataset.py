import sqlite3
import config
import random


def random_inputs():
    num_a = random.uniform(-100.0, 100.0)
    num_b = random.uniform(-100.0, 100.0)
    _sum = num_a + num_b
    return (num_a, num_b, _sum)


class DataSet:
    def __init__(self, dataset_file):
        self.connection = sqlite3.connect(dataset_file)
        self.cursor = self.connection.cursor()

    def insert_to_dataset(self):
        with self.connection:
            for i in range(config.NUMBER_OF_DATASET_UNITS):
                self.cursor.execute("INSERT INTO dataset VALUES (?,?,?)", random_inputs())
            return True
    
    def read_from_dataset(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM dataset").fetchall()
    
    def close(self):
        self.connection.close()

