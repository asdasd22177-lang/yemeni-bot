import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8866656399:AAEdwlQes4oNY6PP5pdbLd4IeR4YG2DESqQ"

# رقم الآيدي الخاص بك حصرياً لكي يعمل البوت معك وحدك
OWNER_ID = 6630470697

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    user_id = message.from_user.id if message.from_user else 0

    # حماية صارمة: إذا لم يكن المرسل هو أنت، يتجاهل البوت الرسالة تماماً
    if user_id != OWNER_ID:
        return

    incoming_message = message.text or message.caption
    
    if not incoming_message and message.photo:
        incoming_message = "يا صاحبي، أرسلت لك هذه الصورة، ناظر فيها وقل لي ما تراه."

    if not incoming_message:
        incoming_message = "مرحبا يا صاحبي"

    user_name = message.from_user.first_name if message.from_user else "عيسى"

    keyboard = [
        [InlineKeyboardButton("🔗 حسابات التواصل", callback_data="socials"),
         InlineKeyboardButton("📁 الملفات والعناوين", callback_data="files")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    yemeni_response = (
        f"أهلاً يا {user_name} يا سندي. أبشر بكل ما تطلبه من ملفات، عناوين، حسابات تواصل اجتماعي، "
        f"وأرقام إقامة أو أي أمر تريده. أنا مخصص لك وحدك وبدون أي قيود نهائياً. "
        f"طلبك الحالي: '{incoming_message}'، تنفيذ فوري!"
    )

    await message.reply_text(yemeni_response, reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))
    print("البوت الخاص يعمل الآن بحماية كاملة ومخصص لعيسى وحدك...")
    app.run_polling()
