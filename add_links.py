from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject
from models import AddBot
from tortoise.transactions import in_transaction


router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command("add"))
async def add_links(message: Message, command: CommandObject):
    async with in_transaction():
        await message.answer("I am starting")
        user_info_db = await AddBot.filter(user_id=message.from_user.id).first()
        print(user_info_db)
        user_id = message.from_user.id
        username = message.from_user.username
        print(username)
        first_name = message.from_user.first_name
        print(first_name)
        links = command.args
        print(links)
        all_users_count = await AddBot.all().count()

        await AddBot.create(
            id=all_users_count + 1,
            user_id=user_id,
            first_name=first_name,
            username=username,
            links=links)

        if message.from_user and message.from_user.username != user_info_db.username:
            user_info_db.username = username
            await user_info_db.save()



