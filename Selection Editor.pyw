import os
import tkinter as tk
from tkinter import messagebox

current_directory = os.path.abspath(os.getcwd()) 
file_path = os.path.join(current_directory, "numbers.reg")

def save_numbers():
    try:
        num1 = int(entry1.get().strip())
        num2 = int(entry2.get().strip())
        num3 = int(entry3.get().strip())

        if not (0 <= num1 <= 255 and 0 <= num2 <= 255 and 0 <= num3 <= 255):
            messagebox.showerror("Ошибка", "Введите числа в диапазоне от 0 до 255")
            return

        if not os.access(current_directory, os.W_OK):
            messagebox.showerror("Ошибка", f"Нет прав на запись в папку: {current_directory}")
            return

        with open(file_path, "w") as file:
            file.write(f"Windows Registry Editor Version 5.00\n[HKEY_CURRENT_USER\Control Panel\Colors]\n\"Hilight\"=\"{num1} {num2} {num3}\"\n\n[HKEY_CURRENT_USER\Control Panel\Colors]\n\"HotTrackingColor\"=\"{num1} {num2} {num3}\"")
        
        os.startfile(file_path);

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа")

root = tk.Tk()
root.title("🎨 РЕДАКТОР ЦВЕТА")
root.geometry("360x300")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Редактор цвета выделения Windows",
    font=("Arial", 14, "bold"),
    pady=10
)
title_label.grid(row=0, column=0, columnspan=2)

desc_label = tk.Label(
    root,
    text="Введите RGB-значения (0-255) для изменения цвета\nвыделения текста и файлов в Windows.",
    font=("Arial", 10),
    padx=10, pady=5
)
desc_label.grid(row=1, column=0, columnspan=2)

tk.Label(root, text="Красный (RED):", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(root, width=10, font=("Arial", 10))
entry1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Зелёный (GREEN):", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(root, width=10, font=("Arial", 10))
entry2.grid(row=3, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Синий (BLUE):", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry3 = tk.Entry(root, width=10, font=("Arial", 10))
entry3.grid(row=4, column=1, padx=10, pady=5, sticky="w")

save_button = tk.Button(
    root,
    text="Поменять цвет", 
    font=("Arial", 12, "bold"),
    padx=10, pady=5,
    command=save_numbers 
)
save_button.grid(row=5, column=0, columnspan=2, pady=15)

root.mainloop()
