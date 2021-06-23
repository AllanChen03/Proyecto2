from tkinter import *
import tkinter as tk
import os
import threading
import multiprocessing
import random
import time
from playsound import playsound


about ="""
-------------------------------------------------------
Instituto Tecnológico de Costa Rica
Taller a la programación
Semestre 1
Grupo 4
-------------------------------------------------------
Profesor: Luis Barboza Artavia
Estudiantes:
Marianna Méndez Solano
Li Hao Allan Chen Liang
Carné:
2021142221
2019049482
Fecha de entrega: 23 de Junio del 2021
Versión de Python: 3.9.2
Pais de elaboracion: Costa Rica
-------------------------------------------------------
Space Rush consiste en controlar una nave
alienigena y sobrevivir a los enemigos por 1
minuto. El jugador comienza con 3 vidas y perderá
1 vida si colisiona con el enemigo. Space Rush
se compone de 3 niveles:
Primer Nivel: Deberá sobrevivir contra 2 enemigos
Segundo Nivel: Deberá sobrevivir contra 4 enemigos
Tercer Nivel: Deberá sobrevivir contra 6 enemigos
Controles:
Up: La nave se mueve hacia arriba
Right: La nave se mueve hacia la derecha
Left: La nave se mueve hacia la izquierda
Down: La nave se mueve hacia abajo
-------------------------------------------------------
"""

#Funcion que crea las imagenes
def load_image(nombre):
    path = os.path.join('/Users/chain03/Documents/Cursos/Taller/Proyecto2',nombre)  #Path 
    image = PhotoImage(file = path)
    return image
