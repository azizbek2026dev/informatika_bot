"""
Senior darajadagi Informatika fani bo'yicha yordamchi Telegram bot.

Ikkita asosiy rejim:
  1) AI yordamchi — foydalanuvchi istalgan informatika mavzusida savol beradi,
     bot Google Gemini API orqali javob qaytaradi.
  2) Test rejimi — sinf (5-11) tanlanadi, o'sha sinf darsligi mavzulariga oid
     natija (ball) hisoblanadi.

Ishga tushirish uchun README.md faylidagi ko'rsatmalarga qarang.
"""

import asyncio
import logging
import os

from telegram import (
    BotCommand,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from quiz_data import QUIZ_TOPICS

try:
    from google import genai
    from google.genai import types as genai_types
except ImportError:  # google-genai kutubxonasi o'rnatilmagan bo'lsa ham bot ishga tushsin
    genai = None
    genai_types = None

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# --- Konfiguratsiya ---
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
AI_MODEL = "gemini-2.0-flash"
MAX_OUTPUT_TOKENS = 8192

SYSTEM_PROMPT = (
    "Siz senior (oxirgi bosqich/universitet darajasidagi) informatika fani bo'yicha "
    "tajribali o'qituvchisiz. Foydalanuvchiga algoritmlar, ma'lumotlar tuzilmalari, "
    "OOP, ma'lumotlar bazalari, tarmoqlar, operatsion tizimlar va dasturlash mavzularida "
    "aniq, tushunarli va ilmiy jihatdan to'g'ri javob bering. Javoblaringizni o'zbek "
    "tilida, lo'nda va tuzilgan tarzda (kerak bo'lsa misollar bilan) bering. Agar savol "
    "kod yozishni talab qilsa, kodni tushuntirish bilan birga taqdim eting. "
    "MUHIM: javobingizda Markdown belgilaridan (**, ###, __, - ro'yxat belgisi va h.k.) "
    "foydalanmang, chunki javob Telegram xabari sifatida oddiy matnda ko'rsatiladi. "
    "Sarlavhalar o'rniga oddiy gap tuzilishidan, ro'yxatlar o'rniga \"1)\", \"2)\" kabi "
    "raqamlashdan foydalaning."
)

gemini_client = genai.Client(api_key=GEMINI_API_KEY) if (genai and GEMINI_API_KEY) else None

# context.user_data kalitlari
MODE_KEY = "mode"
QUIZ_TOPIC_KEY = "quiz_topic"
QUIZ_INDEX_KEY = "quiz_index"
QUIZ_SCORE_KEY = "quiz_score"

MODE_AI = "ai"
MODE_QUIZ = "quiz"


def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🤖 AI yordamchi (savol-javob)", callback_data="menu_ai")],
        [InlineKeyboardButton("📝 Test topshirish", callback_data="menu_quiz")],
        [InlineKeyboardButton("ℹ️ Yordam", callback_data="menu_help")],
    ]
    return InlineKeyboardMarkup(keyboard)


def topics_keyboard() -> InlineKeyboardMarkup:
    keyboard = []
    for key, topic in QUIZ_TOPICS.items():
        keyboard.append([InlineKeyboardButton(topic["title"], callback_data=f"topic_{key}")])
    keyboard.append([InlineKeyboardButton("⬅️ Orqaga", callback_data="menu_back")])
    return InlineKeyboardMarkup(keyboard)


def question_keyboard(options, q_index) -> InlineKeyboardMarkup:
    keyboard = []
    letters = ["A", "B", "C", "D", "E", "F"]
    for i, opt in enumerate(options):
        label = f"{letters[i]}. {opt}"
        keyboard.append([InlineKeyboardButton(label, callback_data=f"answer_{q_index}_{i}")])
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[MODE_KEY] = None
    text = (
        "👋 Assalomu alaykum!\n\n"
        "Men *Senior Informatika* yordamchi botiman. Men bilan:\n"
        "🤖 istalgan informatika mavzusida savol-javob qilishingiz,\n"
        "🖼 kod, masala yoki diagramma rasmini yuborib, tahlil oldirishingiz,\n"
        "📝 sinfingiz (5-11) bo'yicha test topshirishingiz mumkin.\n\n"
        "Quyidagi menyudan tanlang 👇"
    )
    await update.message.reply_text(
        text, reply_markup=main_menu_keyboard(), parse_mode=ParseMode.MARKDOWN
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "*Buyruqlar:*\n"
        "/start — bosh menyu\n"
        "/ai — AI yordamchi rejimiga o'tish\n"
        "/quiz — test rejimini boshlash\n"
        "/help — yordam\n\n"
        "AI rejimida shunchaki savolingizni yozing, men javob beraman.\n"
        "Istalgan vaqtda kod/masala/diagramma rasmini yuborsangiz, uni tahlil qilib xulosa beraman.\n"
        "Test rejimida sinfingizni tanlang va variantlardan birini bosing."
    )
    if update.message:
        await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
    elif update.callback_query:
        await update.callback_query.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)


