from playwright.async_api import async_playwright
import asyncio
import os

async def run():
    phone_number = input("📱 Enter the phone number to scan QR and save session: ").strip()
    session_dir = f"whatsapp_session_{phone_number}"

    # 🛑 Removed deletion of old session
    # if os.path.exists(session_dir):
    #     shutil.rmtree(session_dir)
    #     print(f"🧹 Old session for {phone_number} deleted.")

    async with async_playwright() as p:
        print("🚀 Launching browser for QR scan...")
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=session_dir,
            headless=False
        )
        page = await browser.new_page()
        await page.goto("https://web.whatsapp.com")

        print("📲 Please scan the QR code in the opened browser.")
        print("❗ DO NOT close the browser manually. Once scanned, just close this terminal window or hit Ctrl+C to exit.")

        # Keep browser open for manual scan
        while True:
            await asyncio.sleep(1)

asyncio.run(run())

