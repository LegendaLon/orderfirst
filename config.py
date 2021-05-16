from datetime import datetime as dt
from prettytable import PrettyTable

from colorama import Fore

NAME_SHOP = "FreeBMW"

SETTING_TEMPLATE = {
	"index":"index.html",
	"product_info":"product_info.html",
}

""" Время """
def GetTime():
	time = str(dt.now())[11:19]
	day = str(dt.now())[8:10]
	month = str(dt.now())[5:7]
	year = str(dt.now())[0:4]

	return f"{time} {day}/{month}/{year}"

""" Структура товаров """
class ProductsStructure():
	def __init__(self, logs):
		self.products = []
		self.last_id = 1

		# Красивая таблица структуры
		self.table = PrettyTable([f"{Fore.YELLOW}ID{Fore.RESET}", f"{Fore.YELLOW}NAME{Fore.RESET}", f"{Fore.YELLOW}SHORT_DESCRIPTION{Fore.RESET}", f"{Fore.YELLOW}PRICE{Fore.RESET}"])

		# Вывод итоговой структуры в консоль
		self.log_status = logs

	def logs(self):
		# Добавление товаров в таблицу, для красиового вывода
		for product in self.products:
			self.table.add_row([product['id'], product["name"], product["short_description"], product["price"]])

		print(self.table)

	def add_product(self, name=None, description=None, price=None):
		# Добавление товаров
		product = {
			"id":self.last_id,
			"name":name,
			"price":price,
			"description":description,
		}
		if len(description) >= 60: 
			product["short_description"] = description[:60] + "..."
		else:
			product["short_description"] = description

		self.last_id += 1

		self.products.append(product)

	def search_to_structure(self, id):
		# Поиск по структуре
		for product in self.products:
			if product['id'] == id:
				return product

	""" Ниже прописываем создание всех продуктов в сттруктуре """
	def create_product_structure(self):
		# Пример
		# self.add_product(name="Название продукта", description="Описание продукта", price="Стоимость продукта")
		# Можно просто копировать и просто изменять параметры

		self.add_product(name="BMW X5 2009", description="3 л • Дизель, Черный Авто приехало из Чехии официальной историей (сервисной книгой)", price="17200$")
		self.add_product(name="BMW 740 2017", description="Двигатель 3 л • Бензин, Типтроник Привод Передний, Черный металлик", price="39999$")
		self.add_product(name="BMW 760 XDrive Individual 2019", description="6.6 л • Бензин, Колір Чорний, стоит", price="118000$")
		self.add_product(name="BMW I3 GARANTIYA DO 2023 2019", description="Електро Цвет Белый", price="26300$")
		self.add_product(name="BMW 520 d Xdrive Sport line 2017", description="2 л • Дизель, Серый", price="41600$")
		self.add_product(name="BMW 328 M 2014", description="2 л • Бензин ,Коричневий", price="14700$")
		self.add_product(name="BMW S Series 1000XR 2020", description="1.0 л (165 к.с • 121.3 кВт) • Бензин, Коробка передач Механічна,Привід Ланцюговий привід", price="24323$")
		self.add_product(name="BMW F 800 F800r 2012 800", description="0.8 л  Бензин місто 4 • траса 5.5 • змішаний 5.5 ,Коробка передач Ручна / Механіка", price="2500$")
		self.add_product(name="BMW X5 2009", description="3 л • Дизель, Чорний", price="17200$")
		self.add_product(name="BMW M5 Competition 2020-2019", description="4.9 л • Бензин , Синій", price="149999$")
		self.add_product(name="BMW M5 1999", description="4.9 л • Бензин, Коробка передач Ручна / Механіка, Привод Задній , Цвет Синій", price="37500$")
		self.add_product(name="BMW M5 HAMANN 2005", description="М5 Е60 stage2 550кс Обвес, глушитель HAMANN оригинал После замены масел и фильтров После замены свечей", price="31000$")
		self.add_product(name="BMW 525 M5 2004", description="2.5 л  • Газ / Бензин, Комплектация Экстерьер Фары передние БЫ ксенон рестайловые Фонари задние рестайловые с ресницами Обвес в круг -М5 Крылья с жабрами М5", price="14000$")
		self.add_product(name="BMW M5 2020", description="Акустическая система Harman / Kardon, лазерная оптика, Distronic, отделка интерьера (крыша) - Карбон, камера заднего вида, доводчики дверей, проекция на лобовое стекло, отделка натуральной кожей", price="139900$")
		self.add_product(name="BMW X5 50i X5M 2019", description="4.4 бензин, полный привод, Выхлоп M Perfomance, фары BMW Laser, проекция на лобовое стекло, адаптивный круиз-контроль, система удержания в полосе движений, мониторинг мертвых зон, активные системы безопасности, 4-х зонный климат-контроль, подогревы всех сидений, память передних сидений", price="89000$")

		if self.log_status == 1:
			self.logs()