#notifier.py
import os
from dotenv import load_dotenv
import telegram
import asyncio
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def format_job(job: dict)-> str:
    return (
        f"📌{job.get('title','N/A')}\n"
        f"🏢{job.get('company','N/A')}\n"
        f"📍{job.get('location','N/A')}\n"
        f"🔗{job.get('url','N/A')}"
        )

async def send_message(text: str):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID,text=text)

async def notify(jobs: list):
    for job in jobs:
        text = format_job(job)
        await send_message(text)

def run_notify(jobs: list):
    asyncio.run(notify(jobs))


    