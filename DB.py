def create_DB(name_DB):
    import sqlite3
    base = sqlite3.connect(f'{name_DB}.db')
    cur = base.cursor


def create_table():
    pass


def save_to_BD():
    '''save card to data base'''
    pass
