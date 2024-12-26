from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

st = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='Начать')]])

gm = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='Оставить')],
                                     [KeyboardButton(text='Добавить')]],
                           input_field_placeholder='Оставить/Добавить:')
