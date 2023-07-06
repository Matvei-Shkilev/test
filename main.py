import asyncio
import logging
from aiogram import Dispatcher, Bot
from tortoise import Tortoise, run_async
from middlewares import RegistrationMiddlewares, WeekendMessageMiddleware,\
    WeekendCallbackMiddleware
from handlers import question, group_game, usernames, checkin, bot_in_group,\
    events_in_group, admin_change_in_group, add_links


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token="5581237873:AAH3-yhUgx3w6coRPWDFIdrnjp_CYXA2xI0")
    dp = Dispatcher()
    dp.include_routers(question.router, usernames.router, group_game.router, checkin.router,
                       bot_in_group.router, add_links.router,
                       admin_change_in_group.router, events_in_group.router)
    dp.message.outer_middleware(RegistrationMiddlewares())
    dp.message.middleware(WeekendMessageMiddleware())
    dp.message.outer_middleware(WeekendCallbackMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def setup_db():
    """Инициализация бд"""
    await Tortoise.init(
        db_url="sqlite://database/db.sqlite",
        modules={"models": [
            "models",
        ]},
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(setup_db())
    asyncio.run(main())
