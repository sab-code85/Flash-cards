import sqlite3


class DB:
    """ База данных """

    def __init__(self):

        self.base = sqlite3.connect('My_DB.db')
        self.cur = self.base.cursor

    def create_table(self, x):
        self.base.execute('CREATE TABLE IF NOT EXISTS '
                          '{}(word, translate, memorize_count)'.format(x))

        pass

    def save_to_BD(self):
        '''save card to data base'''
        pass
