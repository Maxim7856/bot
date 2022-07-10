from text import TextDefinitions 
from telebot import types

def get_keyboard():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	yes = types.KeyboardButton(TextDefinitions.YES)
	no = types.KeyboardButton(TextDefinitions.NO)
	stat = types.KeyboardButton(TextDefinitions.SHOW_STATISTICS)
	markup.add(yes, no, stat)
	return markup

def get_start_keyboard():
	"""
	* keyboard while user press /start command.
	"""
	start = types.KeyboardButton(TextDefinitions.BEGIN)
	stat = types.KeyboardButton(TextDefinitions.SHOW_STATISTICS)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	markup.add(start, stat)
	return markup

def get_multiple_coice_keyboard():
	a = types.KeyboardButton("a")
	b = types.KeyboardButton("b")
	c = types.KeyboardButton("c")
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	markup.add(a,b,c)
	return markup