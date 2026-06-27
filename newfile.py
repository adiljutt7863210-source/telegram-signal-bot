from telegram import Bot
import asyncio

TOKEN = "8689130185:AAHHoE5KBZdcKOcyTJX49w08aQCQWqNkxA4"

GROUP = "@pktrader2007"

async def main():
    bot = Bot(TOKEN)

    await bot.send_message(
        chat_id=GROUP,
        text="🚀 BUY SIGNAL\n\nPair: BTCUSDT\nEntry: 100000\nSL: 99000\nTP: 102000"
    )

asyncio.run(main())