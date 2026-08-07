# Senior Informatika Yordamchi — Telegram Bot

Bu bot senior (yuqori/universitet) darajadagi informatika fani bo'yicha ikki xil rejimda yordam beradi:

1. **🤖 AI yordamchi** — istalgan mavzuda (algoritmlar, OOP, ma'lumotlar bazalari, tarmoqlar, OT va h.k.) erkin savol-javob. Google Gemini API orqali ishlaydi.
2. **📝 Test rejimi** — 5 ta mavzu bo'yicha tayyor variantli savollar, natija va tushuntirish bilan.

## 1. Talablar

- Python 3.10 yoki undan yuqori
- Telegram bot tokeni ([@BotFather](https://t.me/BotFather) orqali olinadi)
- Gemini API kaliti (AI rejimi ishlashi uchun; https://aistudio.google.com/apikey — bepul olish mumkin)

## 2. O'rnatish

```bash
cd informatika_bot
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Sozlash

Muhit o'zgaruvchilarini o'rnating:

```bash
export TELEGRAM_BOT_TOKEN="sizning_bot_tokeningiz"
export GEMINI_API_KEY="sizning_gemini_api_kalitingiz"
```

Windows PowerShell uchun:
```powershell
$env:TELEGRAM_BOT_TOKEN="sizning_bot_tokeningiz"
$env:GEMINI_API_KEY="sizning_gemini_api_kalitingiz"
```

> Eslatma: Agar `GEMINI_API_KEY` sozlanmasa, bot baribir ishga tushadi, lekin AI yordamchi rejimi ishlamaydi — faqat test rejimi ishlaydi.

> Gemini API kalitini olish uchun: https://aistudio.google.com/apikey ga o'ting, Google hisobingiz bilan kiring va **Create API key** tugmasini bosing. Bu xizmat bepul limit (free tier) bilan ham ishlaydi.

## 4. Ishga tushirish

```bash
python bot.py
```

Bot ishga tushgach, Telegram'da botingizga `/start` buyrug'ini yuboring.

## 5. Buyruqlar

| Buyruq | Vazifasi |
|---|---|
| `/start` | Bosh menyuni ko'rsatadi |
| `/ai` | AI yordamchi rejimiga o'tadi |
| `/quiz` | Test rejimini boshlaydi (mavzu tanlash) |
| `/help` | Yordam matnini ko'rsatadi |

## 6. Test savollarini kengaytirish

Yangi savollar yoki mavzular qo'shish uchun `quiz_data.py` faylini tahrirlang. Har bir savol quyidagi formatda:

```python
{
    "question": "Savol matni?",
    "options": ["Variant A", "Variant B", "Variant C", "Variant D"],
    "correct": 1,  # to'g'ri javobning indeksi (0 dan boshlanadi)
    "explanation": "To'g'ri javob nima uchun to'g'ri ekanligi haqida tushuntirish."
}
```

Yangi mavzu qo'shish uchun `QUIZ_TOPICS` lug'atiga yangi kalit qo'shing:

```python
"yangi_mavzu": {
    "title": "🔧 Yangi mavzu nomi",
    "questions": [...]
}
```

## 7. Botni doimiy ishlashi uchun (production)

Uzoq muddatli ishlatish uchun serverda (masalan, VPS, Railway, Render) `systemd` xizmati sifatida yoki `screen`/`tmux` ichida ishga tushirishingiz mumkin. Katta yuk uchun `run_polling` o'rniga webhook (`run_webhook`) usulidan foydalanishni ko'rib chiqing.

## 8. Fayllar tuzilishi

```
informatika_bot/
├── bot.py            # Asosiy bot logikasi
├── quiz_data.py       # Test savollari bazasi
├── requirements.txt   # Python kutubxonalari
└── README.md          # Ushbu qo'llanma
```
