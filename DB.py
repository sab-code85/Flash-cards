import sqlite3


class DB:
    """ База данных """

    def __init__(self):

        self.base = sqlite3.connect('My_DB.db')
        self.cur = self.base.cursor()

    def create_table(self, name_table):
        self.name_table = name_table
        self.base.execute('CREATE TABLE IF NOT EXISTS '
                          '{}(word PRIMARY KEY, translate, memorize_count)'.format(name_table))

    def save_to_table(self, world_value):
        self.cur.execute('INSERT INTO {} VALUES (?,?,?)'.format(self.name_table),
                         ('{}'.format(world_value), '544556', 100))
        self.base.commit()
