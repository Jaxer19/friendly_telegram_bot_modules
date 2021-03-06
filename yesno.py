from .. import loader, utils
import random


@loader.tds
class YesNoMod(loader.Module):
    """Помогает вам сделать жизненный выбор"""
    strings = {"name": "YesNo"}

    @loader.unrestricted
    async def yncmd(self, message):
        list = ["Да", "Нет"]
        decision = random.choice(list)
        await message.edit(str(decision))
