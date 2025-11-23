from aiogram import Bot, Dispatcher
from aiogram.types import Message

from aiogram.filters import Command
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated

BOT_TOKEN = '8427217382:AAHAXqthQfTDXY8wIgT543409ocSV5x8urU'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_command_start(message: Message):
    await message.answer('Это команда /start')


# Этот хэндлер будет срабатывать на команду "|start"
@dp.message(Command(commands='start', prefix='|'))
async def process_command_start_2(message: Message):
    await message.answer('И это команда |start')


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')




if __name__ == '__main__':
    dp.run_polling(bot)