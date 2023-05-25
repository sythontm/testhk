
import telethon
from time import sleep

import requests
import heroku3



sython.start()

heroku_conn = heroku3.from_key(heroku_api_key)
app = heroku_conn.apps()[app_name]

@sython.on(events.NewMessage(outgoing=True, pattern=r"\تحديث"))
async def update(event):
    await event.edit("- جارِ تحديث السورس ...\n- انتضر من 1-2 دقيقة")
    await sython.disconnect()
    await sython.send_message(event.chat_id, "- تم تحديث السـورس .. بنجـاح")

@sython.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**〠**""")


sython.run_until_disconnected()
