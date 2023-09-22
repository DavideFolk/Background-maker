import customtkinter as ctk
from svg_turtle import SvgTurtle
import random


# ############################## svg turtle per creare sfondo
list_color_hex = ['#caa46e', '#954b32', '#dec988', '#355d7b', '#aa9a29', '#8a1f14', '#86a3b8', '#c55c49', '#2f7956',
                  '#492b23', '#91b295', '#0e6246', '#e8b0a5', '#a08e9e', '#362d32', '#654b4d', '#b7cdab', '#243c4a',
                  '#135659', '#529481', '#931113', '#1b4466', '#0c4640', '#6b7f99', '#b0c0d0', '#a86366']


def create_background():
    resolution = ''
    if option_menu.get() == '1920x1080':
        t = SvgTurtle(1920, 1080)
    elif option_menu.get() == '3440x1440':
        t = SvgTurtle(3340, 1440)

    form = form_button.get()

    bg_color = switch.get()
    t.screen.bgcolor(bg_color)
    t.up()

    if form == 'Punti':
        draw_dot(t)
    elif form == 'Triangoli':
        draw_triangle(t)
    elif form == 'Linee':
        draw_line(t)


def draw_dot(t):
    coordinate_x = -225
    coordinate_y = -225
    t.clear()
    for i in range(10):
        t.goto(coordinate_x, coordinate_y)
        for _ in range(10):
            t.dot(20, random.choice(list_color_hex))
            t.forward(50)
        coordinate_y += 50
    print('Wallpaper created!')
    t.save_as('wallpaper.svg')


def draw_triangle(t):
    coordinate_x = -225
    coordinate_y = -225
    t.clear()
    t.shape('triangle')
    for i in range(10):
        t.goto(coordinate_x, coordinate_y)
        for _ in range(10):
            t.color(random.choice(list_color_hex))
            t.stamp()
            t.forward(50)
        coordinate_y += 50
    print('Wallpaper created!')
    t.save_as('wallpaper.svg')


def draw_line(t):
    coordinate_x = -225
    coordinate_y = -225
    t.clear()
    t.width(6)
    for i in range(10):
        t.goto(coordinate_x, coordinate_y)
        t.down()
        t.color(random.choice(list_color_hex))
        t.forward(500)
        t.up()
        coordinate_y += 50
    print('Wallpaper created!')
    t.save_as('wallpaper.svg')


# ############################## customTkinter per l'interfaccia
app = ctk.CTk()
app.geometry("500x300")
app.title('Background maker')

app.grid_columnconfigure((0, 1), weight=1)

# label
label = ctk.CTkLabel(app, text='Crea il tuo sfondo', font=('arial', 24))
label.grid(row=0, column=0, padx=20, pady=(5, 10), columnspan=3)

# frame
frame = ctk.CTkFrame(master=app, width=450, height=400)
frame.grid(row=1, column=0, padx=20, pady=(5, 10), columnspan=3)
frame.grid_columnconfigure((0, 1, 2), weight=1)

# menu
option_menu = ctk.CTkOptionMenu(frame, values=["1920x1080", "3440x1440"])
option_menu.grid(row=0, column=0, padx=20, pady=20)

# switch
switch = ctk.CTkSwitch(frame, text="Sfondo nero",
                       onvalue="black",
                       offvalue="white")
switch.grid(row=0, column=1, padx=20, pady=20)

# scelta forma
form_button = ctk.CTkSegmentedButton(frame, values=["Punti", "Triangoli", "Linee"])
form_button.set("Punti")
form_button.grid(row=1, column=0, padx=(20), pady=(10), columnspan=2, sticky="ew")

# button crea
button = ctk.CTkButton(app, text='Crea Sfondo', command=create_background)
button.grid(row=3, column=0, padx=100, pady=(50, 0), sticky="ew", columnspan=3)

app.mainloop()
