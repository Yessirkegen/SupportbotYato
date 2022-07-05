from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from dataBase import SQLighter
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ['подписаться', 'отписаться', 'предложения']
keyboard.add(*buttons)



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = SQLighter('db.db')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,f"Добро пожаловать {message.from_user.username}")
    await bot.send_message(message.from_user.id,"Как самочувствие?",reply_markup=keyboard)



@dp.message_handler(text="подписаться")
async def process_start_command(message: types.Message):
    await message.reply("Ты успешно подписался, теперь время от времени будешь получать вкусноту 😋")

    if(not db.subs_exists(message.from_user.id)):
        db.add_subs(message.from_user.id,message.from_user.username)
        #db.take_name(message.from_user.username)
    else:
        db.update_subs(message.from_user.id, True)

@dp.message_handler(text='отписаться')
async def process_start_command(message: types.Message):
        db.update_subs(message.from_user.id, False)
        await message.answer('Ты успешно отписался, не видать тебе больше лапши 🤨')

@dp.message_handler(text='предложения')
async def process_start_command(message: types.Message):
        await bot.send_message(message.from_user.id, 'При помощи команды "/offer (текст/ссылка)" вы можете предложить вашу мотивашку, слова поддержки и прочее, её после проверки получать все пользователи бота')
        await bot.send_message(message.from_user.id, 'Для того чтобы отправить изображение введите её в виде ссылки')

@dp.message_handler(commands=['send1430019068'])
async def process_start_command(message: types.Message):
    subscriptions = db.get_subscriptions()
    msg=message.text
    msg= msg[16:]
    print(msg)
    print(subscriptions)
    for s in subscriptions:
        await bot.send_photo(s[1], photo=msg)

@dp.message_handler(commands=['sendtxt1430019068'])
async def process_start_command(message: types.Message):
    subscriptions = db.get_subscriptions()
    msg=message.text
    msg=msg[18:]
    print(msg)
    print(subscriptions)
    for s in subscriptions:
        await bot.send_message(s[1], msg)


@dp.message_handler(commands=['db1430019068'])
async def process_start_command(message: types.Message):
    subscriptions = db.get_subscriptions()
    await bot.send_message('1430019068', subscriptions)


@dp.message_handler(commands=['offer'])
async def process_start_command(message: types.Message):
    if len(message.text)<=6:
        await bot.send_message(message.from_user.id, 'Предложение пусто, пожалуйста введите по форме "/offer (текст/ссылка)"')
    else:
        await bot.send_message('1430019068',message.from_user.username)
        await bot.send_message('1430019068', message.text)
        await bot.send_message(message.from_user.id, 'Ваше предложение успешно отправлено')





if __name__ == '__main__':
    executor.start_polling(dp)