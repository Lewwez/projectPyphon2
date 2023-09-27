import tkinter as tk
import random
import time

# Функция для обновления цены доллара к рублю и отображения изменений
def update_price():
    global current_price
    global price_label
    global log_text

    # Генерируем случайное изменение цены (-1% до +1%)
    change_percent = random.uniform(-1, 1)
    change_amount = current_price * change_percent / 100
    current_price += change_amount

    # Определяем цвет текста и символ изменения
    if change_amount > 0:
        color = "green"
        change_symbol = "+"
    else:
        color = "red"
        change_symbol = ""

    # Формируем строку с изменением цены
    change_str = f"{change_symbol}{abs(change_amount):.2f}р ({change_percent:+.2f}%)"

    # Обновляем метку с текущей ценой
    price_label.config(text=f"1 USD = {current_price:.2f} RUB")

    # Добавляем изменение цены в лог
    log_text.insert(tk.END, change_str + "\n")
    log_text.see(tk.END)  # Прокручиваем лог вниз

    # Запускаем функцию обновления цены через 10 секунд
    root.after(10000, update_price)

# Создаем главное окно
root = tk.Tk()
root.title("Курс доллара к рублю")

# Изначальная цена доллара к рублю
current_price = 73.00

# Создаем метку для отображения цены
price_label = tk.Label(root, text=f"1 USD = {current_price:.2f} RUB", font=("Helvetica", 24))
price_label.pack()

# Создаем текстовое поле для отображения изменений
log_text = tk.Text(root, height=10, width=40)
log_text.pack()

# Запускаем функцию обновления цены
update_price()

# Запускаем главное окно
root.mainloop()