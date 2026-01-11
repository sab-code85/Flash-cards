
from DB import *
from tkinter import *
print('1')
# создание базы и таблицы для карт
My_DB = DB()
My_DB.create_table('Flash_cards')
# My_DB.save_to_table('cat', 'кошка')


# описание окна
main_window = Tk()
main_window.title('Флеш-карты')
main_window.geometry('500x500+1000+200')
word_field = Entry(width=30)  # окно ввода слова
word_field.place(x=100, y=100)
translate_field = Entry(width=30)  # окно ввода перевода
translate_field.place(x=100, y=200)


def save_new_card(event):  # событие добавления данных из полей
    w = word_field.get()
    t = translate_field.get()
    My_DB.save_to_table(w, t)


# создаем кнопку для добавления карточки в таблицу БД
Saver_button = Button(text='Сохранить')
Saver_button.bind('<Button-1>', save_new_card)
Saver_button.place(x=100, y=300)


# вывод на экран
main_window.mainloop()
