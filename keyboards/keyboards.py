from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# ---------- Главное меню ----------
activity_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["activity_btn"])
memory_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["memory_btn"])
biography_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["biography_btn"])
credits_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["credits_btn"])
back_to_menu_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["back_to_menu_btn"])

main_menu_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
main_menu_kb_builder.row(activity_btn, memory_btn, biography_btn, credits_btn, width=1)

main_menu_kb = main_menu_kb_builder.as_markup(resize_keyboard=True)


# ---------- Деятельность ----------
ideas_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["ideas_btn"])
works_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["works_btn"])
quotes_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["quotes_btn"])
books_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["books_btn"])

activity_kb_builer: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
activity_kb_builer.row(ideas_btn, works_btn, books_btn, quotes_btn, back_to_menu_btn, width=2)

activity_kb = activity_kb_builer.as_markup(resize_keyboard=True)


# ---------- Память ----------
instituts_btn: KeyboardButton =KeyboardButton(text=LEXICON_RU["instituts_btn"])
streets_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["streets_btn"])
monuments_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["monuments_btn"])

memory_kb_builder: ReplyKeyboardBuilder =ReplyKeyboardBuilder()
memory_kb_builder.row(instituts_btn, streets_btn, monuments_btn, back_to_menu_btn, width=1)

memory_kb = memory_kb_builder.as_markup(resize_keyboard=True)


# ---------- Биография ----------
childhood_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["childhood_btn"])
years_of_working_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["years_of_working_btn"])
traveling_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["traveling_btn"])

biography_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
biography_kb_builder.row(childhood_btn, years_of_working_btn, traveling_btn, back_to_menu_btn, width=1)

biography_kb = biography_kb_builder.as_markup(resize_keyboard=True)

# Годы работы
first_page_btn: InlineKeyboardButton = InlineKeyboardButton(text="⏮", callback_data="years_of_working_first_page")
previous_page_btn: InlineKeyboardButton = InlineKeyboardButton(text="◀", callback_data="years_of_working_previous_page")
next_page_btn: InlineKeyboardButton = InlineKeyboardButton(text="▶", callback_data="years_of_working_next_page")
last_page_btn: InlineKeyboardButton = InlineKeyboardButton(text="⏭", callback_data="years_of_working_last_page")

years_of_working_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
years_of_working_kb_builder.add(first_page_btn, previous_page_btn, next_page_btn, last_page_btn)

years_of_working_kb = years_of_working_kb_builder.as_markup()


# ---------- Общие сведения о боте ----------
authors_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["authors_btn"])
sources_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU["sources_btn"])

credits_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
credits_kb_builder.row(authors_btn, sources_btn, back_to_menu_btn, width=1)

credits_kb = credits_kb_builder.as_markup(resize_keyboard=True)