#Clase Ventana Principal
class Ventana_Principal:
    def __init__(self,master):

        self.canvas = Canvas(master, width = 550, height = 700, highlightthickness = 0, bg = 'black')
        self.canvas.place(x=0,y=0)

        self.fondo = load_image('Fondo.png')
        self.label_fondo = Label(self.canvas,bg = 'black', image = self.fondo)
        self.label_fondo.place(x = 0, y = 0)

        self.logo = load_image('spacerushSW.png')
        self.label_logo = Label(self.canvas,bg = 'black', image = self.logo)

        self.label_logo.place(x = 15, y = 90)

        #Imagenes Estaticas para el fondo
        self.spaceship = load_image('player.png')
        self.label_spaceship = Label(self.canvas, bg='black', image=self.spaceship)
        self.label_spaceship.place(x=385, y=530)

        #Imagenes Estaticas para el fondo
        self.enemyVP = load_image('enemyVP.png')
        self.label_enemyVP = Label(self.canvas, bg='black', image=self.enemyVP)
        self.label_enemyVP.place(x=30, y=300)

        #Imagenes Estaticas para el fondo
        self.enemyVP1 = load_image('enemyVP1.png')
        self.label_enemyVP1 = Label(self.canvas, bg='black', image=self.enemyVP1)
        self.label_enemyVP1.place(x=120, y=370)

        #Imagenes Estaticas para el fondo
        self.enemyVP2 = load_image('enemyVP2.png')
        self.label_enemyVP2 = Label(self.canvas, bg='black', image=self.enemyVP2)
        self.label_enemyVP2.place(x=170, y=290)

        #Entry para el nombre del jugador
        self.name_entry = Entry(self.canvas)
        self.name_entry.place(x=260, y=195, width=150, height=25)

        #Label "Digite su nombre"
        self.label_name = Label(self.canvas, text = "Digite su nombre:", bg= 'black', fg = 'white', font = ("Century Gothic",11))
        self.label_name.place(x= 110, y = 195)
        
        #Selecciona el nivel 1 por default
        selection.set(1)
        self.best_score = Best_Score

        #Botones
        #Boton que comienza el juego
        self.button_play = Button(self.canvas, text="Play", bg="yellow", fg='black', font=("Century Gothic", 10),command=self.verificacion)
        self.button_play.place(x=230, y=530, width=80, height=30)
        #Botones de Radio para seleccionar el nivel
        #Nivel 1
        self.Radio_level1 = Radiobutton(self.canvas, text = "Level 1",bg = 'black', fg = 'white',  font = ("Century Gothic",10), variable=selection,value=1)
        self.Radio_level1.place(x=230, y = 330)
        #Nivel 2
        self.Radio_level2 = Radiobutton(self.canvas, text = "Level 2",bg = 'black', fg = 'white', font = ("Century Gothic",10), variable=selection,value=2)
        self.Radio_level2.place(x=230, y = 390)
        #Nivel 3
        self.Radio_level3 = Radiobutton(self.canvas, text = "Level 3",bg = 'black', fg = 'white',  font = ("Century Gothic",10), variable=selection,value=3)
        self.Radio_level3.place(x=230, y = 460)
        #Boton para abrir la pantalla del about
        self.button_about = Button(self.canvas, text = "About",bg='yellow',fg = 'black', command = self.about)
        self.button_about.place(x=20, y= 630, width= 50, height= 30)
        #Boton para cerrar la ventana principal
        self.button_exit = Button(self.canvas, text = "Exit", bg = "black", fg= 'white', command = self.exit_ventana)
        self.button_exit.place(x=450, y=630, width= 50, height= 30)
        #Boton para acceder a las mejores puntuaciones
        self.button_best_score = Button(self.canvas, text = "Score", bg = "black", fg= 'white', command = self.best_score)
        self.button_best_score.place(x=80, y = 630, width= 50, height= 30)
        #Reproduce la cancion del juego
        playsound('song1.wav', block = False)

    #Pantalla del about
    def about(self):

        self.about = Toplevel()
        self.about.title("Creditos")
        self.about.minsize(500,500)
        self.about.resizable(width = NO, height = NO)
        self.canvas_about = Canvas(self.about, width = 500, height = 500, highlightthickness = 0, bg = 'black')
        self.canvas_about.place(x=0,y=0)

        self.fondo = load_image('Fondo2.png')
        self.label_fondo = Label(self.canvas_about,bg = 'black', image = self.fondo)
        self.label_fondo.place(x = 0, y = 0)

        self.label_about = Label(self.about, text = about, font= ("Arial",13), bg = 'black', fg = 'white')
        self.label_about.place(x=90,y=0)

        self.button_about_exit = Button(self.about, text = "Exit", bg = 'black', command = self.exit_about)
        self.button_about_exit.place(x=450, y= 470)
    #Funcion que verifica que la entrada del nombre no este vacia
    def verificacion(self):
        self.label_error = Label(self.canvas, text = "Debe ingresar su nombre", font = ("Arial",14), bg = 'black', fg = 'white')
         #Get the name ot the text entry
        self.name = self.name_entry.get()

        self.rango = selection.get()
        #Verifica que la entrada del nombre no este vaci
        if self.name != "":
            self.new_game_screen = Game(self.name,self.rango)
            self.new_game_screen.iniciar_juego()
        else:
            return self.label_error.place(x=150, y=330)
    #Funcion que cierra la pantalla del about
    def exit_about(self):
        self.about.destroy()
    #Funcion que cierra la pantalla principal    
    def exit_ventana(self):
        window.destroy()
        
        
