
from DB import *
from tkinter import *

# создание базы и таблицы для карт
My_DB = DB()
My_DB.create_table('Flash_cards')
# My_DB.save_to_table('cat', 'кошка')


# описание окна
main_window = Tk()
main_window.title('Флеш-карты')
main_window.geometry('500x500+1000+200')
word_field = Entry(width=30, validate='key')  # окно ввода слова
word_field.place(x=100, y=100)
translate_field = Entry(width=30, validate='key')  # окно ввода слова перевода
# добавляем карточку в таблицу БД
Saver_button = Button(text='Сохранить')
Saver_button.bind(
    '<Button-1>', My_DB.save_to_table(world_value=word_field.get()))
Saver_button.place(x=100, y=300)

# вывод на экран
word_field.place(x=100, y=100)
translate_field.place(x=100, y=200)
main_window.mainloop()
