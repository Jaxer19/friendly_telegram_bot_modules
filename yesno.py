from .. import loader, utils
import random


@loader.tds
class YesNoMod(loader.Module):
    """Помогает вам сделать важный жизненный выбор"""
    strings = {"name": "YesNo"}

    @loader.unrestricted
    async def yesnocmd(self, message):
        """Делает выбор жизни"""
        list = ["Yes", "No", "Of course yes", "Of course no"]
        decision = random.choice(list)
        await message.edit(str(decision))
