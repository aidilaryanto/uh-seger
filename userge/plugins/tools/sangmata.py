""" Sangmata """
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import userge, Message


@userge.on_cmd("sg", about={
    'header': "Sangmata gives you user info , last updated names.",
    'usage': "{tr}sg [Reply to user]"})
async def sangmata_(message: Message):
    """ Get User's Updated previous Names """
    replied = message.reply_to_message
    if not replied:
       await message.err("```Reply to Media to deepfry !...```", del_in=5)
       return
    if not replied.text:
       await message.err("```Reply to Text message only !...```", del_in=5)
       return
    user = replied.from_user.id
    chat = "@Sangmatainfo_bot"
    await message.edit("```Getting info, Wait plox ...```", del_in=3)
    

    async with userge.conversation(chat) as conv:
        try:
            await conv.send_message("/search_id {}".format(user))
        except YouBlockedUser:
            await message.err("**For your kind information, you blocked @Sangmatainfo_bot, Unblock it**", del_in=5)
            return
        msg1 = await conv.get_response()
        msg2 = await conv.get_response()
        msg3 = await conv.get_response()
        for msg in (msg1, msg2, msg3):
        	if msg.text.startswith("Name History"):
        		get_msg = await userge.get_messages(chat, msg.message_id)
        		await userge.send_message(message.chat.id, "`{}`".format(get_msg.text), reply_to_message_id=replied.message_id)