async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[MODE_KEY] = MODE_AI
    await update.message.reply_text(
        "🤖 AI yordamchi rejimi yoqildi. Endi menga informatika bo'yicha "
        "istalgan savolingizni yozing.\n\nBosh menyuga qaytish uchun /start buyrug'ini bosing."
    )


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data[MODE_KEY] = None
    await update.message.reply_text(
        "📝 Test uchun sinfingizni tanlang:", reply_markup=topics_keyboard()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "menu_ai":
        context.user_data[MODE_KEY] = MODE_AI
        await query.edit_message_text(
            "🤖 AI yordamchi rejimi yoqildi. Endi menga informatika bo'yicha "
            "istalgan savolingizni yozing.\n\nBosh menyuga qaytish uchun /start buyrug'ini bosing."
        )
        return

    if data == "menu_quiz":
        await query.edit_message_text("📝 Test uchun sinfingizni tanlang:", reply_markup=topics_keyboard())
        return

    if data == "menu_help":
        await help_command(update, context)
        return

    if data == "menu_back":
        await query.edit_message_text(
            "Quyidagi menyudan tanlang 👇", reply_markup=main_menu_keyboard()
        )
        return

    if data.startswith("topic_"):
        topic_key = data[len("topic_"):]
        context.user_data[QUIZ_TOPIC_KEY] = topic_key
        context.user_data[QUIZ_INDEX_KEY] = 0
        context.user_data[QUIZ_SCORE_KEY] = 0
        await send_question(query, context)
        return

    if data.startswith("answer_"):
        _, q_index_str, opt_index_str = data.split("_")
        await handle_answer(query, context, int(q_index_str), int(opt_index_str))
        return


async def send_question(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    topic_key = context.user_data.get(QUIZ_TOPIC_KEY)
    q_index = context.user_data.get(QUIZ_INDEX_KEY, 0)
    topic = QUIZ_TOPICS[topic_key]
    questions = topic["questions"]

    if q_index >= len(questions):
        score = context.user_data.get(QUIZ_SCORE_KEY, 0)
        total = len(questions)
        percent = round(100 * score / total) if total else 0
        result_text = (
            f"✅ Test yakunlandi!\n\n"
            f"Sinf: {topic['title']}\n"
            f"Natija: {score}/{total} ({percent}%)\n\n"
        )
        if percent >= 80:
            result_text += "🏆 Ajoyib natija!"
        elif percent >= 50:
            result_text += "👍 Yaxshi, lekin yana mashq qiling."
        else:
            result_text += "📚 Ushbu sinf mavzularini qayta ko'rib chiqishingizni tavsiya qilaman."

        keyboard = [
            [InlineKeyboardButton("🔁 Boshqa sinf", callback_data="menu_quiz")],
            [InlineKeyboardButton("⬅️ Bosh menyu", callback_data="menu_back")],
        ]
        await query.edit_message_text(result_text, reply_markup=InlineKeyboardMarkup(keyboard))
        return

    question = questions[q_index]
    text = f"*{topic['title']}*\nSavol {q_index + 1}/{len(questions)}:\n\n{question['question']}"
    await query.edit_message_text(
        text,
        reply_markup=question_keyboard(question["options"], q_index),
        parse_mode=ParseMode.MARKDOWN,
    )


async def handle_answer(query, context: ContextTypes.DEFAULT_TYPE, q_index: int, opt_index: int) -> None:
    topic_key = context.user_data.get(QUIZ_TOPIC_KEY)
    topic = QUIZ_TOPICS[topic_key]
    questions = topic["questions"]
    question = questions[q_index]
    correct = question["correct"]

    is_correct = opt_index == correct
    if is_correct:
        context.user_data[QUIZ_SCORE_KEY] = context.user_data.get(QUIZ_SCORE_KEY, 0) + 1
        feedback = "✅ To'g'ri!"
    else:
        letters = ["A", "B", "C", "D", "E", "F"]
        feedback = f"❌ Noto'g'ri. To'g'ri javob: {letters[correct]}. {question['options'][correct]}"

    feedback += f"\n\n💡 {question['explanation']}"

    keyboard = [[InlineKeyboardButton("➡️ Keyingi savol", callback_data="next_question")]]
    await query.edit_message_text(feedback, reply_markup=InlineKeyboardMarkup(keyboard))

    context.user_data[QUIZ_INDEX_KEY] = q_index + 1


async def next_question_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await send_question(query, context)


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mode = context.user_data.get(MODE_KEY)
    user_text = update.message.text

    if mode != MODE_AI:
        await update.message.reply_text(
            "Iltimos, avval rejimni tanlang 👇", reply_markup=main_menu_keyboard()
        )
        return

    if not gemini_client:
        await update.message.reply_text(
            "⚠️ AI xizmati sozlanmagan. Iltimos, GEMINI_API_KEY muhit o'zgaruvchisini "
            "sozlang (README.md ga qarang)."
        )
        return

    await update.message.chat.send_action(action="typing")

    try:
        response = gemini_client.models.generate_content(
            model=AI_MODEL,
            contents=user_text,
            config=genai_types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                max_output_tokens=MAX_OUTPUT_TOKENS,
            ),
        )
        answer_text = (response.text or "").strip()
        if not answer_text:
            answer_text = "Kechirasiz, javob shakllantirib bo'lmadi. Qaytadan urinib ko'ring."
    except Exception as exc:  # noqa: BLE001
        logger.exception("Gemini API xatosi: %s", exc)
        answer_text = "quiz_data.py"

    await update.message.reply_text(answer_text)


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Foydalanuvchi yuborgan rasmni Gemini orqali tahlil qilib, xulosa qaytaradi."""
    if not gemini_client:
        await update.message.reply_text(
            "⚠️ AI xizmati sozlanmagan. Iltimos, GEMINI_API_KEY muhit o'zgaruvchisini "
            "sozlang (README.md ga qarang)."
        )
        return

    await update.message.chat.send_action(action="typing")

    caption = (update.message.caption or "").strip()
    prompt = caption if caption else (
        "Ushbu rasmni diqqat bilan tahlil qiling. Agar rasmda kod, algoritm, "
        "blok-sxema, jadval yoki informatika fani bo'yicha savol/masala bo'lsa, "
        "uni tushuntirib bering va aniq xulosa yoki yechim taqdim eting."
    )

    try:
        photo_file = await update.message.photo[-1].get_file()
        photo_bytes = bytes(await photo_file.download_as_bytearray())
        image_part = genai_types.Part.from_bytes(data=photo_bytes, mime_type="image/jpeg")

        response = gemini_client.models.generate_content(
            model=AI_MODEL,
            contents=[image_part, prompt],
            config=genai_types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                max_output_tokens=MAX_OUTPUT_TOKENS,
            ),
        )
        answer_text = (response.text or "").strip()
        if not answer_text:
            answer_text = "Kechirasiz, rasmni tahlil qilib bo'lmadi. Qaytadan urinib ko'ring."
    except Exception as exc:  # noqa: BLE001
        logger.exception("Gemini API (rasm tahlili) xatosi: %s", exc)
        answer_text = "⚠️ Rasmni tahlil qilishda xatolik yuz berdi. Birozdan so'ng qaytadan urinib ko'ring."

    await update.message.reply_text(answer_text)


async def setup_commands(application: Application) -> None:
    """Telegram xabar yozish maydonining chap tomonidagi Menu tugmasi
    ostida chiqadigan buyruqlar ro'yxatini o'rnatadi."""
    await application.bot.set_my_commands(
        [
            BotCommand("start", "Bosh menyu"),
            BotCommand("ai", "AI yordamchi rejimi"),
            BotCommand("quiz", "Test topshirish"),
            BotCommand("help", "Yordam"),
        ]
    )


def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN muhit o'zgaruvchisi topilmadi. README.md ga qarang."
        )

    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .read_timeout(30)
        .connect_timeout(30)
        .post_init(setup_commands)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ai", ai_command))
    application.add_handler(CommandHandler("quiz", quiz_command))

    application.add_handler(CallbackQueryHandler(next_question_handler, pattern="^next_question$"))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    logger.info("Bot ishga tushmoqda...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
