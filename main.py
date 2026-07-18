import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import TOKEN
from keyboards import main_menu, register_keyboard
from register import user_exists, add_user, delete_user
from booking import router as booking_router
from admin import router as admin_router
from database import create_db

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(booking_router)
dp.include_router(admin_router)
print("✅ Booking router подключен")


# Подключаем роутер сразу после создания Dispatcher


# ======================
# Регистрация
# ======================

class Register(StatesGroup):
    waiting_name = State()
    waiting_phone = State()


# ======================
# /start
# ======================

@dp.message(Command("start"))
async def start(message: Message):
    if user_exists(message.from_user.id):

        await message.answer(
            f"👋 С возвращением, {message.from_user.first_name}!",
            reply_markup=main_menu
        )

    else:

        await message.answer(
            "━━━━━━━━━━━━━━━━━━\n"
            "🎮 GAME CLUB\n\n"
            "Добро пожаловать!\n\n"
            "Для начала зарегистрируйтесь.",
            reply_markup=register_keyboard
        )


# ======================
# /reset
# ======================

@dp.message(Command("reset"))
async def reset_register(message: Message):
    delete_user(message.from_user.id)

    await message.answer(
        "🔄 Регистрация сброшена.\n\n"
        "Нажмите кнопку регистрации заново.",
        reply_markup=register_keyboard
    )


# ======================
# Регистрация
# ======================

@dp.message(F.text == "📝 Зарегистрироваться")
async def register(message: Message, state: FSMContext):
    await message.answer("👤 Введите ваше имя:")

    await state.set_state(Register.waiting_name)


@dp.message(Register.waiting_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(
        "📱 Введите номер телефона\n\n"
        "Например:\n"
        "+77771234567"
    )

    await state.set_state(Register.waiting_phone)


@dp.message(Register.waiting_phone)
async def get_phone(message: Message, state: FSMContext):
    phone = message.text

    data = await state.get_data()

    add_user(
        message.from_user.id,
        data["name"],
        phone
    )

    await message.answer(
        f"✅ Регистрация завершена!\n\n"
        f"Добро пожаловать, {data['name']}!",
        reply_markup=main_menu
    )

    await state.clear()


# ======================
# Прайс
# ======================

@dp.message(F.text == "💰 Прайс-лист")
async def price(message: Message):
    await message.answer(
        "💰 ПРАЙС\n\n"
        "🕐 1 час — 1000 тг\n"
        "🕑 2 часа — 1800 тг\n"
        "🕒 3 часа — 2500 тг"
    )


# ======================
# Магазин
# ======================

@dp.message(F.text == "🛒 Магазин")
async def shop(message: Message):
    await message.answer(
        "🛒 Магазин\n\n"
        "🥤 Gorilla\n"
        "🥤 Coca-Cola\n"
        "🌭 Хот-дог\n"
        "🍟 Lay's"
    )


# ======================
# Адрес
# ======================

@dp.message(F.text == "📍 Адрес")
async def address(message: Message):
    await message.answer(
        "📍 Восток 2, дом 5"
    )


# ======================
# Профиль
# ======================

@dp.message(F.text == "👤 Профиль")
async def profile(message: Message):
    await message.answer(
        f"👤 Ваш Telegram ID:\n{message.from_user.id}"
    )


# ======================
# Поддержка
# ======================

@dp.message(F.text == "📞 Поддержка")
async def support(message: Message):
    await message.answer(
        "📞 Администратор\n@ВашНик"
    )

