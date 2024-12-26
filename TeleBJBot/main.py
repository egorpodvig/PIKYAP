import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

bot = Bot(token='7807663047:AAHmbxjW9ws2y_lZnS0BrADgda13GooNQX4')
dp = Dispatcher()

class bj():
    cards = []
    a = []
    b = []

def arr():
    cards = []
    check = [2, 3, 4, 5, 6, 7, 8, 9, 11]
    for i in range(9):
        for j in range(4):
            cards.append(check[i])
    for i in range(16):
        cards.append(10)
    cards = random.sample(cards, len(cards))
    print(cards)
    return cards

def game(c):
    a = []
    b = []
    a[0:2] = c[0: 2]
    b[2:4] = c[2: 4]
    print(a[0], '  *')
    print(b)
    return a, b
game(arr())

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, этот бот может сыграть с тобой в Black Jack!', reply_markup=kb.st)

@dp.message(F.text == 'Начать')
async def cmd_start(message: Message):
    bj.cards = arr()
    bj.a, bj.b = game(bj.cards)
    await message.answer(text='Карты диллера: ')
    await message.answer(bj.a[0], '*')
    await message.answer(text='Твои карты:  ', reply_markup=kb.st)
    await message.answer(bj.a[0], '*')

@dp.message(F.text == 'Оставить')
async def cmd_start(message: Message):
    await message.answer(text='Карты диллера: ', reply_to_message_id = bj.a[0:])

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')


