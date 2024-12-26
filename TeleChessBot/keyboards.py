from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='Мат в 1 ход')],
                                       [KeyboardButton(text='Мат в 2 хода'),
                                       KeyboardButton(text='Мат в 4 хода')],
                                       [KeyboardButton(text='Наименования фигур')]],
                           input_field_placeholder='Выберете тип задачи:')

rep = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='Показать ответ'),
                                       KeyboardButton(text='Наименования фигур')],
                                      [KeyboardButton(text='Назад')]])
back = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='Назад')]])
