import asyncio

from collections import deque

from telethon.tl.functions.users import GetFullUserRequest

from . import eor, legend, mention

menu_category = "fun"

@legend.legend_cmd(

    pattern="bsdk$",

    command=("bsdk", menu_category),

    info={

        "header": "Created for myself ...... Hehe 👀 👀",

        "usage": "{tr}ki",

    },

)

async def _(event):

    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await event.edit("bsdk oyy")

        await asyncio.sleep(1.4)

        await event.edit("fuck off bsdk ")

        await asyncio.sleep(0.4)

        await event.edit("😡😡😡🔥")

        await asyncio.sleep(1.3)

        await event.edit("jhantu lode")

        await asyncio.sleep(0.4)

        await event.edit("@Atharva_xD sabka baap")

        await asyncio.sleep(1.3)

        await event.edit(

            "Nikal chl🤬"

        )
