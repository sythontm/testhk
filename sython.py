
import telethon
from time import sleep

import requests
import heroku3



sython.start()

heroku_conn = heroku3.from_key(heroku_api_key)
app = heroku_conn.apps()[app_name]

@sython.on(events.NewMessage(pattern='\.تحديث'))
async def update(event):
    await event.respond('جارٍ التحديث...')
    app.builds().create(source_blob={"url": "https://github.com/sythontm/testhk"})
    await event.respond('تم التحديث بنجاح!')


@sython.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**〠**""")


sython.run_until_disconnected()
