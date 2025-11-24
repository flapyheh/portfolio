from aiogram.types import Message
from aiogram.filters import BaseFilter

class NumbersFilter(BaseFilter):
    async def __call__(self, message : Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',','').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'num': numbers}
        else:
            return False