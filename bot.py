import sys
import asyncio
import re
import time
import urllib.request
import urllib.parse
import urllib.error
import json
from telethon import TelegramClient, events

# --- SIZNING API MA'LUMOTLARINGIZ ---
API_ID = 36408779
API_HASH = 'ff492c10319c67711ff51caef8b88b79'
DOWNLOAD_DIR = "downloads"
# ------------------------------------

# Papka yaratish
import os
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Mijozni sozlash
client = TelegramClient('ai_userbot', API_ID, API_HASH)

# --- QO'SHIMCHA SOZLAMALAR (Oldin config.py da edi) ---
OLLAMA_URL = "http://localhost:11434/api/generate"
ENABLE_FILE_DOWNLOAD = True
ENABLE_MEDIA_SEARCH = True
BOT_INSTRUCTIONS = "Sen foydali yordamchisan."
FALLBACK_REPLY = "Kechirasiz, bu savolga javob bera olmayman."
USE_LOCAL_AI = False
FAST_REPLIES = {"salom": "Assalomu alaykum!", "qalesan": "Yaxshi, rahmat!"}
# -----------------------------------------------------

def clean_text(text):
    if not text: return ""
    cleaned = text.strip().lower()
    cleaned = re.sub(r'[^\w\s]', '', cleaned, flags=re.UNICODE)
    return cleaned

def extract_media_subject(text, keywords):
    cleaned = text.lower()
    for kw in keywords: cleaned = cleaned.replace(kw, "")
    fillers = ["tashla", "ber", "jo'nat", "qidir", "top", "rasmini", "fotosini", "videosini", "ashulasini", "qo'shig'ini", "qoshigini", "rasm", "foto", "musiqa", "qoshiq", "qo'shiq", "video", "klip", "mp3", "faylini", "fayl", "yuklab", "skachat", "qilib", "darsligi", "kitob"]
    for f in fillers: cleaned = cleaned.replace(f, "")
    return re.sub(r'\s+', ' ', cleaned).strip()

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0: return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} TB"

def get_progress_bar(percentage, length=10):
    filled_length = int(length * percentage // 100)
    bar = '█' * filled_length + '░' * (length - filled_length)
    return f"[{bar}] {percentage:.1f}%"

def ask_pollinations_ai(prompt, system_instruction, model_name="openai"):
    url = "https://text.pollinations.ai/"
    data = {"messages": [{"role": "system", "content": system_instruction}, {"role": "user", "content": prompt}], "model": "openai", "jsonMode": False}
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status == 200: return response.read().decode("utf-8")
    except: return None
    return None

async def download_file_chunked(url, filepath, status_message, client_instance, chat_id):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(None, lambda: urllib.request.urlopen(req, timeout=30))
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        with open(filepath, 'wb') as f:
            while True:
                chunk = await loop.run_in_executor(None, response.read, 1024 * 512)
                if not chunk: break
                f.write(chunk)
                downloaded += len(chunk)
        return True, total_size
    except: return False, 0

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handle_new_message(event):
    message_text = event.message.message
    if not message_text: return
    
    # AI orqali javob berish (Oddiy test)
    async with client.action(event.chat_id, 'typing'):
        reply_text = await asyncio.to_thread(ask_pollinations_ai, message_text, BOT_INSTRUCTIONS)
        if reply_text:
            await event.reply(reply_text.strip())
        else:
            await event.reply("Tushunmadim, qaytadan yozing.")

async def main():
    print("Bot ishga tushdi!")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
