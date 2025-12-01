from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from aiogram.filters import Command
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated
from IsAdmin import IsAdmin
from NumbersFilter import NumbersFilter
import logging
import logging.config
import dotenv
import os
from logging_settings import logging_config

dotenv.load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

#class ErrorFilter(logging.Filter):
#    def filter(self, record):
#        return record.levelname == "ERROR" and "важно" in record.msg.lower() or record.dop
logger = logging.getLogger(__name__)

logging.config.dictConfig(logging_config)

'''stderr_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs.log')
#file_handler.addFilter(ErrorFilter())

format_1='[{asctime}] #{levelname:8} {filename}:'\
            '{lineno} - {name} - {message}'
formatter_1 = logging.Formatter(
    fmt=format_1,
    style = '{'
    )


#stderr_handler.setFormatter(formatter_1)
#file_handler.setFormatter(formatter_1)

#logger.addHandler(stderr_handler)
#logger.addHandler(file_handler)'''

admin_list : list[int] = [1204095743]

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_command_start(message: Message):
    await message.answer('Это команда /start')
    print(message.from_user.id)
    logger.error('важно! Это DEBUG сообщение')


# Этот хэндлер будет срабатывать на команду "|start"
@dp.message(Command(commands='start', prefix='|'))
async def process_command_start_2(message: Message):
    await message.answer('И это команда |start')
    try:
        print(4/2)
        print(4/0)
    except Exception:
        logger.exception('ошибка в делении!')


@dp.message(F.text.lower().startswith('найди числа'), NumbersFilter())
async def process_find_numbers(message : Message, num : list[int]):
    await message.answer(f'Нашел такие числа: {', '.join(str(number) for number in num)}')

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')

@dp.message(IsAdmin(admin_list))
async def procces_admin_message(message : Message):
    await message.answer('Вы админ!')

if __name__ == '__main__':
    dp.run_polling(bot)