from UltraUX-Spam-Bot import UltraUX01, UltraUX02, UltraUX03, UltraUX04, UltraUX05, UltraUX06, UltraUX07, UltraUX08, UltraUX09, UltraUX10, UltraUX11, UltraUX12, UltraUX13, UltraUX14, UltraUX15, UltraUX16, UltraUX17, UltraUX18, UltraUX19, UltraUX20, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime


SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
  
if UltraUX01:
      @UltraUX01.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX02:
      @UltraUX02.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
  
if UltraUX03:
      @UltraUX03.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX04:
      @UltraUX04.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX05:
      @UltraUX05.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX06:
      @UltraUX06.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX07:
      @UltraUX07.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
                  
else:
    pass
  
if UltraUX08:
      @UltraUX08.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX09:
      @UltraUX09.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX10:
      @UltraUX010.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX11:
      @UltraUX011.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX12:
      @UltraUX012.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX13:
      @UltraUX013.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX14:
      @UltraUX014.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
                  
else:
    pass
                  
if UltraUX15:
      @UltraUX015.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX16:
      @UltraUX016.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
  
if UltraUX17:
      @UltraUX017.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
                  
if UltraUX18:
      @UltraUX018.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
                  
if UltraUX19:
      @UltraUX019.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
                  
                  
else:
    pass
                  
if UltraUX20:
      @UltraUX20.on(events.NewMessage(pattern=".ping"))
      async def ping(e) :
        if e.sender_id in SMEX_USERS:
                  start = datetime.now()
                  text = "P-P-P-Pong!"
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  end = datetime.now()
                  ms = (end-start).microseconds / 1000
                  await event.edit(f"🤖 𝗣𝗼𝗻𝗴! 🤖\n`UltraUX Spam Bots are alive`\n Repo ->> https://github.com/noob-dv/UltraUX-Spam-Bot\n`{ms}` 𝗺𝘀")
                  
else:
    pass
