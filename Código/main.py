from tkinter import *
from tkinter import colorchooser
from PIL import ImageGrab
from threading import Thread, Semaphore
import time

class Paint:
    def __init__(self):
        # Inicializando a janela principal
        self.window = Tk()
        self.window.title("Paint")
        self.window.minsize(width=970, height=600)
        self.window.resizable(0,0)

        # Definindo os tipos de pincel
        self.oval_brush = True
        self.line_brush = False
        self.line_eraser = False

        # Carregando as imagens dos ícones
        self.img_line = PhotoImage(file="icons/line.png")
        self.img_oval = PhotoImage(file="icons/oval.png")
        self.img_eraser = PhotoImage(file="icons/eraser.png")
        self.img_save = PhotoImage(file="icons/save.png")
        self.img_square = PhotoImage(file="icons/square.png")
        self.img_new = PhotoImage(file="icons/new.png")

        # Definindo as cores disponíveis
        self.colors = ['black', 'grey', 'white','red', 'pink', 'green', 'blue', 'purple', 'orange', 'yellow']

        # Definindo a cor inicial do pincel
        self.pick_colors = 'black'

        # Criando o menu
        self.menu = Frame(self.window, bg="#3b3b3b", height=45)
        self.menu.pack(fill="x")

        # Adicionando os elementos ao menu
        self.text_color = Label(self.menu, text=" Colors: ", fg="white", bg="#3b3b3b")
        self.text_color.pack(side="left")

        # Criando um botão para cada cor disponível
        for i in self.colors:
            Button(self.menu, bg=i, width=3, height=1, command=lambda col=i: self.select_colors(col)).pack(side='left')

        # Adicionando mais elementos ao menu
        self.label_color_choose = Label(self.menu, text='  Color Choose:  ', fg='white', bg='#3b3b3b')
        self.label_color_choose.pack(side='left')

        # Criando o botão para escolher a cor
        self.color_choose = Button(self.menu, image=self.img_square, bd=0, command=self.selected_color)
        self.color_choose.pack(side='left')

        # Adicionando o seletor de tamanho do pincel
        Label(self.menu, text=" Size: ", fg="white", bg="#3b3b3b").pack(side='left')
        self.pen_size = Spinbox(self.menu, from_=1, to=50)
        self.pen_size.pack(side='left')

        # Adicionando os botões para escolher o tipo de pincel
        Label(self.menu, text=" Brushs: ", fg="white", bg="#3b3b3b").pack(side='left')
        Button(self.menu, image=self.img_line, bd=0, command=self.brush_line).pack(side='left')
        Button(self.menu, image=self.img_oval, bd=0, command=self.brush_oval).pack(side='left')
        Button(self.menu, image=self.img_eraser, bd=0, command=self.brush_eraser).pack(side='left')

        # Adicionando os botões de opções
        Label(self.menu, text=" Options: ", fg="white", bg="#3b3b3b").pack(side='left')
        Button(self.menu, image=self.img_save, bd=0, command=self.save).pack(side='left')
        Button(self.menu, image=self.img_new, bd=0, command=self.clean).pack(side='left')

        # Criando a área de desenho
        self.area_draw = Canvas(self.window, height=620, bg='gainsboro')
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)

        # Inicializando os semáforos
        self.draw_semaphore = Semaphore(0)  # Controla o acesso à área de desenho
        self.save_semaphore = Semaphore(0)  # Controla o acesso à função save_image

        # Iniciando a janela principal
        self.window.mainloop()

    # Função para desenhar na tela
    def draw(self, event):
        # Sinaliza que há um desenho pendente
        self.draw_semaphore.release()
        Thread(target=self.threaded_draw, args=(event,)).start()

    def threaded_draw(self, event):
        # Espera até que seja seguro desenhar
        self.draw_semaphore.acquire()
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x), (event.y)

        # Desenhando de acordo com o tipo de pincel selecionado
        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors, outline=self.pick_colors, width=self.pen_size.get())
        elif self.line_brush:
            self.area_draw.create_line(x1 - 10, y1 - 10, x2, y2, fill=self.pick_colors, width=self.pen_size.get())
        else:
            self.area_draw.create_oval(x1, y1, x2, y2, fill="gainsboro", outline='gainsboro', width=self.pen_size.get())
        time.sleep(0.01)  # Pequena pausa para simular trabalho intensivo

    # Função para selecionar a cor do pincel
    def select_colors(self, col):
        self.pick_colors = col

    # Funções para selecionar o tipo de pincel
    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.line_eraser = False

    def brush_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.line_eraser = False

    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.line_eraser = True

    # Função para limpar a tela
    def clean(self):
        self.area_draw.delete('all')

    # Função modificada para salvar a imagem
    def save(self):
        # Sinaliza que há um salvamento pendente
        self.save_semaphore.release()
        Thread(target=self.threaded_save).start()

    def threaded_save(self):
        # Espera até que seja seguro salvar
        self.save_semaphore.acquire()
        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.menu.winfo_height()
        x1 = x + self.area_draw.winfo_width()
        y1 = y + self.area_draw.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("image.png")
        time.sleep(0.01)  # Pequena pausa para simular trabalho intensivo

    # Função para selecionar a cor através de um seletor de cores
    def selected_color(self):
        color = colorchooser.askcolor()
        self.pick_colors = color[1]

# Iniciando a aplicação
Paint()