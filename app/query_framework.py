import sqlite3
class Database(object):
    """sqlite3 database class"""
    __DB_LOCATION = 'food.db'

    def __init__(self, db_location=None):
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.__DB_LOCATION)
        self._db = self.connection.cursor()

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def insert(self, row):
        self._db.execute(f'insert into {self._table} (dish_name, website) values (?, ?)',
                         (row['dish_name'], row['website']))
        self._db.commit()

    def retrieve_dish(self, key):
        cursor = self._db.execute(f'select * from {self._table} where dish_name = ?', (key,))
        return dict(cursor.fetchone())

    def retrieve_website(self, key):
        cursor = self._db.execute(f'select * from {self._table} where website = ?', (key,))
        return dict(cursor.fetchone())

    def update(self, row):
        self._db.execute(f'update {self._table} set website = ? where dish_name = ?',
                         (row['website'], row['dish_name']))
        self._db.commit()

    def delete(self, key):
        self._db.execute(f'delete from {self._table} where dish_name = ?', (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute(f'select * from {self._table}')
        for row in cursor:
            print(f"  {row['dish_name']}: {row['website']}")

    def __iter__(self):
        cursor = self._db.execute(f'select * from {self._table}')
        for row in cursor:
            yield dict(row)

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.Connection(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, t):
        self._table = t

    @table.deleter
    def table(self):
        self._table = 'test'

    def close(self):
        self._db.close()
        del self._filename
