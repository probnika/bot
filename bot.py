from email import message
import tracemalloc
from imaplib import Commands
import random
from tkinter import Text
from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random

bot = Bot (token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(regexp='каталог')
async def say_hi(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ручные инструменты","Электроинструменты","Диски","Наборы","Ящики и сумки для инструментов","Биты","Инструменты для работы с материалами","Страховочные системы","Средства индивидуальной защиты","Прочее...","<НАЗАД"]
    keyboard.add(*buttons)
    await message.answer("вот что я могу предложить", reply_markup=keyboard)

@dp.message_handler(regexp='назад')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/help", "каталог", "промокоды"]
    keyboard.add(*buttons)
    await message.answer("что хотите узнать?", reply_markup=keyboard)

@dp.message_handler(regexp='Ручные инструменты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Отвертки","Пассатижи и плоскогубцы","Молотки и кувалды","Гаечные ключи","Бокорезы","Клещи","Тонкогубцы и круглогубцы","Шпатели","Штангенциркули","Строительные тёрки","Рулетки и мерные ленты","Трещотки и воротки","Торцевые головки и ключи","Струбцины","Стамески","Труборезы","Шестигранные и шлицевые ключи","Пинцеты","Монтажные ножи","Ножницы","Пилы и ножовки","Клещи для работы с кабелем","Болторезы","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Электроинструменты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Лобзики","Дрели","Аккумуляторы","Шуруповёрты","Гайковёрты","Строительный радиоприёмник","Сверлильный станок","Точило с двумя кругами","Лазерный уровень","Воздушные компрессоры","Установка для алмазного бурения","Детекторы","Строительные пылесосы","Строительный фен","Клеевые инструменты","Фонари и прожекторы","Электрические ножницы","МФИ","Рубанки","Гвоздескобозабивные пистолеты и степлеры","Циркулярные пилы","Системы пылеудаления","Шлифмашинки","Электрические краскопульты","Перфораторы","Болгарки","Фрезеры","Электрогенераторы","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Диски')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пильные диски","Диски отрезные","Шлифнасадки","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Наборы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Инструменты","Отвёртки"," Пассатижи","Клещи","Гаечные ключи","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Инструменты для работы с материалами')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Буры, долота, пики для перфораторов","Свёрла","Коронки","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Средства индивидуальной защиты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Маски и очки","Средства защиты","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Прочее')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Расходный материал","Электрические детали","Штативы, вехи, рейки","Инструментальные тележки","назад"]
    keyboard.add(*buttons)
    await message.answer("вот что есть по вашему запросу", reply_markup=keyboard)

@dp.message_handler(regexp='Отвертки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к отверткам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к отверткам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к отверткам", url="https://toolarmory-shop.ru/collection/otvyortki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Пассатижи и плоскогубцы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к пассатижам и плоскогубцам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к пассатижам и плоскогубцам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к пассатижам и плоскогубцам", url="https://toolarmory-shop.ru/collection/passatizhi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Молотки и кувалды')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к молоткам и кувалдам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к молоткам и кувалдам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к молоткам и кувалдам", url="https://toolarmory-shop.ru/collection/molotki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Гаечные ключи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к гаечным ключам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к гаечным ключам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к гаечным ключам", url="https://toolarmory-shop.ru/collection/gaechnye-klyuchi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Бокорезы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к бокорезам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к бокорезам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к бокорезам", url="https://toolarmory-shop.ru/collection/bokorezy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Шпатели')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к шпателям"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к шпателям')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к шпателям", url="https://toolarmory-shop.ru/collection/shpateli")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Клещи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к клещам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к клещам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к клещам", url="https://toolarmory-shop.ru/collection/kleschi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Тонкогубцы и круглогубцы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к тонкогубцам и круглогубцам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к тонкогубцам и круглогубцам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к тонкогубцам и круглогубцам", url="https://toolarmory-shop.ru/collection/kruglogubtsy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Штангенциркули')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к штангенциркулям"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к штангенциркулям')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к штангенциркулям", url="https://toolarmory-shop.ru/collection/shtangentsirkuli")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Строительные тёрки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к строительным тёркам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к строительным тёркам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к строительным тёркам", url="https://toolarmory-shop.ru/collection/stroitelnye-tyorki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Рулетки и мерные ленты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к рулеткам и мерные лентам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к рулеткам и мерные лентам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к рулеткам и мерные лентам", url="https://toolarmory-shop.ru/collection/ruletki-i-mernye-lenty")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Трещотки и воротки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к трещоткам и вороткам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к трещоткам и вороткам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к трещоткам и вороткам", url="https://toolarmory-shop.ru/collection/treschotki-i-vorotki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Торцевые головки и ключи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к торцевым головкам и ключам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к торцевым головкам и ключам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к торцевым головкам и ключам", url="https://toolarmory-shop.ru/collection/tortsevye-golovki-i-klyuchi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Струбцины')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к струбцинам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к струбцинам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к струбцинам", url="https://toolarmory-shop.ru/collection/strubtsiny")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Стамески')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к стамескам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к стамескам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к стамескам", url="https://toolarmory-shop.ru/collection/stameski")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Труборезы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к труборезам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к труборезам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к труборезам", url="https://toolarmory-shop.ru/collection/truborezy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Шестигранные и шлицевые ключи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к шестигранным и шлицевым ключам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к шестигранным и шлицевым ключам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к шестигранным и шлицевым ключам", url="https://toolarmory-shop.ru/collection/shestigrannye-i-shlitsevye-klyuchi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Пинцеты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к пинцетам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к пинцетам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к пинцетам", url="https://toolarmory-shop.ru/collection/pintsety")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Монтажные ножи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к монтажным ножам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к монтажным ножам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к монтажным ножам", url="https://toolarmory-shop.ru/collection/montazhnye-nozhi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Ножницы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к ножницам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к ножницам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к ножницам", url="https://toolarmory-shop.ru/collection/nozhnitsy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Пилы и ножовки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к пилам и ножовкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к пилам и ножовкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к пилам и ножовкам", url="https://toolarmory-shop.ru/collection/pily-i-nozhovki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Клещи для работы с кабелем')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к клещам для работы с кабелем"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к клещам для работы с кабелем')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к клещам для работы с кабелем", url="https://toolarmory-shop.ru/collection/avtomaticheskie-kleschi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Болторезы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к болторезам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к болторезам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к болторезам", url="https://toolarmory-shop.ru/collection/boltorezy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Шуруповёрты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к шуруповёртам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к шуруповёртам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к шуруповёртам", url="https://toolarmory-shop.ru/collection/shurupovyorty")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Лобзики')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к лобзикам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к лобзикам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к лобзикам", url="https://toolarmory-shop.ru/collection/lobziki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Дрели')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к дрелям"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к дрелям')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к дрелям", url="https://toolarmory-shop.ru/collection/dreli")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Аккумуляторы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к аккумуляторам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к аккумуляторам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к аккумуляторам", url="https://toolarmory-shop.ru/collection/akkumulyatory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Аккумуляторы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к аккумуляторам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к аккумуляторам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к аккумуляторам", url="https://toolarmory-shop.ru/collection/akkumulyatory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Гайковёрты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к гайковёртам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к гайковёртам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к гайковёртам", url="https://toolarmory-shop.ru/collection/gaykovyorty")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Строительный радиоприёмник')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к строительным радиоприёмникам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к строительным радиоприёмникам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к строительным радиоприёмникам", url="https://toolarmory-shop.ru/collection/stroitelnyy-radiopriyomnik")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Сверлильный станок')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к сверлильным станокам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к сверлильным станокам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к сверлильным станокам", url="https://toolarmory-shop.ru/collection/sverlilnyy-stanok")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Точило с двумя кругами')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к точилам с двумя кругами"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к точилам с двумя кругами')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к точилам с двумя кругами", url="https://toolarmory-shop.ru/collection/tochilo-s-dvumya-krugami")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Лазерный уровень')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к лазерным уровеням"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к лазерным уровеням')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к лазерным уровеням", url="https://toolarmory-shop.ru/collection/lazernyy-uroven")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Воздушные компрессоры')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к воздушным компрессорам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к воздушным компрессорам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к воздушным компрессорам", url="https://toolarmory-shop.ru/collection/vozdushnye-kompressory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Установка для алмазного бурения')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к установкам для алмазного бурения"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к установкам для алмазного бурения')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к установкам для алмазного бурения", url="https://toolarmory-shop.ru/collection/ustanovka-dlya-almaznogo-bureniya")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Строительные пылесосы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к строительным пылесосам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к строительным пылесосам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к строительным пылесосам", url="https://toolarmory-shop.ru/collection/stroitelnye-pylesosy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Строительный фен')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к строительным фенам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к строительным фенам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к строительным фенам", url="https://toolarmory-shop.ru/collection/stroitelnyy-fen")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Клеевые инструменты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к клеевым инструментам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к клеевым инструментам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к клеевым инструментам", url="https://toolarmory-shop.ru/collection/kleevye-instrumenty")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Фонари и прожекторы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к фонарям и прожекторам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к фонарям и прожекторам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к фонарям и прожекторам", url="https://toolarmory-shop.ru/collection/fonari-i-prozhektory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Электрические ножницы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к электрическим ножницам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к электрическим ножницам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к электрическим ножницам", url="https://toolarmory-shop.ru/collection/elektricheskie-nozhnitsy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='МФИ')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к МФИ"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к МФИ')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к МФИ", url="https://toolarmory-shop.ru/collection/mfi")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Рубанки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к рубанкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к рубанкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к рубанкам", url="https://toolarmory-shop.ru/collection/rubanki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Гвоздескобозабивные пистолеты и степлеры')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к гвоздескобозабивным пистолетам и степлерам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к гвоздескобозабивным пистолетам и степлерам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к гвоздескобозабивным пистолетам и степлерам", url="https://toolarmory-shop.ru/collection/gvozdeskobozabivnye-pistolety-i-steplery")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Системы пылеудаления')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к системам пылеудаления"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к системам пылеудаления')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к системам пылеудаления", url="https://toolarmory-shop.ru/collection/sistemy-pyleudaleniya")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Шлифмашинки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к шлифмашинкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к шлифмашинкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к шлифмашинкам", url="https://toolarmory-shop.ru/collection/shlifmashinki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Электрические краскопульты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к электрическим краскопультам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к электрическим краскопультам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к электрическим краскопультам", url="https://toolarmory-shop.ru/collection/elektricheskie-kraskopulty")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Перфораторы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к перфораторам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к перфораторам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к перфораторам", url="https://toolarmory-shop.ru/collection/perforatory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Болгарки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к болгаркам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к болгаркам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к болгаркам", url="https://toolarmory-shop.ru/collection/bolgarki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Фрезеры')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к фрезерам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к фрезерам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к фрезерам", url="https://toolarmory-shop.ru/collection/frezery")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Электрогенераторы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к электрогенераторам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к электрогенераторам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к электрогенераторам", url="https://toolarmory-shop.ru/collection/elektrogeneratory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Пильные диски')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к пильным дискам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к пильным дискам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к пильным дискам", url="https://toolarmory-shop.ru/collection/elektrogeneratory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Диски отрезные')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к дискам отрезным"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к дискам отрезным')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к дискам отрезным", url="https://toolarmory-shop.ru/collection/elektrogeneratory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Шлифнасадки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к шлифнасадкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к шлифнасадкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к шлифнасадкам", url="https://toolarmory-shop.ru/collection/shlifnasadki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Инструменты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к наборам инструментов"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к наборам инструментов')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к наборам инструментов", url="https://toolarmory-shop.ru/collection/nabory-instrumentov")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Отвёртки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к наборам отвёрток"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к наборам отвёрток')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к наборам отвёрток", url="https://toolarmory-shop.ru/collection/nabory-otvyortok")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Пассатижи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к наборам пассатижей"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к наборам пассатижей')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к наборам пассатижей", url="https://toolarmory-shop.ru/collection/nabory-passatizhey")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Гаечные ключи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к наборам гаечных ключей"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к наборам гаечных ключей')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к наборам гаечных ключей", url="https://toolarmory-shop.ru/collection/nabory-gaechnyh-klyuchey")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Клещи')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к наборам клещей"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к наборам клещей')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к наборам клещей", url="https://toolarmory-shop.ru/collection/nabory-kleschey")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Ящики и сумки для инструментов')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к ящикам и сумкам для инструментов"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к ящикам и сумкам для инструментов')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к ящикам и сумкам для инструментов", url="https://toolarmory-shop.ru/collection/yaschiki-dlya-instrumentov")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Буры, долота, пики для перфораторов')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к бурам, долотам, пикам для перфораторов"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к бурам, долотам, пикам для перфораторов')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к бурам, долотам, пикам для перфораторов", url="https://toolarmory-shop.ru/collection/bury-dolota-piki-dlya-perforatorov")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Свёрла')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к свёрлам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к свёрлам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к свёрлам", url="https://toolarmory-shop.ru/collection/svyorla-2")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Коронки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к коронкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к коронкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к коронкам", url="https://toolarmory-shop.ru/collection/koronki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Страховочные системы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к страховочным системам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к страховочным системам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к страховочным системам", url="https://toolarmory-shop.ru/collection/strahovochnye-sistemy")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Средства индивидуальной защиты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к средствам индивидуальной защиты"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к средствам индивидуальной защиты')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к средствам индивидуальной защиты", url="https://toolarmory-shop.ru/collection/sredstva-individualnoy-zaschity")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Маски и очки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к маскам и очкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к маскам и очкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к маскам и очкам", url="https://toolarmory-shop.ru/collection/maski-i-ochki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Биты')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к битам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к битам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к битам", url="https://toolarmory-shop.ru/collection/bity")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Расходный материал')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к расходным материалам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к расходным материалам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к расходным материалам", url="https://toolarmory-shop.ru/collection/rashodnyy-material")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Электрические детали')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к электрическим деталям"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к электрическим деталям')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к электрическим деталям", url="https://toolarmory-shop.ru/collection/elektronika")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Инструментальные тележки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к инструментальным тележкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к инструментальным тележкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к инструментальным тележкам", url="https://toolarmory-shop.ru/collection/instrumentalnye-telezhki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Штативы, вехи, рейки')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к штативам, вехам, рейкам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к штативам, вехам, рейкам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к штативам, вехам, рейкам", url="https://toolarmory-shop.ru/collection/shtativy-vehi-reyki")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(regexp='Детекторы')
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["назад","перейти к детекторам"]
    keyboard.add(*buttons)
    await message.answer("узнайте больше у нас на сайте", reply_markup=keyboard)

@dp.message_handler(regexp='Перейти к детекторам')
async def send_inline_keyboard(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти к детекторам", url="https://toolarmory-shop.ru/collection/detektory")
    keyboard_markup.add(url_button)
    await message.answer(text="Нажми на кнопку, чтобы перейти на сайт", reply_markup=keyboard_markup)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/help", "каталог", "промокоды"]
    keyboard.add(*buttons)
    await message.answer("что хотите узнать?", reply_markup=keyboard)

@dp.message_handler(regexp="промокоды")
async def process_reply(message: types.Message):
    await bot.send_message(message.from_user.id, 'На данный момент действующий промокод на 3% "TOOLARMORY"\n Который действует на все товары магазина!\n Приятных покупок!)')

@dp.message_handler(commands={'help'})
async def process_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'возникили проблемы?,\n можете обратиться к нашему менеджеру\n контакты https://t.me/Oleg_menager')

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    file_info = await bot.get_file(message.photo[-1].file_id)
    await message.photo[-1].download(file_info.file_path.split('photos/')[1]) # ++
    await bot.send_message(message.from_user.id, 'пожалуй сохраню')

@dp.message_handler(content_types=[types.ContentType.VIDEO])
async def handle_video(message: types.Message):
    await message.reply('пока я не умею распозновать видео, но скоро научусь)')

@dp.message_handler()
async def process_reply(message: types.Message):
    await bot.send_message(message.from_user.id, 'я тебя не понимаю!!!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)