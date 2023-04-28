# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying Sukoon Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About Sukoon**

🧿 Ultroid is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@Nillcoderbot**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/SukoonUserBot/7)
-> [Keeping Custom Addons Repo](https://t.me/SukoonUserBot/6)
-> [Disabling Deploy message](https://t.me/SukoonUserBot/8)
-> [Setting up TimeZone](https://t.me/SukoonUserBot/9)
-> [About Inline PmPermit](https://t.me/SukoonUserBot/10)
-> [About Dual Mode](https://t.me/SukoonUserBot/11)
-> [Custom Thumbnail](https://t.me/SukoonUserBot/12)
-> [About FullSudo](https://t.me/SukoonUserBot/13)
-> [Setting Up PmBot](https://t.me/SukoonUserBot/2)
-> [Also Check](https://t.me/SukoonUserBot/14)

**• To Know About Updates**
  - Join @Nillcoderbot.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@night_talks_m **.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