#Clase Juego        
class Game:
    def __init__(self,name,rango):
        self.game = Toplevel()
        
        self.game.minsize(550,700)
        self.game.resizable(width=NO,height=NO)
        
        self.canvas_game = Canvas(self.game, width = 550,height = 700,bg = 'black',highlightthickness = 0)
        self.canvas_game.place(x=0,y=0)

        self.fondo = load_image('Fondo.png')
        self.label_fondo = Label(self.canvas_game,bg = 'black', image = self.fondo)
        self.label_fondo.place(x = 0, y = 0)

        self.label_player = Label(self.game, text = "Player:",font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_player.place(x=5,y=5)
        self.label_name = Label(self.game, text = name ,font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_name.place(x=53, y = 5)
        
        self.rango = rango
        self.name = name

        self.lista_enemigos = []

        #crea el Thread que verifica si hay colisiones
        self.check_collision_thread = threading.Thread(target=self.check_collision)
        self.check_collision_thread.setDaemon(True)
        
        #define la Clase Player en la clase Game
        self.player = Player(self.canvas_game,self.game)

        #define la Clase Nave en la clase Game
        self.nave = Nave(self.canvas_game)
        
        #define la Clase Score en la clase Game
        self.score = Score(self.canvas_game,self.rango,self.name)
        

        #Boton para cerrar la pantalla de Juego
        self.button_exit = Button(self.game, text = "Exit",font = ("Arial",16),background = 'black', command = self.exit)
        self.button_exit.place(x=430, y= 5)
        #define la Clase Timer en la clase Game
        self.timer = Timer(self.canvas_game,self.game,self.rango,self.name)

    #Funcion para cerrar la pantalla del juego
    def exit(self):
        self.game.destroy()
    #Funcion que inicia el juego
    def iniciar_juego(self):
        #Posiciona la nave
        self.nave.posicionar_nave()
        indice_par = 0
        indice_impar = 0
        #Crea los enemigos en una lista
        for x in range(2*self.rango):
            if self.rango == 1:
                self.lista_enemigos += [Enemigo(self.canvas_game,140+(x*140), 100,self.rango)]
            elif self.rango == 2:
                if x%2 == 0:
                    self.lista_enemigos += [Enemigo(self.canvas_game,140+(indice_par*140), 100,self.rango)]
                    indice_par += 1
                else:
                    self.lista_enemigos += [Enemigo(self.canvas_game,140+((indice_impar)*140), 200,self.rango)]
                    indice_impar +=1
            elif self.rango == 3:
                if x%2 == 0:
                    self.lista_enemigos += [Enemigo(self.canvas_game,60+(indice_par*140), 100,self.rango)]
                    indice_par += 1
                else:
                     self.lista_enemigos += [Enemigo(self.canvas_game,60+((indice_impar)*140), 200,self.rango)]
                     indice_impar +=1
            #Llama la funcion start_enemy
            self.lista_enemigos[x].start_enemy()
        #Inicia Clase Score
        self.score = Score(self.canvas_game,self.rango,self.name)
        #Inicia el Thread para verificar colisiones
        self.check_collision_thread.start()
        
    #Funcion que verifica si hay colisiones
    def check_collision(self):

        while (True):
            for x in range(len(self.lista_enemigos)):
                enemigo = self.lista_enemigos[x]
                if ((enemigo.get_enemy_right() >= self.nave.ship_posx) &
                   (enemigo.enemy_y <= self.nave.get_y_down()) &
                   (enemigo.get_enemy_down() >= self.nave.ship_posy) &
                   (enemigo.enemy_x <= self.nave.get_x_right())):
                       playsound('nave.wav', block = False)
                       self.player.colision()
                        
            time.sleep(1)
                 

#Clase Nave
class Nave:
    def __init__(self,canvas_game):
        self.ship = load_image('player.png')
        self.canvas_game = canvas_game
        self.label_ship = Label(canvas_game,bg = 'black', image = self.ship)
        self.ship_posx = 220
        self.ship_posy = 600
    #Funcion que posiciona la nave y crea los binds
    def posicionar_nave(self):
        self.label_ship.place(x = self.ship_posx,y = self.ship_posy)
        self.label_ship.focus_set()
        self.label_ship.bind("<Right>",self.right)
        self.label_ship.bind("<Left>", self.left)
        self.label_ship.bind("<Up>",self.up)
        self.label_ship.bind("<Down>",self.down)
    #Funcion que obtiene el valor de x del largo de la nave
    def get_x_right(self):
        return self.ship_posx + 90
    #Funcion que obtiene el valor de y del ancho de la nave
    def get_y_down(self):
        return self.ship_posy +80
        
    #Direccion Right de la nave(bind)    
    def right(self,event):
        if (self.ship_posx < 460):
            self.ship_right = load_image('player_right.png')
            self.label_ship.configure(image=self.ship_right)
            self.label_ship.image = self.ship_right
            self.ship_posx += 20
            self.ship_posy += 0
            self.label_ship.place(x= self.ship_posx, y = self.ship_posy)
    #Direccion Left de la nave(bind)  
    def left(self,event):
        if (self.ship_posx > 20):
            self.ship_left = load_image('player_left.png')
            self.label_ship.configure(image=self.ship_left)
            self.label_ship.image = self.ship_left
            self.ship_posx -= 20
            self.ship_posy -= 0
            self.label_ship.place(x= self.ship_posx, y = self.ship_posy)
    #Direccion Up de la nave(bind)
    def up(self,event):
        if (self.ship_posy > 40):
            self.ship_up = load_image('player.png')
            self.label_ship.configure(image = self.ship_up)
            self.label_ship.image = self.ship_up
            self.ship_posx += 0
            self.ship_posy -= 20
            self.label_ship.place(x= self.ship_posx, y = self.ship_posy)
    #Direccion Down de la nave(bind)
    def down(self,event):
        if (self.ship_posy < 620):
            self.ship_down = load_image('player_down.png')
            self.label_ship.configure(image = self.ship_down)
            self.label_ship.image = self.ship_down
            self.ship_posx += 0
            self.ship_posy += 20
            self.label_ship.place(x= self.ship_posx, y = self.ship_posy)

#Clase Enemigo
class Enemigo:
    def __init__(self,canvas_game, pos_x,pos_y,rango):
        self.enemy_x = pos_x
        self.enemy_y = pos_y
        self.rango = rango
        self.enemy_move = random.randint(0,3)
        self.enemy_image = load_image('enemy2.png')
        self.label_enemy = Label(canvas_game, bg = 'black', image = self.enemy_image)
        self.thread_movement = threading.Thread(target=self.move)
        self.thread_movement.setDaemon(True)
    #Funcion que obtiene el valor de x del largo del enemigo
    def get_enemy_right(self):
        return self.enemy_x + 120
    #Funcion que obtiene el valor de y del ancho de la nave
    def get_enemy_down(self):
        return self.enemy_y + 60
        
    #Inicia el Thread que controla los movimientos    
    def start_enemy(self):
        self.thread_movement.start()

    #Funcion que controla el movimiento de los enemigos
    def move(self):
        #Movimientos Aleatorios
        while (True):
            if self.enemy_x <= 0:
                self.enemy_move = random.choice([1,3])
                playsound('golpe.wav', block = False)
            elif self.enemy_x >= 420:
                self.enemy_move = random.choice([0,2])
                playsound('golpe.wav', block = False)
            if self.enemy_y <= 40:
                self.enemy_move = random.choice([2,3])
                playsound('golpe.wav', block = False)
            elif self.enemy_y >= 620:
                self.enemy_move = random.choice([0,1])
                playsound('golpe.wav', block = False)
                
            #0 = Izquierda Superior
            #1 = Derecha Superior
            #2 Izquierda Inferior
            #3 Derecha Inferior
            if self.enemy_move == 0:
                if self.rango == 1:
                    self.enemy_x -= 10
                    self.enemy_y -= 10
                else:
                    self.enemy_x -= 20
                    self.enemy_y -= 20
            elif self.enemy_move == 1:
                if self.rango == 1:
                    self.enemy_x += 10
                    self.enemy_y -= 10
                else:
                    self.enemy_x += 20
                    self.enemy_y -= 20
            elif self.enemy_move == 2:
                if self.rango == 1:
                    self.enemy_x -= 10
                    self.enemy_y += 10
                else:
                    self.enemy_x -= 20
                    self.enemy_y += 20
            else:
                if self.rango == 1:
                    self.enemy_x += 10
                    self.enemy_y += 10
                else:
                    self.enemy_x += 20
                    self.enemy_y += 20

            self.label_enemy.place(x=self.enemy_x,y=self.enemy_y)
            self.label_enemy.configure(image = self.enemy_image)
            time.sleep(0.2)
            
#Clase Player
class Player:
    def __init__(self,canvas_game,game):
        self.game = game
        self.canvas_game = canvas_game
        self.player_life = 3
        self.label_player_life = Label(self.canvas_game, text = self.player_life ,font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_player_life.place(x= 225,y= 5)
        self.label_player = Label(self.canvas_game, text = "Life:" ,font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_player.place(x= 190,y= 5)            
    #Funcion que resta una vida cada vez que la nave colisione
    def colision(self):
        if self.player_life == 1:
            self.game.destroy()
            self.perdedor = Perdedor()
        self.player_life -=1
        self.label_player_life = Label(self.canvas_game, text = self.player_life ,font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_player_life.place(x= 225,y= 5)
        
        
        
#Clase Timer        
class Timer:
    def __init__(self,canvas_game,game,rango,name):
        self.game = game
        self.name = name
        self.rango = rango
        self.label_time = Label(canvas_game, text = "Time:",font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_time.place(x=125, y = 5)
        self.meter = 40
        self.label_meter = Label(canvas_game, text = self.meter, font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_meter.place(x= 165, y=5)
        self.label_meter.after(1000, self.refresh_timer)
        self.score = Score(canvas_game,self.rango,self.name)
        
        

    #Actualiza el Tiempo y Llama a otras funciones cuando el tiempo == 60 seg
    def refresh_timer(self):
        if self.meter >= 60:
            self.game.destroy()
            self.ganador = Ganador(self.rango,self.name)
            self.score.agregar_score()
            self.score.division()
            
            
        self.meter += 1
        self.label_meter.configure(text=self.meter)
        self.label_meter.after(1000,self.refresh_timer)
#Clase Score
class Score:
    def __init__(self,canvas_game,rango,name):
        self.name = name
        self.rango = rango
        self.player_score = 0
        self.lista_score = [["Allan",60],["Allan",60],["Marianna",60],["Allan",54],["Allan",49],["Marianna",45],["Marianna",42]]
        self.label_player_score= Label(canvas_game, text = "Score:" ,font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_player_score.place(x = 340, y = 5)
        self.label_score = Label(canvas_game, text = self.player_score ,font = ("Arial",14), bg = 'black', fg = 'yellow')
        self.label_score.place(x = 390, y = 5)
        self.label_score.after(1000, self.refresh_score)
    #Actualiza la puntuacion del usuario dependiendo del nivel
    def refresh_score(self):
        if self.rango == 1:
            self.player_score += 1
            self.label_score.configure(text=self.player_score)
            self.label_score.after(1000,self.refresh_score)
        elif self.rango == 2:
            self.player_score += 3
            self.label_score.configure(text=self.player_score)
            self.label_score.after(1000,self.refresh_score)
        else:
            self.player_score += 5
            self.label_score.configure(text=self.player_score)
            self.label_score.after(1000,self.refresh_score)
                    
    #Funcion que clasifica los elementos de la lista en menores,mayores y el pivot
    def division(self):
        self.mayores = []
        self.menores = []
        self.pivot = self.lista_score[0][1]

        for x in range(1,len(lista)):
            if list(self.lista_score[x][1]) < self.pivot:
                self.menores += self.lista_score[x]
            else:
                self.mayores += self.lista_score[x]
        self.quick_sort()
    #Funcion que acomoda la lista de mayor a menor
    def quick_sort(self):
        self.lista_score = self.mayores+[self.pivot]+self.menores
            
        
    #Funcion que escribe las puntuaciones en el archivo .txt
    def agregar_score(self):
        self.file = open('Best_Scores.txt',"w")
        for x in range(7):
            self.text = self.file.write(str(self.lista_score[x]))
            self.espacio = self.file.write("\n")
        self.file.close()

        
        
            
#Clase Best_Score
class Best_Score:
    def __init__(self):
        #Crea la pantalla de mejores puntuaciones
        self.score_window = Toplevel()
        self.score_window.title("Best Scores")

        self.score_window.minsize(500,500)

        self.score_window.resizable(width = NO, height = NO)
        
        self.canvas_score = Canvas(self.score_window,width = 500, height = 500,highlightthickness = 0, bg = 'black')
        self.canvas_score.place(x=0,y=0)

        self.bg = load_image('Fondo2.png')
        self.label_bg = Label(self.canvas_score,bg = 'black', image = self.bg)
        self.label_bg.place(x = 0,y = 0)

        self.button_score_exit = Button(self.canvas_score, text = "Exit",background = 'black', command = self.exit_score)
        self.button_score_exit.place(x=460,y=460)
        #Abre el archivo .txt
        self.file = open('Best_Scores.txt','r')
        #Lee el archivo .txt
        self.text = self.file.read()

        self.label_score = Label(self.score_window, text = self.text, font= ("Arial",30), bg = 'black', fg = 'white')
        self.label_score.place(x=140,y=140)
    #Funcion que cierra la ventana de puntuaciones
    def exit_score(self):
        self.score_window.destroy()
#Clase Ganador
class Ganador:
    def __init__(self,rango,name):
        #Crea la pantalla del ganador
        self.pantalla_ganador = Toplevel()
        self.pantalla_ganador.minsize(500,500)
        self.pantalla_ganador.title("Ganador")
        self.pantalla_ganador.resizable(width = NO, height = NO)

        self.canvas_ganador = Canvas(self.pantalla_ganador,width = 500, height = 500,highlightthickness = 0, bg = 'black')
        self.canvas_ganador.place(x=0,y=0)
        self.rango = rango
        self.name = name

        self.ganador_img = load_image('Fondo.png')
        self.label_ganador = Label(self.canvas_ganador,bg = 'black', image = self.ganador_img)
        self.label_ganador.place(x = 0,y = 0)

        self.label_ganaste = Label(self.canvas_ganador,text = 'Ganaste!',font = ("Arial",50), bg = 'black', fg = 'red')
        self.label_ganaste.place(x=140,y=180)

        self.label_fin = Label(self.canvas_ganador,text = 'Fin del Juego!',font = ("Arial",30), bg = 'black', fg = 'white')
        #Verifica el nivel para ir al siguiente nivel o terminar el juego
        if self.rango == 1 or self.rango == 2:
            self.next_lvl = Button(self.pantalla_ganador, text = 'Siguiente Nivel',font = ("Arial",16),background = 'black', command = self.Next_lvl)
            self.next_lvl.place(x=180, y= 270)
        else:
            self.label_fin.place(x=150, y= 250 )
            

        self.button_exit = Button(self.pantalla_ganador, text = 'Exit',font = ("Arial",16),background = 'black', command = self.exit)
        self.button_exit.place(x=460, y= 460)

    #Funcion que inicia el siguiente nivel
    def Next_lvl(self):
        self.rango += 1
        self.game = Game(self.name,self.rango)
        self.game.iniciar_juego()
    #Funcion que destruye la pantalla del ganador
    def exit(self):
        self.pantalla_ganador.destroy()
        
            
#Clase Perdedor
class Perdedor:
    def __init__(self):
        #Crea la pantalla del perdedor
        self.pantalla_perdedor = Toplevel()
        self.pantalla_perdedor.minsize(500,500)
        self.pantalla_perdedor.title("Perdedor")
        self.pantalla_perdedor.resizable(width = NO, height = NO)

        self.canvas_perdedor = Canvas(self.pantalla_perdedor,width = 500, height = 500,highlightthickness = 0, bg = 'black')
        self.canvas_perdedor.place(x=0,y=0)

        self.perdedor_img = load_image('Fondo.png')
        self.label_perdedor = Label(self.canvas_perdedor,bg = 'black', image = self.perdedor_img)
        self.label_perdedor.place(x = 0,y = 0)

        self.label_perdedor = Label(self.canvas_perdedor,text = 'Perdiste!',font = ("Arial",50), bg = 'black', fg = 'red')
        self.label_perdedor.place(x=140,y=180)

        self.button_exit = Button(self.pantalla_perdedor, text = 'Exit',font = ("Arial",16),background = 'black', command = self.exit)
        self.button_exit.place(x=230, y= 270)
    #Funcion que destruye la pantalla del perdedor
    def exit(self):
        self.pantalla_perdedor.destroy()


        

        

        
        
    
    
        
        

window = Tk()
selection = IntVar()
window.minsize(550,700)
window.resizable(width = NO, height = NO)
ventana_principal = Ventana_Principal(window)
window.title("SpaceRush")
window.mainloop()


