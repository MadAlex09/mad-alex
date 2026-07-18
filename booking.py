from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from keyboards import (
    hall_inline,
    common_pc_keyboard,
    vip_keyboard,
    time_keyboard,
    date_keyboard,
    start_time_keyboard,
    confirm_keyboard,
    vip_time_keyboard,
    vip_confirm_keyboard
)

from database import add_booking, check_booking
from config import ADMIN_ID


router = Router()

print("booking.py загружен")


# ======================
# Начало брони
# ======================

@router.message(F.text == "🎮 Забронировать ПК")
async def booking(message: Message):

    await message.answer(
        "🎮 Выберите зал:",
        reply_markup=hall_inline
    )


# ======================
# Выбор зала
# ======================

@router.callback_query(F.data == "hall_common")
async def hall_common(callback: CallbackQuery):

    await callback.message.edit_text(
        "🖥️ Выберите компьютер:",
        reply_markup=common_pc_keyboard()
    )

    await callback.answer()



@router.callback_query(F.data == "hall_vip")
async def hall_vip(callback: CallbackQuery):

    await callback.message.edit_text(
        "👑 Выберите VIP компьютер:",
        reply_markup=vip_keyboard()
    )

    await callback.answer()



# ==================================================
# ОБЫЧНЫЕ ПК
# ==================================================

@router.callback_query(F.data.startswith("pc_"))
async def select_pc(callback: CallbackQuery):

    pc = callback.data.split("_")[1]

    await callback.message.edit_text(
        f"""🎮 GAME CLUB

🖥️ ПК-{pc}

Выберите длительность:""",
        reply_markup=time_keyboard(pc)
    )

    await callback.answer()



@router.callback_query(F.data.startswith("time_"))
async def select_time(callback: CallbackQuery):

    data = callback.data.split("_")

    pc = data[1]
    hours = data[2]


    await callback.message.edit_text(
        f"""🖥️ ПК-{pc}

⏳ {hours} час(а)

📅 Выберите дату:""",
        reply_markup=date_keyboard(pc, hours)
    )

    await callback.answer()



@router.callback_query(F.data.startswith("date_"))
async def select_date(callback: CallbackQuery):

    data = callback.data.split("_")

    pc = data[1]
    hours = data[2]
    date = data[3]


    await callback.message.edit_text(
        f"""🖥️ ПК-{pc}

⏳ {hours} час(а)

📅 {date}

⏰ Выберите время:""",
        reply_markup=start_time_keyboard(
            pc,
            hours,
            date
        )
    )

    await callback.answer()



@router.callback_query(F.data.startswith("start_"))
async def select_start(callback: CallbackQuery):

    data = callback.data.split("_")

    pc = data[1]
    hours = data[2]
    date = data[3]
    start = data[4]


    await callback.message.edit_text(
        f"""✅ Проверьте бронь:

🖥️ ПК-{pc}

⏳ {hours} час(а)

📅 {date}

⏰ {start}

Подтвердить?""",
        reply_markup=confirm_keyboard(
            pc,
            hours,
            date,
            start
        )
    )

    await callback.answer()



@router.callback_query(F.data.startswith("confirm_"))
async def confirm(callback: CallbackQuery):

    data = callback.data.split("_")

    pc = data[1]
    hours = data[2]
    date = data[3]
    start = data[4]

    place = f"ПК-{pc}"


    if check_booking(place, date, start):

        await callback.message.edit_text(
            "❌ Этот компьютер уже занят на это время!"
        )

        await callback.answer()
        return



    add_booking(
        callback.from_user.id,
        callback.from_user.full_name,
        place,
        hours,
        date,
        start
    )


    await callback.message.edit_text(
        f"""🎉 Бронь создана!

🖥️ {place}

⏳ {hours} час(а)

📅 {date}

⏰ {start}

Спасибо за выбор GAME CLUB 🎮"""
    )


    await callback.bot.send_message(
        ADMIN_ID,
        f"""🔔 Новая бронь!

👤 Клиент:
{callback.from_user.full_name}

🖥️ {place}

⏳ {hours} час(а)

📅 {date}

⏰ {start}

🆔 ID:
{callback.from_user.id}

✅ Подтверждено"""
    )


    await callback.answer()



# ==================================================
# VIP
# ==================================================

@router.callback_query(F.data.startswith("vip_"))
async def select_vip(callback: CallbackQuery):

    vip = callback.data.split("_")[1]


    await callback.message.edit_text(
        f"""👑 VIP-{vip}

Выберите длительность:""",
        reply_markup=vip_time_keyboard(vip)
    )

    await callback.answer()



@router.callback_query(F.data.startswith("viptime_"))
async def vip_time(callback: CallbackQuery):

    data = callback.data.split("_")

    vip = data[1]
    hours = data[2]


    await callback.message.edit_text(
        f"""👑 VIP-{vip}

⏳ {hours} час(а)

📅 Выберите дату:""",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="📅 Сегодня",
                        callback_data=f"vipdate_{vip}_{hours}_today"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="📅 Завтра",
                        callback_data=f"vipdate_{vip}_{hours}_tomorrow"
                    )
                ]
            ]
        )
    )

    await callback.answer()



@router.callback_query(F.data.startswith("vipdate_"))
async def vip_date(callback: CallbackQuery):

    data = callback.data.split("_")

    vip = data[1]
    hours = data[2]
    date = data[3]


    await callback.message.edit_text(
        f"""👑 VIP-{vip}

⏳ {hours} час(а)

📅 {date}

⏰ Выберите время:""",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="14:00",
                        callback_data=f"vipstart_{vip}_{hours}_{date}_14:00"
                    ),
                    InlineKeyboardButton(
                        text="15:00",
                        callback_data=f"vipstart_{vip}_{hours}_{date}_15:00"
                    )
                ]
            ]
        )
    )

    await callback.answer()



@router.callback_query(F.data.startswith("vipstart_"))
async def vip_start(callback: CallbackQuery):

    data = callback.data.split("_")

    vip = data[1]
    hours = data[2]
    date = data[3]
    start = data[4]


    await callback.message.edit_text(
        f"""✅ Проверьте бронь:

👑 VIP-{vip}

⏳ {hours} час(а)

📅 {date}

⏰ {start}

Подтвердить?""",
        reply_markup=vip_confirm_keyboard(
            vip,
            hours,
            date,
            start
        )
    )

    await callback.answer()



@router.callback_query(F.data.startswith("vipconfirm_"))
async def vip_confirm(callback: CallbackQuery):

    data = callback.data.split("_")

    vip = data[1]
    hours = data[2]
    date = data[3]
    start = data[4]

    place = f"VIP-{vip}"


    if check_booking(place, date, start):

        await callback.message.edit_text(
            "❌ Этот VIP уже занят на это время!"
        )

        await callback.answer()
        return



    add_booking(
        callback.from_user.id,
        callback.from_user.full_name,
        place,
        hours,
        date,
        start
    )


    await callback.message.edit_text(
        f"""🎉 VIP бронь создана!

👑 {place}

⏳ {hours} час(а)

📅 {date}

⏰ {start}"""
    )


    await callback.bot.send_message(
        ADMIN_ID,
        f"""🔔 Новая VIP бронь!

👤 Клиент:
{callback.from_user.full_name}

👑 {place}

⏳ {hours} час(а)

📅 {date}

⏰ {start}

🆔 ID:
{callback.from_user.id}

✅ Подтверждено"""
    )


    await callback.answer()