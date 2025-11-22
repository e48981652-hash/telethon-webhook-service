"""
برنامج إنشاء Telethon Session File
يستخدم للمرة الأولى فقط لتفعيل الحساب
"""

import asyncio
from telethon import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('TELEGRAM_API_ID'))
API_HASH = os.getenv('TELEGRAM_API_HASH')
PHONE = os.getenv('TELEGRAM_PHONE')
SESSION_NAME = os.getenv('SESSION_NAME', 'sessions/telethon_session')


async def main():
    print("\n" + "="*50)
    print("🔐 Telethon Session Setup")
    print("="*50)
    print(f"📱 Phone: {PHONE}")
    print(f"📁 Session: {SESSION_NAME}.session")
    print("="*50 + "\n")
    
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    
    try:
        print("🔗 جاري الاتصال بـ Telegram...")
        await client.start(phone=PHONE)
        
        print("✅ تم التفعيل بنجاح!")
        print(f"📁 تم حفظ الـ Session في: {SESSION_NAME}.session\n")
        
        me = await client.get_me()
        print(f"👤 User ID: {me.id}")
        print(f"👤 Name: {me.first_name}")
        print("\n✨ جاهز للاستخدام!\n")
        
        await client.disconnect()
    except Exception as e:
        print(f"❌ خطأ: {e}\n")
        raise


if __name__ == "__main__":
    asyncio.run(main())