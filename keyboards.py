from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from settings import COMMON_PC, VIP_PC


# ======================
# Главное меню
# ======================

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎮 Забронировать ПК")],
        [
            KeyboardButton(text="💰 Прайс-лист"),
            KeyboardButton(text="🛒 Магазин")
        ],
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="📍 Адрес")
        ],
        [
            KeyboardButton(text="📞 Поддержка")
        ]
    ],
    resize_keyboard=True
)


# ======================
# Регистрация
# ======================

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📝 Зарегистрироваться"
            )
        ]
    ],
    resize_keyboard=True
)


# ======================
# Залы
# ======================

hall_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🖥️ Общий зал",
                callback_data="hall_common"
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 VIP-зал",
                callback_data="hall_vip"
            )
        ]
    ]
)


# ======================
# Обычные ПК
# ======================

def common_pc_keyboard():

    keyboard = []
    row = []

    for i in range(1, COMMON_PC + 1):

        row.append(
            InlineKeyboardButton(
                text=f"🟢 ПК-{i}",
                callback_data=f"pc_{i}"
            )
        )

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append(
        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back_halls"
            )
        ]
    )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )


# ======================
# VIP компьютеры
# ======================

def vip_keyboard():

    keyboard = []
    row = []

    for i in range(1, VIP_PC + 1):

        row.append(
            InlineKeyboardButton(
                text=f"👑 VIP-{i}",
                callback_data=f"vip_{i}"
            )
        )

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append(
        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back_halls"
            )
        ]
    )

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )


# ======================
# Время обычного ПК
# ======================

def time_keyboard(pc):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🕐 1 час",
                    callback_data=f"time_{pc}_1"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🕑 2 часа",
                    callback_data=f"time_{pc}_2"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🕒 3 часа",
                    callback_data=f"time_{pc}_3"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="hall_common"
                )
            ]
        ]
    )


# ======================
# Дата
# ======================

def date_keyboard(pc, hours):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📅 Сегодня",
                    callback_data=f"date_{pc}_{hours}_today"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📅 Завтра",
                    callback_data=f"date_{pc}_{hours}_tomorrow"
                )
            ]
        ]
    )


# ======================
# Время начала
# ======================

def start_time_keyboard(pc, hours, date):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🕙 10:00",
                    callback_data=f"start_{pc}_{hours}_{date}_10:00"
                ),
                InlineKeyboardButton(
                    text="🕚 11:00",
                    callback_data=f"start_{pc}_{hours}_{date}_11:00"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🕛 12:00",
                    callback_data=f"start_{pc}_{hours}_{date}_12:00"
                ),
                InlineKeyboardButton(
                    text="🕐 13:00",
                    callback_data=f"start_{pc}_{hours}_{date}_13:00"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🕑 14:00",
                    callback_data=f"start_{pc}_{hours}_{date}_14:00"
                ),
                InlineKeyboardButton(
                    text="🕒 15:00",
                    callback_data=f"start_{pc}_{hours}_{date}_15:00"
                )
            ]
        ]
    )


# ======================
# Подтверждение обычного ПК
# ======================

def confirm_keyboard(pc, hours, date, start):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Подтвердить",
                    callback_data=f"confirm_{pc}_{hours}_{date}_{start}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ Отменить",
                    callback_data="cancel_booking"
                )
            ]
        ]
    )


# ======================
# VIP время
# ======================

def vip_time_keyboard(vip):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🕐 1 час",
                    callback_data=f"viptime_{vip}_1"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🕑 2 часа",
                    callback_data=f"viptime_{vip}_2"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🕒 3 часа",
                    callback_data=f"viptime_{vip}_3"
                )
            ]
        ]
    )


# ======================
# VIP подтверждение
# ======================

def vip_confirm_keyboard(vip, hours, date, start):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Подтвердить",
                    callback_data=f"vipconfirm_{vip}_{hours}_{date}_{start}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ Отменить",
                    callback_data="cancel_booking"
                )
            ]
        ]
    )