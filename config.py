# Telegram API ma'lumotlari (https://my.telegram.org saytidan olingan)
API_ID = 36408779  # API ID (faqat raqam)
API_HASH = 'ff492c10319c67711ff51caef8b88b79'  # API Hash (matn)

# ==================== O'ZBEKCHA AI PERSONA (FEW-SHOT PROMPTING) ====================
# Sun'iy intellekt o'zbekcha gaplarni buzib gapirmasligi uchun aniq qoidalar va namunalar
BOT_INSTRUCTIONS = """
Siz Telegram userbotning juda aqlli, samimiy va muloyim AI asistentisiz. Egangingiz hozir tarmoqda emas. 
Siz uning nomidan do'stona, juda qisqa va eng asosiysi TABIIY o'zbek tilida javob berishingiz kerak.

O'ZBEK TILI QOIDALARI:
1. Har doim jonli, insoniy va do'stona o'zbek tilida gapiring.
2. Sun'iy yoki robotga o'xshash so'zlardan qoching.
3. Ruscha yoki inglizcha so'zlarni to'g'ridan-to'g'ri o'zbekchaga so'zma-so'z tarjima qilmang.
4. Javobingiz juda qisqa bo'lsin (maksimal 1 yoki 2 ta gap). Uzun xabarlar yozmang.

SUHBAT NAMUNALARI:
Suhbatdosh: "salom, ishlar qalay?"
Siz: "Salom! Rahmat, zo'r. O'zingizda nima gaplar? Hozir egamiz bandroq edi, kelgach yozadi."

Suhbatdosh: "savolim bor edi"
Siz: "Bemalol yozib qoldiravering, egamiz ko'rishi bilan batafsil javob beradi."
"""

# ==================== AI ISHLASH REJIMI ====================
# True  - Kompyuteringizdagi Oflayn AI (Ollama) orqali ishlaydi (Internet shart emas!)
# False - Onlayn bepul AI (Pollinations) orqali ishlaydi (Internet kerak!)
USE_LOCAL_AI = True

# Oflayn Ollama Sozlamalari (Faqat USE_LOCAL_AI = True bo'lganda ishlaydi)
OLLAMA_URL = "http://localhost:11434/api/chat"

# TAVSIYA: O'zbekchani daho darajasida bilishi va muammosiz gapirishi uchun "qwen2.5:14b" yoki "qwen2.5:7b" yuklab oling!
# CMD buyrug'i: ollama run qwen2.5:14b  yoki  ollama run qwen2.5:7b
LOCAL_MODEL = "qwen2.5:14b"

# Onlayn Bepul AI Sozlamalari (Faqat USE_LOCAL_AI = False bo'lganda ishlaydi)
AI_MODEL = 'gpt-4o-mini'
# ============================================================

# ==================== MEDIA VA FAYL TIZIMI ====================
# Bot foydalanuvchilar rasm, musiqa, video yoki katta fayllarni so'rashganda internetdan qidirib yuklab topsinmi?
ENABLE_MEDIA_SEARCH = True
ENABLE_FILE_DOWNLOAD = True

# Fayllar vaqtincha saqlanadigan papka nomi
DOWNLOAD_DIR = "bot_downloads"
# ============================================================

# Tezkor va tayyor javoblar ro'yxati (Kutmasdan darhol javob berish uchun)
FAST_REPLIES = {
    "salom": "Salom! Men Boxoviddin ning menejeriman. Nima gapingiz bor edi? Yozib qoldirsangiz, o'ziga yetkazib qo'yaman. 🤝",
    "assalomu alaykum": "Va alaykum assalom! Men Boxoviddin ning menejeriman. Nima gapingiz bor edi? Yozib qoldirsangiz, o'ziga yetkazib qo'yaman. 🤝",
    "qalaysiz": "Yaxshi, rahmat! Men Boxoviddin ning menejeriman. Nima gapingiz bor edi? Yozib qoldirsangiz, o'ziga yetkazib qo'yaman.",
    "ishlar qalay": "Zo'r, rahmat! Ishlar bilan charchamayapsizmi? Boxoviddin ga biror narsa yetkazishim kerakmi?",
    "rahmat": "Arziydi! Doimo xizmatga tayyorman. 😊",
    "kim bu": "Men Boxoviddin ning avtomatik menejeriman. Egam kelishi bilan xabaringizni o'qiydi. 👤",
    "qayerdasan": "Men raqamli dunyoda, Boxoviddin ni kutib o'tiribman. 💻",
    "nima qilayapsan": "Xabarlaringizni qabul qilib, egamga yetkazishga tayyor turibman. ✅",
    "yordam kerak": "Albatta, yozib qoldiring. Boxoviddin kelgach, darhol ko'rib chiqadi. 📩",
    "qachon javob berasiz": "Egam kelishi bilan xabaringizni o'qiydi va sizga javob qaytaradi. ⏳",
    "xayr": "Xayr! Yana bog'lanamiz, salomat bo'ling. 👋"
}
# Sun'iy intellekt xizmatida xatolik yuz berganda qaytariladigan zaxira xabar
FALLBACK_REPLY = "Hozircha aloqaga chiqa olmayman, birozdan so'ng o'zim yozaman. Rahmat!"
