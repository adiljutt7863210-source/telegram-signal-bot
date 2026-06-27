import asyncio
from telegram import Bot

TOKEN="8689130185:AAEWVqNBhrsM3jEd2ZgocXMGUtHc8V6H6AY"
GROUP_ID = "@pktrader2007"

MESSAGE = """🚀 BUY SIGNAL

Pair: BTCUSDT
Entry: 100000
SL: 99000
TP: 102000
"""

async def main():
    bot = Bot(token=TOKEN)

    while True:
        await bot.send_message(
            chat_id=GROUP_ID,
            text=MESSAGE
        )
        print("Message Sent")
        await asyncio.sleep(3600)  # ہر 1 گھنٹے بعد

if __name__ == "__main__":
    asyncio.run(main())