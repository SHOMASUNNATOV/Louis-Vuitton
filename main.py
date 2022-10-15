import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from aiogram.types import KeyboardButton

token = "5458205001:AAFKL-oYf0I-zW495QOJCFfn4GkPZN9hx8U"
logging.basicConfig(level=logging.INFO)

btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn.add("ERKAKLAR", "AYOLLAR", "BOLALAR")

inline = types.InlineKeyboardButton('Xarid qilish ✅', callback_data='next')
inline2 = types.InlineKeyboardButton('Bekor qilish 🚫', callback_data='object remove')
forinline = types.InlineKeyboardMarkup()
forinline.add(inline, inline2)

order = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
w = KeyboardButton('Location', request_location=True)
w1 = KeyboardButton('Contact', request_contact=True)
w2 = KeyboardButton('MENU 📤')
order.add(w, w1, w2)

btnERKA = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btnERKA.add("ERKAKLAR-KO'YLAGI", "ERKAKLAR-SHIMI", "ERKAKLAR-OYOQ KIYIMI", "MENU 📤")

btnAYOL = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btnAYOL.add("AYOLLAR-KO'YLAGI", "AYOLLAR-SHIMI", "AYOLLAR-OYOQ KIYIMI", 'MENU 📤')

btnBOLA = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btnBOLA.add("BOLALAR-KO'YLAGI", "BOLALAR-SHIMI", "BOLALAR-OYOQ KIYIMI", 'MENU 📤')

bot = Bot(token)
con = Dispatcher(bot)


@con.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f'Hurmatli {message.chat.first_name} Louis Vuitton\n Botiga Xush kelibsiz!', reply_markup=btn)


@con.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(f' {message.chat.first_name}  murojaat uchun 👇\n  @shomasunnatov', reply_markup=btn)


@con.callback_query_handler(text=['next'])
async def asdff(call: types.CallbackQuery):
    await call.message.answer('Malumotingizni jonating', reply_markup=order)


@con.callback_query_handler(text=['object remove'])
async def stop(call: types.CallbackQuery):
    await call.message.answer('Buyurtma bekor qilindi!', reply_markup=btn)


@con.message_handler(text="ERKAKLAR")
async def erkaklar(message: types.Message):
    await message.reply("KO'YLAK", reply_markup=btnERKA)


@con.message_handler(text="ERKAKLAR-KO'YLAGI")
async def koylak(message: types.Message):
    rasm = open("pic/erkakkoylak1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK\nRazmer:XL,XXL,3XL\nNarxi:500000so'm",
                         reply_markup=forinline)
    rasm = open("pic/erkakkoylak2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK\nRazmer:L,XL,XXL,\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/erkakkoylak3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK\nRazmer:XL,XXL,3XL\nNarxi:550000so'm",
                         reply_markup=forinline)
    rasm = open("pic/erkakkoylak4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK\nRazmer:XL,XXL,3XL,4XL\nNarxi:600000so'm",
                         reply_markup=forinline)
    rasm = open("pic/erkakkoylak5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK\nRazmer:XL,XXL,3XL\nNarxi:350000so'm",
                         reply_markup=forinline)


@con.message_handler(text="ERKAKLAR")
async def erkaklar(message: types.Message):
    await message.reply("SHIM", reply_markup=btnERKA)


@con.message_handler(text="ERKAKLAR-SHIMI")
async def koylak(message: types.Message):
    rasm = open("pic/eshim1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM\nRazmer:34,36,38\nNarxi:500000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eshim2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM\nRazmer:36,38,40\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eshim3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM\nRazmer:34,36,40\nNarxi:550000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eshim4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM\nRazmer:32,34,36,38\nNarxi:600000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eshim5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM\nRazmer:32,34,36,38\nNarxi:600000so'm",
                         reply_markup=forinline)


@con.message_handler(text="ERKAKLAR")
async def erkaklar(message: types.Message):
    await message.reply("OYOQ KIYIM", reply_markup=btnERKA)


@con.message_handler(text="ERKAKLAR-OYOQ KIYIMI")
async def oyoqkiyim(message: types.Message):
    rasm = open("pic/eoyoq1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM\nRazmer:40,42,43\nNarxi:750000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eoyoq2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM\nRazmer:39,40,43\nNarxi:900000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eoyoq3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM\nRazmer:40,42,44\nNarxi:780000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eoyoq4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM\nRazmer:42,43,44,45\nNarxi:1200000so'm",
                         reply_markup=forinline)
    rasm = open("pic/eoyoq5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM\nRazmer:39,40,41L\nNarxi:650000so'm",
                         reply_markup=forinline)


@con.message_handler(text="AYOLLAR")
async def ayollar(message: types.Message):
    await message.reply("KO'YLAK", reply_markup=btnAYOL)


