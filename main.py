from flask import Flask, url_for, request, render_template, redirect

from config import *

app = Flask(__name__)

""" Создание структуры продуктов """
# За детальной информацией перейдите в config.py

# Чтобы видеть созданную структуру: измените 0 на 1, на строчке ниже. Чтобы не видеть созданную структуру: измените 1 на 0, на строчке ниже
pr = ProductsStructure(logs = 1)

pr.create_product_structure()

""" Подготовка глобальных данных """

global_data = {
	"NAME_SHOP":NAME_SHOP,
}
return_data = {
		"PRODUCTS": pr.products,
	}

""" Подключение урл путей """
@app.route('/')
def index():

	return render_template(SETTING_TEMPLATE["index"], data=return_data, global_data=global_data)

@app.route('/<int:id>')
def product(id):
	product = pr.search_to_structure(id)

	return render_template(SETTING_TEMPLATE["product_info"], data=product, global_data=global_data)

@app.route('/order/<int:id>', methods=["GET", "POST"])
def order(id):

	notifications = []

	if request.method == 'POST':

		product = pr.search_to_structure(id)

		full_name = request.form.get("full_name", False)
		phone_number = request.form.get("phone_number", False)
		payment_method = request.form.get("payment_method", "Наличкой")

		with open('orders.txt', 'a', encoding='utf-8') as file:
		    file.write(
		    	f"\n[{GetTime()}] Заказ оформлен. Номер телефона: {full_name}, {phone_number}, {payment_method}. "
		    	f"Информация о заказе: Название {product['name']} | Стоимость: {product['price']}\n")

		notifications.append("Заказ успешно оформлен. Пожалуйста ожидайте.")

		return render_template(SETTING_TEMPLATE["index"], notifications=notifications, data=return_data, global_data=global_data)

		#  {request.form.get('phone_number', False)} | {request.form.get("full_name", False)} | {request.form.get("payment_method", False)}.

			
	product = pr.search_to_structure(id)

	return render_template(SETTING_TEMPLATE["product_info"], data=product, global_data=global_data, notifications=notifications)

if __name__ == "__main__":

	# Чтобы убрать режим дебага измените параметр True на False
	app.run(debug=True)