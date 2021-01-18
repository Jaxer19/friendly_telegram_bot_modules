from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
from time import sleep


@borg.on(admin_cmd("ping"))
async def _(event):
    if event.fwd_from:
        return
    a = datetime.now()
    await event.edit("`Соединение...`")
    b = datetime.now()
    c = (b - a).microseconds / 1000
    sleep(1.1)
    await event.edit("**PONG: {}ms**".format(c))
