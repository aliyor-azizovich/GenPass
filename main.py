import tkinter as tk
from tkinter import messagebox
from front import RandPass

def pwGenerator(size=8):
    """Генерирует пароль и обновляет интерфейс"""
    # Генерируем новый пароль и информацию о его силе
    data = RandPass(size)  # Передаем размер пароля
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    
    # Обновляем текстовое поле с паролем
    PASSWORD.set(new_password)
    # Обновляем метку с силой пароля
    lbl_strength.configure(
        foreground="white", 
        background=pw_color, 
        text=pw_strength, 
        font=('sans serif', 10, 'bold'), 
        bd=10, 
        height=1, 
        width=10
    )
    
    # Копируем новый пароль в буфер обмена
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update_idletasks()

#
# Создаем основное окно приложения
gui = tk.Tk()
gui.title("Password Generator")

# Устанавливаем размеры и положение окна
width, height = 600, 262
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
gui.geometry(f"{width}x{height}+{x}+{y}")

# Определяем переменные для хранения пароля и размера
PASSWORD = tk.StringVar()
PW_SIZE = tk.IntVar(value=8)  # Устанавливаем значение по умолчанию для размера пароля


# Создаем фреймы для размещения виджетов
Top = tk.Frame(gui, width=width)
Top.pack(side=tk.TOP)
Form = tk.Frame(gui, width=width)
Form.pack(side=tk.TOP)
Bot = tk.Frame(gui, width=width)
Bot.pack(side=tk.BOTTOM)


# Заголовок в верхней части окна
lbl_title = tk.Label(
    Top, 
    width=width, 
    font=('sans serif', 12, 'bold'), 
    text="Select: Size >> Click: Generate Now", 
    bd=1, 
    relief=tk.SOLID
)
lbl_title.pack(fill=tk.X)

# Метка для отображения пароля
lbl_password = tk.Label(
    Form, 
    font=('sans serif', 18), 
    text="Password", 
    bd=10
)
lbl_password.grid(row=0, pady=10)

# Метка для отображения силы пароля
lbl_strength = tk.Label(
    Form, 
    font=('sans serif', 10, 'bold'), 
    foreground="white", 
    background="#6d0001", 
    text="Weak", 
    bd=10, 
    height=1, 
    width=10
)
lbl_strength.grid(row=0, column=3, pady=10, padx=10)

# Метка для отображения размера пароля
lbl_pw_size = tk.Label(
    Form, 
    font=('sans serif', 18), 
    text="Size", 
    bd=10
)
lbl_pw_size.grid(row=1, pady=10)

# Инструкции в нижней части окна
lbl_instructions = tk.Label(
    Bot, 
    width=width, 
    font=('sans serif', 12, 'bold'), 
    text="Result will be on clipboard.", 
    bd=1, 
    relief=tk.SOLID
)
lbl_instructions.pack(fill=tk.X)

# Поле для отображения сгенерированного пароля
password = tk.Entry(
    Form, 
    textvariable=PASSWORD, 
    font=(18), 
    width=24
)
password.grid(row=0, column=1, columnspan=2)

# Ползунок для выбора размера пароля
pw_size = tk.Scale(
    Form, 
    from_=8, 
    to=24, 
    length=230, 
    width=24, 
    sliderlength=14, 
    orient=tk.HORIZONTAL, 
    variable=PW_SIZE, 
    font=(18)
)
pw_size.grid(row=1, column=1, columnspan=2)


# Кнопка для генерации пароля
btn_generate = tk.Button(
    Form, 
    text="Generate Now", 
    width=20, 
    command=lambda: pwGenerator(PW_SIZE.get())
)
btn_generate.grid(row=2, column=1, columnspan=2)

# Запускаем основной цикл обработки событий
gui.mainloop()
