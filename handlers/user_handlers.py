from aiogram import Router, Bot
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery
from aiogram.methods.delete_message import DeleteMessage
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import main_menu_kb, biography_kb, credits_kb, years_of_working_kb, memory_kb, activity_kb
from services.services import book_message_id

router: Router = Router()


# ---------- Общие хэндлеры ---------
# Обработка /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=main_menu_kb)


# Обработка /help
@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=main_menu_kb)


# Обработка ВОЗВРАЩЕНИЯ В МЕНЮ
@router.message(Text(text=[LEXICON_RU["back_to_menu_btn"]]))
async def process_back_to_menu_button(message: Message):
    await message.answer(text=LEXICON_RU["back_to_menu"], reply_markup=main_menu_kb)


# ---------- Хэндлеры для деятельности ----------
@router.message(Text(text=[LEXICON_RU["activity_btn"]]))
async def process_activity_button(message: Message):
    await message.answer(text=LEXICON_RU["activity"], reply_markup=activity_kb)


# Обработка ИДЕЙ
@router.message(Text(text=[LEXICON_RU["ideas_btn"]]))
async def process_ideas_button(message: Message):
    await message.answer(text=LEXICON_RU["ideas"])


# Обработка РАБОТ
@router.message(Text(text=[LEXICON_RU["works_btn"]]))
async def process_works_button(message: Message):
    await message.answer(text=LEXICON_RU["works"])


# Обработка КНИГ
@router.message(Text(text=[LEXICON_RU["books_btn"]]))
async def process_books_button(message: Message):
    await message.answer(text=LEXICON_RU["books"])
    await message.answer_photo(photo="https://s1.livelib.ru/boocover/1001302134/o/e3d2/K._Ushinskij__Kotvorkot.jpeg")


# Обработка ЦИТАТ
@router.message(Text(text=[LEXICON_RU["quotes_btn"]]))
async def process_quotes_button(message: Message):
    await message.answer(text=LEXICON_RU["quotes"])


# ---------- Хэндлеры для памяти ----------
@router.message(Text(text=[LEXICON_RU["memory_btn"]]))
async def process_memory_button(message: Message):
    await message.answer(text=LEXICON_RU["memory"], reply_markup=memory_kb)


# Обработка УЧЕБНЫХ ЗАВЕДЕНИЙ
@router.message(Text(text=[LEXICON_RU["instituts_btn"]]))
async def process_institutes_button(message: Message):
    await message.answer(text=LEXICON_RU["institutes"])
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/ru/thumb/c/cf/Yaroslavl_State_Pedagogical_University_named_after_K.D._Ushinsky%2C_1_corpus.jpg/1280px-Yaroslavl_State_Pedagogical_University_named_after_K.D._Ushinsky%2C_1_corpus.jpg")


# Обработка УЛИЦ
@router.message(Text(text=[LEXICON_RU["streets_btn"]]))
async def process_streets_button(message: Message):
    await message.answer(text=LEXICON_RU["streets"])


# Обработка ПАМЯТНИКОВ
@router.message(Text(text=[LEXICON_RU["monuments_btn"]]))
async def process_monuments_button(message: Message):
    await message.answer(text=LEXICON_RU["monuments"])
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/f/f1/%D0%A0%D0%93%D0%9F%D0%A3_%D0%B8%D0%BC._%D0%90.%D0%98._%D0%93%D0%B5%D1%80%D1%86%D0%B5%D0%BD%D0%B0_-_panoramio.jpg")


# ---------- Хэндлеры для биографии ----------
# Обработка БИОГРАФИИ
@router.message(Text(text=[LEXICON_RU["biography_btn"]]))
async def process_biography_button(message: Message):
    await message.answer(text=LEXICON_RU["biography"], reply_markup=biography_kb)


# Обработка ДЕТСТВА И ОБРАЗОВАНИЯ
@router.message(Text(text=[LEXICON_RU["childhood_btn"]]))
async def process_childhood_button(message: Message):
    await message.answer(text=LEXICON_RU["childhood"])
    await message.answer_photo(photo="https://wiki.fenix.help/common/upload/ckeditor/2020/09/29/d41d8c--1601379872.jpeg")


# ----- Обработка ЛЕТ РАБОТЫ -----
@router.message(Text(text=[LEXICON_RU["years_of_working_btn"]]))
async def process_years_of_working_button(message: Message):
    global current_page, book_message_id
    current_page = 0
    if book_message_id:
        await DeleteMessage(chat_id=message.from_user.id, message_id=book_message_id)
        await DeleteMessage(chat_id=message.from_user.id, message_id=book_message_id - 1)
    msg = await message.answer(text=LEXICON_RU["years_of_working"][0], reply_markup=years_of_working_kb)
    book_message_id = msg.message_id


# Навигация по годам работы
# Переход на первую страницу
@router.callback_query(Text(text=["years_of_working_first_page"]))
async def process_first_page_of_working_button_press(callback: CallbackQuery):
    global current_page
    if current_page != 0:
        await callback.message.edit_text(text=LEXICON_RU["years_of_working"][0], reply_markup=callback.message.reply_markup)
        current_page = 0
        await callback.answer()
    else:
        await callback.answer(text="Вы итак на первой странице")


# Переход на предыдущую страницу
@router.callback_query(Text(text=["years_of_working_previous_page"]))
async def process_previous_page_of_working_button_press(callback: CallbackQuery):
    global current_page
    if current_page > 0:
        await callback.message.edit_text(text=LEXICON_RU["years_of_working"][current_page - 1], reply_markup=callback.message.reply_markup)
        current_page -= 1
        await callback.answer()
    else:
        await callback.answer(text="Вы на первой странице")


# Переход на следующую страницу
@router.callback_query(Text(text=["years_of_working_next_page"]))
async def process_next_page_button_pressed(callback: CallbackQuery):
    global current_page
    if current_page < 3:
        await callback.message.edit_text(text=LEXICON_RU["years_of_working"][current_page + 1], reply_markup=callback.message.reply_markup)
        current_page += 1
        await callback.answer()
    else:
        await callback.answer(text="Вы на последней странице странице")


# Переход на последнюю страницу
@router.callback_query(Text(text=["years_of_working_last_page"]))
async def process_last_page_button_press(callback: CallbackQuery):
    global current_page
    if current_page != 3:
        await callback.message.edit_text(text=LEXICON_RU["years_of_working"][-1], reply_markup=callback.message.reply_markup)
        current_page = 3
        await callback.answer()
    else:
        await callback.answer(text="Вы итак на последней странице странице")


# Обработка ПУТЕШЕСТВИЯ
@router.message(Text(text=[LEXICON_RU["traveling_btn"]]))
async def process_traveling_button(message: Message):
    await message.answer(text=LEXICON_RU["traveling"])


# ---------- Хендлеры для ИНФО ----------
# Обработка ИНФО о боте
@router.message(Text(text=[LEXICON_RU["credits_btn"]]))
async def process_credits_button(message: Message):
    await message.answer(text=LEXICON_RU["credits"], reply_markup=credits_kb)


# Обработка АВТОРОВ
@router.message(Text(text=[LEXICON_RU["authors_btn"]]))
async def process_authors_btn(message: Message):
    await message.answer(text=LEXICON_RU["authors"])


# Обработка ИСТОЧНИКОВ ИНФОРМАЦИИ
@router.message(Text(text=[LEXICON_RU["sources_btn"]]))
async def process_authors_btn(message: Message):
    await message.answer(text=LEXICON_RU["sources"], disable_webpage_preview=True)