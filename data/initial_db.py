import os
from secret import secret
from helpers import dbs
import sqlite3

class Database(object):
    """sqlite3 database class"""
    __DB_LOCATION = 'food.db'

    def __init__(self, db_location=None):
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.commit()
        self.connection.close()

    def close(self):
        self.connection.close()

    def execute(self, new_data):
        self.cur.execute(new_data)

    def executemany(self, table, many_new_data):
        self.create_table(table)
        self.cur.executemany(f"insert into {table} (id, dish_name, website) values (null, ?, ?)", many_new_data)

    def create_table(self, table):
        query = f"create table if not exists {table} (id integer primary key, dish_name text, website text)"
        self.execute(query)

    def drop_if(self, table):
        query = f"drop table if exists {table}"
        self.execute(query)

    def commit(self):
        self.connection.commit()


def main():
    with Database(secret['database']) as db:
        db.drop_if('fish')
        db.drop_if('beef')
        db.drop_if('chicken')
        db.drop_if('pork')
        db.drop_if('vegetarian')
        db.commit()
        db.executemany('fish', dbs['fish'])
        db.executemany('beef', dbs['beef'])
        db.executemany('chicken', dbs['chicken'])
        db.executemany('pork', dbs['pork'])
        db.executemany('vegetarian', dbs['vegetarian'])
        db.commit()


if __name__ == "__main__":
    main()
