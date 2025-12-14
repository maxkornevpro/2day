from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import FARM_TYPES, NFT_GIFTS

def get_main_menu():
    """Главное меню"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⭐ Мой профиль"), KeyboardButton(text="🌾 Мои фермы")],
            [KeyboardButton(text="🛒 Магазин ферм"), KeyboardButton(text="🎁 Магазин NFT")],
            [KeyboardButton(text="💰 Собрать доход"), KeyboardButton(text="🔗 Реферальная ссылка")],
            [KeyboardButton(text="🔨 Аукцион"), KeyboardButton(text="🎰 Казино")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_farm_shop_keyboard():
    """Клавиатура магазина ферм"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    for farm_id, farm_data in FARM_TYPES.items():
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=f"{farm_data['name']} - {farm_data['price']} ⭐",
                callback_data=f"buy_farm_{farm_id}"
            )
        ])
    
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")
    ])
    
    return keyboard

def get_nft_shop_keyboard():
    """Клавиатура магазина NFT"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    for nft_id, nft_data in NFT_GIFTS.items():
        boost_text = f"+{int((nft_data['boost'] - 1) * 100)}%"
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=f"{nft_data['name']} - {nft_data['price']} ⭐ ({boost_text})",
                callback_data=f"buy_nft_{nft_id}"
            )
        ])
    
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")
    ])
    
    return keyboard

def get_back_keyboard():
    """Клавиатура с кнопкой назад"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])
    return keyboard

def get_auction_keyboard(auction_id: int, current_bid: int):
    """Клавиатура для аукциона"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f"💰 Ставка: {current_bid + 100} ⭐",
                callback_data=f"bid_{auction_id}_{current_bid + 100}"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"💰 Ставка: {current_bid + 500} ⭐",
                callback_data=f"bid_{auction_id}_{current_bid + 500}"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"💰 Ставка: {current_bid + 1000} ⭐",
                callback_data=f"bid_{auction_id}_{current_bid + 1000}"
            )
        ],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])
    return keyboard

def get_admin_menu():
    """Админ меню"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 Справка (/ahelp)", callback_data="admin_help")],
        [InlineKeyboardButton(text="👤 Управление пользователями", callback_data="admin_users")],
        [InlineKeyboardButton(text="💰 Выдать звезды", callback_data="admin_give_stars")],
        [InlineKeyboardButton(text="🌾 Выдать ферму", callback_data="admin_give_farm")],
        [InlineKeyboardButton(text="🎁 Выдать NFT", callback_data="admin_give_nft")],
        [InlineKeyboardButton(text="🚫 Забанить", callback_data="admin_ban")],
        [InlineKeyboardButton(text="✅ Разбанить", callback_data="admin_unban")],
        [InlineKeyboardButton(text="📢 Рассылка", callback_data="admin_broadcast")],
        [InlineKeyboardButton(text="📊 Статистика", callback_data="admin_stats")]
    ])
    return keyboard

def get_casino_menu():
    """Меню казино"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Кости (x2)", callback_data="casino_dice")],
        [InlineKeyboardButton(text="🎰 Слоты (x3)", callback_data="casino_slots")],
        [InlineKeyboardButton(text="🎯 Рулетка (x5)", callback_data="casino_roulette")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])
    return keyboard

def get_farm_select_keyboard():
    """Клавиатура выбора фермы для админа"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for farm_id, farm_data in FARM_TYPES.items():
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=farm_data['name'],
                callback_data=f"admin_farm_{farm_id}"
            )
        ])
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text="🔙 Назад", callback_data="admin_back")
    ])
    return keyboard

def get_nft_select_keyboard():
    """Клавиатура выбора NFT для админа"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for nft_id, nft_data in NFT_GIFTS.items():
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=nft_data['name'],
                callback_data=f"admin_nft_{nft_id}"
            )
        ])
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(text="🔙 Назад", callback_data="admin_back")
    ])
    return keyboard
