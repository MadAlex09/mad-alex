from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Все брони")
        ],
        [
            KeyboardButton(text="❌ Удалить бронь")
        ]
    ],
    resize_keyboard=True
)