@con.message_handler(text="AYOLLAR-KO'YLAGI")
async def koylak(message: types.Message):
    rasm = open("pic/ayollarkoylak1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👗\nRazmer:XL,XXL,3XL\nNarxi:500000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ayollarkoylak2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👗\nRazmer:L,XL,XXL,\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ayollarkoylak3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👗\nRazmer:XL,XXL,3XL\nNarxi:550000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ayollarkoylak4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👗\nRazmer:XL,XXL,3XL,4XL\nNarxi:600000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ayollarkoylak5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👗\nRazmer:XL,XXL,3XL\nNarxi:350000so'm",
                         reply_markup=forinline)


@con.message_handler(text="AYOLLAR")
async def ayollar(message: types.Message):
    await message.reply("SHIM", reply_markup=btnAYOL)


@con.message_handler(text="AYOLLAR-SHIMI")
async def shim(message: types.Message):
    rasm = open("pic/ashim1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👖\nRazmer:34,36,38\nNarxi:500000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ashim2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👖\nRazmer:36,38,40\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ashim3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👖\nRazmer:36,38,40\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ashim4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👖\nRazmer:32,34,36,38\nNarxi:600000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ashim5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👖\nRazmer:34,36,40\nNarxi:350000so'm",
                         reply_markup=forinline)


@con.message_handler(text="AYOLLAR")
async def ayollar(message: types.Message):
    await message.reply("OYOQ KIYIM", reply_markup=btnAYOL)


@con.message_handler(text="AYOLLAR-OYOQ KIYIMI")
async def oyoqkiyim(message: types.Message):
    rasm = open("pic/aoyoq1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👠\nRazmer:40,42,43\nNarxi:750000so'm",
                         reply_markup=forinline)
    rasm = open("pic/aoyoq2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👠\nRazmer:39,40,43\nNarxi:900000so'm",
                         reply_markup=forinline)
    rasm = open("pic/aoyoq3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👠\nRazmer:40,42,44\nNarxi:780000so'm",
                         reply_markup=forinline)
    rasm = open("pic/aoyoq4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👠\nRazmer:42,43,44,45\nNarxi:1200000so'm",
                         reply_markup=forinline)
    rasm = open("pic/aoyoq5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👠\nRazmer:39,40,41L\nNarxi:650000so'm",
                         reply_markup=forinline)


@con.message_handler(text="BOLALAR")
async def bolalar(message: types.Message):
    await message.reply("KO'YLAK", reply_markup=btnBOLA)


@con.message_handler(text="BOLALAR-KO'YLAGI")
async def koylak(message: types.Message):
    rasm = open("pic/k1.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👕\nRazmer:XL,XXL,3XL\nNarxi:500000so'm",
                         reply_markup=forinline)
    rasm = open("pic/k2.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👕\nRazmer:L,XL,XXL,\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/k3.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👕\nRazmer:XL,XXL,3XL\nNarxi:550000so'm",
                         reply_markup=forinline)
    rasm = open("pic/k4.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👕\nRazmer:XL,XXL,3XL,4XL\nNarxi:600000so'm",
                         reply_markup=forinline)
    rasm = open("pic/k5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="KO'YLAK👕\nRazmer:XL,XXL,3XL\nNarxi:350000so'm",
                         reply_markup=forinline)


@con.message_handler(text="BOLALAR")
async def bolalar(message: types.Message):
    await message.reply("SHIM", reply_markup=btnBOLA)


@con.message_handler(text="BOLALAR-SHIMI")
async def shim(message: types.Message):
    rasm = open("pic/ksh5.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👕\nRazmer:34,36,38\nNarxi:500000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ksh123.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👕\nRazmer:36,38,40\nNarxi:250000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ksh144.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👕\nRazmer:34,36,40\nNarxi:550000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ksh203.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👕\nRazmer:32,34,36,38\nNarxi:600000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ksh243.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="SHIM👕\nRazmer:34,36,40\nNarxi:350000so'm",
                         reply_markup=forinline)


@con.message_handler(text="BOLALAR")
async def bolalar(message: types.Message):
    await message.reply("OYOQ KIYIM", reply_markup=btnBOLA)


@con.message_handler(text="BOLALAR-OYOQ KIYIMI")
async def oyoqkiyim(message: types.Message):
    rasm = open("pic/ko221.jpg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👟\nRazmer:40,42,43\nNarxi:750000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ko136.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👟\nRazmer:39,40,43\nNarxi:900000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ko244.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👟\nRazmer:40,42,44\nNarxi:780000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ko422.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👟\nRazmer:42,43,44,45\nNarxi:1200000so'm",
                         reply_markup=forinline)
    rasm = open("pic/ko441.jpeg", "rb")
    await bot.send_photo(message.chat.id, rasm, caption="OYOQ KIYIM👟\nRazmer:39,40,41L\nNarxi:650000so'm",
                         reply_markup=forinline)


@con.message_handler(text="ORQAGA ⬅")
async def black(message: types.Message):
    await message.reply("Ortga qaytdi", reply_markup=btnBOLA)


@con.message_handler(text="MENU 📤")
async def menu(message: types.Message):
    await message.reply(f'{message.chat.first_name} bosh sahifaga qaytdingiz', reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(con, skip_updates=True)
