
class TextDefinitions:
	SHOW_STATISTICS = "Посмотреть статистику"
	YES = "да"
	NO = "нет"
	BEGIN = "начать"



def get_start_text(first_name, player):
	result = f"Привет, {first_name}.\n\
Это игра в которой есть выбор да или нет.\
Это решит судьбу людей которые будут приходить к тебе! (нажми начать чтобы продолжить).\
Ваша начальная статистика:\n\
жители:{player.resident}.\n\
радость:{player.happiness}.\n\
монеты:{player.money}.\n"
	return result


class Questions:
	question1 = "Крестьянин: Добрый день,Ваше виличество!\nМожно ли мне собрать пшеницу с вашего поля?"