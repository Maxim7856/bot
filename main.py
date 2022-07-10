import telebot
from telebot import types
from text import TextDefinitions, get_start_text, Questions
from defenitions import Menu
from keyboards import get_keyboard, get_start_keyboard,get_multiple_coice_keyboard
import random

bot = telebot.TeleBot('5067705315:AAHXgRrwImWGp7SiHcxv9jV14hb6ILNCqwM')
players = {}


class Player:
	def __init__(self):
		self.money = random.randint(30,60)
		self.happiness = random.randint(30,70)
		self.resident = random.randint(15,20)

		# user menu
		self.menu = Menu.menu1

	class Flags:
		gatherPsheno = False

	class Torgovech:
		Vernylca = False

	class Torgoves_a:
		KameneDoma = False

	class Torgovech_b:
		dospehy = False

	class Torgovech_c:
		obevlenie = False

	def __str__(self):
		res = f"Ваша статистика:\n\
			Монеты={self.money}\n\
			Жители={self.resident}\n\
			Счастье={self.happiness}\n"
		return res

@bot.message_handler(commands=["start"])
def start(message):
	players[message.chat.id] = Player()
	mass = get_start_text(message.from_user.first_name, players[message.chat.id])
	bot.send_message(message.chat.id, mass, reply_markup=get_start_keyboard())


@bot.message_handler(regexp=rf"^{TextDefinitions.BEGIN}$")
def start_game(message):
	if message.chat.id not in players.keys():
		bot.send_message(message.chat.id, "Ошибка! напишите /start")
		return
	players[message.chat.id].menu=Menu.menu2
	bot.send_message(message.chat.id, Questions.question1, reply_markup=get_keyboard())


@bot.message_handler(regexp=rf"^{TextDefinitions.SHOW_STATISTICS}$")
def show_statistics(message):
	if message.chat.id not in players.keys():
		bot.send_message(message.chat.id, "Ошибка! напишите /start")
		return
	# shows statistics of current player.
	pl = players[message.chat.id]
	bot.send_message(message.chat.id,  str(pl))


@bot.message_handler(content_types=["text"])
def text(message):
	if message.chat.id not in players.keys():
		bot.send_message(message.chat.id, "Ошибка! напишите /start")
		return

	current_player_menu = players[message.chat.id].menu
	user_input = message.text
	markup = get_keyboard()

	if current_player_menu == Menu.menu2:
		if user_input == TextDefinitions.YES:
			bot.send_message(message.chat.id, "спасибо я вернусь поже!")
			players[message.chat.id].Flags.gatherPsheno = True
		elif user_input == TextDefinitions.NO:
			bot.send_message(message.chat.id, "что-ж жаль, а я хотел продать это пшено! -5 щястя")
			players[message.chat.id].happiness -= 5
		players[message.chat.id].menu = Menu.menu3
		bot.send_message(message.chat.id,
						 "К вам прешол шут\nшут:добрый день ваше величество! Хочете я вас розвеселю?", 
						 reply_markup=markup)
	elif current_player_menu == Menu.menu3:
		if user_input == TextDefinitions.YES:
			bot.send_message(message.chat.id, "Хорошо! *начинает розвлекать*. + 50 щястя", reply_markup=markup)
			players[message.chat.id].happiness += 50

			bot.send_message(message.chat.id, "Вам понравилось мое предстовление?", reply_markup=markup)
			players[message.chat.id].menu = Menu.menu4
		
		elif user_input == TextDefinitions.NO:
			bot.send_message(message.chat.id, "Ну и ладно! *Уходит*", reply_markup=markup)
			players[message.chat.id].menu = Menu.menu5
	elif current_player_menu == Menu.menu4:

		if user_input == TextDefinitions.YES:
			bot.send_message(message.chat.id, "спасибо я открою цырк!", reply_markup=markup)
		elif user_input == TextDefinitions.NO:
			bot.send_message(message.chat.id, "ЧТО!!!!??? НУ И ЛАДНО!", reply_markup=markup)
		

		if players[message.chat.id].Flags.gatherPsheno == True:
			bot.send_message(message.chat.id, "к вам вернулся крестианин\nвот деньги! + 50 монет")
			players[message.chat.id].money += 50

		players[message.chat.id].menu = Menu.menu5
		bot.send_message(message.chat.id, "к вам прешол торговец")
		bot.send_message(message.chat.id, "добрый день ваше величество! Хотите что-то купить?")
	elif current_player_menu == Menu.menu5: 
		if user_input == TextDefinitions.YES:
			bot.send_message(message.chat.id, "Что хотите купить?\na-каменный дома\nb-сильная армия\nс-обьявление\n", reply_markup=get_multiple_coice_keyboard())
			players[message.chat.id].Torgovech.Vernylca = True
			players[message.chat.id].menu = Menu.menu6
		elif user_input == TextDefinitions.NO: 
			bot.send_message(message.chat.id, "*уходит*")
			players[message.chat.id].menu = Menu.menu7

	elif current_player_menu == Menu.menu6: 
		if user_input == "a":

			price_a = random.randint(50,60)
			bot.send_message(message.chat.id, f"Отлично! Каменные дома построим завтра! монеты -{price_a}", reply_markup=markup)
			players[message.chat.id].Torgoves_a.KameneDoma = True
			players[message.chat.id].money -= price_a
		elif user_input == "b":
			bot.send_message(message.chat.id, "Отлично! одам доспехи завтра! монеты -30", reply_markup=markup)
			players[message.chat.id].Torgovech_b.dospehy = True
			players[message.chat.id].money -= 30
		elif user_input == "c":
			bot.send_message(message.chat.id, "Отлично! Разошлю почтовых голубей завтра! монеты -10", reply_markup=markup)
			players[message.chat.id].Torgovech_c.obevlenie = True
			players[message.chat.id].money -= 10

		players[message.chat.id].menu = Menu.menu8
		bot.send_message(message.chat.id, "автор:конец первого дня!\nспокойной ночи!", reply_markup=markup)
		bot.send_message(message.chat.id, f"автор:начало 2 дня! И вот деньги за жилье ваших граждан! \n +{players[message.chat.id].resident} монет", reply_markup=markup)
		players[message.chat.id].money += players[message.chat.id].resident

		players[message.chat.id].menu = Menu.menu9
	elif current_player_menu == Menu.menu9:
		bot.send_message(message.chat.id, "к вам прешол ищо один крестианин")
		bot.send_message(message.chat.id, "добрый день, ваше величество! У нас заканьчиваеца еда! Дайте пожалуйста 30 монет!")

		if user_input == TextDefinitions.YES:
			bot.send_message(message.chat.id, "спасибо!", reply_markup=markup)
			players[message.chat.id].menu = Menu.menu9
		elif user_input == TextDefinitions.NO:
			bot.send_message(message.chat.id, "ПОЧЕМУ?!", reply_markup=markup)
			players[message.chat.id].menu = Menu.menu9

		players[message.chat.id].menu = Menu.menu10
		if players[message.chat.id].Torgovech.Vernylca == True:
			if players[message.chat.id].Torgoves_a.KameneDoma == True:
				bot.send_message(message.chat.id, "а", reply_markup=markup)
			if players[message.chat.id].Torgovech_b.dospehy == True:
				bot.send_message(message.chat.id, "в", reply_markup=markup)
			if players[message.chat.id].Torgovech_c.obevlenie == True:
				bot.send_message(message.chat.id, "с", reply_markup=markup)


bot.polling(none_stop=True)