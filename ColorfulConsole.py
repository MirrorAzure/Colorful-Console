from tkinter import *
from tkinter import ttk
import mrcolor
import random
import os
import math


class MainWindow:
    bg_color = '#dbe9f4'
    text_color = '#131350'

    def __init__(self):
        self.root = Tk()
        self.configure_window()

        Label(self.root, text='Введите фразу:', bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, stick='w')
        self.phrase = Entry(self.root)
        self.phrase.grid(row=0, column=1)

        Label(self.root, text='Введите первый цвет:', bg=self.bg_color, fg=self.text_color).grid(row=1, column=0,
                                                                                                 stick='w')
        self.first_color = Entry(self.root)
        self.first_color.grid(row=1, column=1)

        Label(self.root, text='Введите второй цвет:', bg=self.bg_color, fg=self.text_color).grid(row=2, column=0,
                                                                                                 stick='w')
        self.second_color = Entry(self.root)
        self.second_color.grid(row=2, column=1)

        Button(self.root, text='Сделать красиво', command=self.phrase_fill, fg=self.text_color).grid(row=0, column=2,
                                                                                                     rowspan=3,
                                                                                                     stick='sn')

        Label(self.root, text='Задайте направление:', bg=self.bg_color, fg=self.text_color).grid(row=3, column=0,
                                                                                                 stick='w')
        directions = ["Диагональ направо", "Диагональ налево", "Сверху вниз", "Справа налево"]
        self.direction = ttk.Combobox(self.root, values=directions, state="readonly")
        self.direction.current(2)
        self.direction.grid(row=3, column=1)

    def configure_window(self):
        self.root.title("Colorful Console")
        self.root.geometry("400x160")
        self.root.configure(background=self.bg_color)

    def phrase_fill(self):
        if mrcolor.is_correct_color(self.first_color.get()):
            color_one = self.first_color.get()
        else:
            color_one = choose_random_color()

        if mrcolor.is_correct_color(self.second_color.get()):
            color_two = self.second_color.get()
        else:
            color_two = choose_random_color()

        word = self.phrase.get() + ' ' if self.phrase.get() else "MirrorAzure "
        length = len(word)
        current = 0

        color_list = mrcolor.gradient(color_one, color_two, 120)
        clear_console()
        for y in range(30):
            for x in range(120):
                if self.direction.get() == "Диагональ налево":
                    red_color, green_color, blue_color = mrcolor.hex_to_color(
                        color_list[y * 3 + (30 - math.floor(x / 4))])
                elif self.direction.get() == "Диагональ направо":
                    red_color, green_color, blue_color = mrcolor.hex_to_color(color_list[y * 3 + math.floor(x / 4)])
                elif self.direction.get() == "Сверху вниз":
                    red_color, green_color, blue_color = mrcolor.hex_to_color(color_list[y * 4])
                elif self.direction.get() == "Справа налево":
                    red_color, green_color, blue_color = mrcolor.hex_to_color(color_list[x])
                else:
                    red_color, green_color, blue_color = (255, 255, 255)
                if current >= length:
                    current = 0
                print(f'\033[38;2;{red_color};{green_color};{blue_color}m' + word[current], end='')
                current += 1
        print()


def clear_console():
    """
    Function clears the console
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # cls for Windows
        command = 'cls'
    os.system(command)


def choose_random_color():
    return random.randint(0x80, 0xFF) * 0x10000 + random.randint(0x80, 0xFF) * 0x100 + random.randint(0x80, 0xFF)


os.system('mode 120,31')
window = MainWindow()
window.root.mainloop()
