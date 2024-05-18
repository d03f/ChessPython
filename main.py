import pygame, sys
import numpy as np

colors = {"blanco":(255,255,255), "negro":(0,0,0), "gris":(30,30,30), "marron": (122,80,57)}

tablero_x = "87654321"
tablero_y = "abcdefgh"

tablero_grid = {}

tablero_cords_x = []
tablero_cords_y = []


piezas_positions = {}
piezas_next = {}



#Valor más proximo a una lista de valores
def closest_value(value, list):
  array = np.asarray(list)
  i = (np.abs(array - value)).argmin()
  return array[i]

def check_for_piece(positions):
    x = 0
    for a in positions:
        cord = tablero_grid[a]
        ficha = piezas_positions[cord]
        if ficha != "vacia":x = 1
    return x == 1


#TODO Si el rey come a una pieza a la cual estan protegida se bugea
def check_jaque(position, pieza, turno_w):
    #Posicion letra: position[0]
    #Positicion num: position[1]
    #King positions = position

    if pieza == "king_w":
        
        #Jaques Rectos
        if True:
            enemigo_recto = []
            print("\n\n")

            #!Posiciones delante
            pos_delante = 8 - int(position[1])
            if pos_delante != 0:
                for i in range(pos_delante):
                    cuadricula = f"{position[0]}{(i+1)+int(position[1])}"
                    pieza_delante = piezas_next[cuadricula]
                    #Si hay una ficha aliada delante
                    if pieza_delante.endswith("w"):
                        print("Aliados delante")
                        break

                    elif pieza_delante.endswith("b"):
                        print("Enemigos delante")
                        enemigo_recto.append(pieza_delante)
                        break
            
            #!Posiciones detras
            pos_detras = int(position[1]) - 1

            if pos_detras != 0:
                for i in range(pos_detras):
                    cuadricula = f"{position[0]}{i+1}"
                    pieza_detras = piezas_next[cuadricula]
                    if pieza_detras.endswith("w"):
                        print("Aliados detras")
                        break
                    elif pieza_detras.endswith("b"):
                        print("Enemigos detras")
                        enemigo_recto.append(pieza_detras)
                        break


            #!Posiciones der
            #                  posicion del rey en eje x
            pos_rey = tablero_y.index(position[0]) + 1
            pos_der = 8 - (tablero_y.index(position[0]) + 1)
            
            if pos_der != 0:
                for i in range(pos_der):
                    #                tablero_y[ posiciones der rey ]
                    cuadricula = f"{tablero_y[(i)+pos_rey]}{position[1]}"
                    pieza_der = piezas_next[cuadricula]
                    if pieza_der.endswith("w"):
                        print("Aliados derecha")
                        break      
                    elif pieza_der.endswith("b"):
                        print("Enemigos derecha")
                        enemigo_recto.append(pieza_der)
                        break
            
            #!Posiciones izq
            pos_rey = tablero_y.index(position[0]) + 1
            pos_izq = (tablero_y.index(position[0]) + 1)-1

            if pos_izq != 0:
                for i in range(pos_izq):
                    cuadricula = f"{tablero_y[(pos_rey - (i+1)) - 1]}{position[1]}"
                    pieza_izq = piezas_next[cuadricula]
                    if pieza_izq.endswith("w"):
                        print("Aliados izquierda")
                        break
                    elif pieza_izq.endswith("b"):
                        print("Enemigos izquierda")
                        enemigo_recto.append(pieza_izq)
                        break
        
        #Jaques diagonales
        if True:
            print()
            enemigo_diagonal = []

            #Derecha delante
            pos_letra = tablero_y.index(position[0]) + 1
            pos_num = int(position[1])

            #Delante derecha
            for i in range(99):
                #print(pos_letra + i)
                #print(pos_num + i)
                if pos_letra + i == 8 or pos_num + i + 1 == 0:
                    print("Out delante derecha")
                    break
                cuadricula = f"{tablero_y[pos_letra + i ]}{pos_num + i + 1}"
                pieza_delante = piezas_next[cuadricula]
                if pieza_delante.endswith("w"):
                    print("Aliado derecha arriba")
                    break
                elif pieza_delante.endswith("b"):
                    print("Enemigo derecha arriba")
                    enemigo_diagonal.append(pieza_delante)



            #Delante izquierda
            
            for i in range(99):
                #print(pos_num + i)
                    
                if (pos_letra - (i +1)) == 0 or (pos_num + i + 1) == 8:
                    print("OUT delante izquierda")
                    break
                cuadricula = f"{tablero_y[(pos_letra - (i +1))-1]}{pos_num + i + 1}"
                pieza_delante = piezas_next[cuadricula]
                if pieza_delante.endswith("w"):
                    print("Aliado izquierda arriba", cuadricula)
                    break
                elif pieza_delante.endswith("b"):
                    print("Enemigo izquierda arriba")
                    enemigo_diagonal.append(pieza_delante)
                    break
            
            #Atras derecha
            for i in range(99):
                #print(pos_letra + i)
                #print(pos_num + i)
                if pos_letra + i == 8 or pos_num - (i +1) == 0:
                    print("OUT atras derecha")
                    break
                cuadricula = f"{tablero_y[pos_letra + i ]}{pos_num - (i +1)}"
                pieza_delante = piezas_next[cuadricula]
                if pieza_delante.endswith("w"):
                    print("Aliado derecha abajo")
                    break
                elif pieza_delante.endswith("b"):
                    print("Enemigo derecha abajo")
                    enemigo_diagonal.append(pieza_delante)
                    break

            #atras izquierda
            for i in range(99):
                #print(pos_num + i)
                
                if pos_letra - (i +1) == 0 or pos_num - (i +1) == 0:
                    print("OUT atras izquierda")
                    break
                cuadricula = f"{tablero_y[(pos_letra - (i +1))-1]}{(pos_num - (i +1))}"
                pieza_delante = piezas_next[cuadricula]
                if pieza_delante.endswith("w"):
                    print("Aliado izquierda atras", cuadricula)
                    break
                elif pieza_delante.endswith("b"):
                    print("Enemigo izquierda atras")
                    enemigo_diagonal.append(pieza_delante)
                    break

        #Peones
        if True:
            peones_amen = []

            #arriba_izq
            pos_letra = tablero_y.index(position[0]) + 1
            pos_num = int(position[1])

            try:cuadricula = f"{tablero_y[pos_letra]}{pos_num+1}"
            except:pass
            pieza_delante = piezas_next[cuadricula]
            if pieza_delante.startswith("peon"):
                peones_amen.append(pieza_delante)

            #arriba_der
            pos_letra = tablero_y.index(position[0]) + 1
            pos_num = int(position[1])

            try:cuadricula = f"{tablero_y[pos_letra-2]}{pos_num+1}"
            except:pass
            pieza_delante = piezas_next[cuadricula]
            print(cuadricula)
            if pieza_delante.startswith("peon"):
                peones_amen.append(pieza_delante)



        for i in enemigo_recto:
            if i.startswith("queen") or i.startswith("torre"):
                print("Will be right back")
                if turno_w:return True
        for i in enemigo_diagonal:
            if i.startswith("queen") or i.startswith("alfil"):
                print("Will be right back")
                if turno_w:return True
        for i in peones_amen:
            if i.endswith("b"):
                print("Will be right back")
                if turno_w:return True
        

#CLASES

class Tablero(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


#Usada a la hora de arrastrar y rellenar huecos
class Vacia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces.png")
        self.rect = self.image.get_rect()
    def move(self, pos):
        pass

class King_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/king_b.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()
    
class King_w(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/king_w.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()
    
class Queen_w(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/queen_w.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

class Torre_w(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/torre_w.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()
    
class Alfil_w(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/alfil_w.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()
    
class Horse_w(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/horse_w.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

class Peon_w(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/peon_w.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

#-----NEGRAS
class Queen_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/queen_b.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

class Torre_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/torre_b.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

class Alfil_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/alfil_b.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

class Horse_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/horse_b.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

class Peon_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/pieces/peon_b.png")
        self.rect = self.image.get_rect()
    def update(self, pos):
        self.rect.center = pos
    def move(self):
        self.rect.center = pygame.mouse.get_pos()

#Ventana
pygame.init()
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("images/bg.png")
pygame.mouse.set_visible(True)

font = pygame.font.Font(pygame.font.get_default_font(), 36)




#TABLERO
tablero_group = pygame.sprite.Group()
for a in range(8):
    for b in range(8):
        pos_x = 100 + 50*b
        pos_y = 100 + 50*a
        #Empezar por gris si es impar
        if a % 2:color = colors["marron"] if b % 2 == 0 else colors["blanco"]
        #Empezar por blanco si es par
        else:color = colors["blanco"] if b % 2 == 0 else colors["marron"]

        tablero = Tablero(50,50,pos_x,pos_y,color)
        tablero_group.add(tablero)

        #añadir lista posiciones
        tablero_grid.update({(pos_x, pos_y):f"{tablero_y[b]}{tablero_x[a]}"})
        tablero_cords_x.append(pos_x)
        tablero_cords_y.append(pos_y)

        piezas_positions.update({f"{tablero_y[b]}{tablero_x[a]}":""})


#PIEZAS
piezas_group = piezas_group = pygame.sprite.Group()


#KING_B
king_b = King_b()
king_b_group = pygame.sprite.Group()
king_b_group.add(king_b)

piezas_group.add(king_b_group)
#Position
king_b_group.update((300, 100))
piezas_positions.update({tablero_grid[(300, 100)]:"king_b"})

#Queen_B
queen_b = Queen_b()
queen_b_group = pygame.sprite.Group()
queen_b_group.add(queen_b)
piezas_group.add(queen_b_group)
#Position
queen_b_group.update((250, 100))
piezas_positions.update({tablero_grid[(250, 100)]:"queen_b"})

#TORRE_1b
torre_1b = Torre_b()
torre_1b_group = pygame.sprite.Group()
torre_1b_group.add(torre_1b)
piezas_group.add(torre_1b_group)
#Position
torre_1b_group.update((100, 100))
piezas_positions.update({tablero_grid[(100, 100)]:"torre_1b"})

#TORRE_2b
torre_2b = Torre_b()
torre_2b_group = pygame.sprite.Group()
torre_2b_group.add(torre_2b)
piezas_group.add(torre_2b_group)
#Position
torre_2b_group.update((450, 100))
piezas_positions.update({tablero_grid[(450, 100)]:"torre_2b"})

#ALFIL_1b
alfil_1b = Alfil_b()
alfil_1b_group = pygame.sprite.Group()
alfil_1b_group.add(alfil_1b)
piezas_group.add(alfil_1b_group)
#Position
alfil_1b_group.update((200, 100))
piezas_positions.update({tablero_grid[(200, 100)]:"alfil_1b"})

#ALFIL_2b
alfil_2b = Alfil_b()
alfil_2b_group = pygame.sprite.Group()
alfil_2b_group.add(alfil_2b)
piezas_group.add(alfil_2b_group)
#Position
alfil_2b_group.update((350, 100))
piezas_positions.update({tablero_grid[(350, 100)]:"alfil_2b"})

#HORSE_1b
horse_1b = Horse_b()
horse_1b_group = pygame.sprite.Group()
horse_1b_group.add(horse_1b)
piezas_group.add(horse_1b_group)
#Position
horse_1b_group.update((150, 100))
piezas_positions.update({tablero_grid[(150, 100)]:"horse_1b"})

#HORSE_2b
horse_2b = Horse_b()
horse_2b_group = pygame.sprite.Group()
horse_2b_group.add(horse_2b)
piezas_group.add(horse_2b_group)
#Position
horse_2b_group.update((400, 100))
piezas_positions.update({tablero_grid[(400, 100)]:"horse_2b"})

#PEON
for i in range(8):
    a += 1
    exec(f"peon_{a}b = Peon_b()")
    exec(f"peon_{a}b_group = pygame.sprite.Group()")
    exec(f"peon_{a}b_group.add(peon_{a}b)")
    exec(f"piezas_group.add(peon_{a}b_group)")
    #Position
    exec(f"peon_{a}b_group.update(({100 + 50*i}, 150))")
    piezas_positions.update({tablero_grid[(100 + 50*i, 150)]:f"peon_{a}b"})


#--------WHITE-----------
#KING_W
king_w = King_w()
king_w_group = pygame.sprite.Group()
king_w_group.add(king_w)
piezas_group.add(king_w_group)
#Position
king_w_group.update((300, 450))
piezas_positions.update({tablero_grid[(300, 450)]:"king_w"})

#Queen_W
queen_w = Queen_w()
queen_w_group = pygame.sprite.Group()
queen_w_group.add(queen_w)
piezas_group.add(queen_w_group)
#Position
queen_w_group.update((250, 450))
piezas_positions.update({tablero_grid[(250, 450)]:"queen_w"})

#Queen add
queen_addw = Queen_w()
queen_addw_group = pygame.sprite.Group()
queen_addw_group.add(queen_addw)

#TORRE_1W
torre_1w = Torre_w()
torre_1w_group = pygame.sprite.Group()
torre_1w_group.add(torre_1w)
piezas_group.add(torre_1w_group)
#Position
torre_1w_group.update((100, 450))
piezas_positions.update({tablero_grid[(100, 450)]:"torre_1w"})

#TORRE_2W
torre_2w = Torre_w()
torre_2w_group = pygame.sprite.Group()
torre_2w_group.add(torre_2w)
piezas_group.add(torre_2w_group)
#Position
torre_2w_group.update((450, 450))
piezas_positions.update({tablero_grid[(450, 450)]:"torre_2w"})

#ALFIL_1W
alfil_1w = Alfil_w()
alfil_1w_group = pygame.sprite.Group()
alfil_1w_group.add(alfil_1w)
piezas_group.add(alfil_1w_group)
#Position
alfil_1w_group.update((200, 450))
piezas_positions.update({tablero_grid[(200, 450)]:"alfil_1w"})

#ALFIL_2W
alfil_2w = Alfil_w()
alfil_2w_group = pygame.sprite.Group()
alfil_2w_group.add(alfil_2w)
piezas_group.add(alfil_2w_group)
#Position
alfil_2w_group.update((350, 450))
piezas_positions.update({tablero_grid[(350, 450)]:"alfil_2w"})

#HORSE_1W
horse_1w = Horse_w()
horse_1w_group = pygame.sprite.Group()
horse_1w_group.add(horse_1w)
piezas_group.add(horse_1w_group)
#Position
horse_1w_group.update((150, 450))
piezas_positions.update({tablero_grid[(150, 450)]:"horse_1w"})

#HORSE_2W
horse_2w = Horse_w()
horse_2w_group = pygame.sprite.Group()
horse_2w_group.add(horse_2w)
piezas_group.add(horse_2w_group)
#Position
horse_2w_group.update((400, 450))
piezas_positions.update({tablero_grid[(400, 450)]:"horse_2w"})

#PEON
for i in range(8):
    a += 1
    exec(f"peon_{a}w = Peon_w()")
    exec(f"peon_{a}w_group = pygame.sprite.Group()")
    exec(f"peon_{a}w_group.add(peon_{a}w)")
    exec(f"piezas_group.add(peon_{a}w_group)")
    #Position
    exec(f"peon_{a}w_group.update(({100 + 50*i}, 400))")
    piezas_positions.update({tablero_grid[(100 + 50*i, 400)]:f"peon_{a}w"})



#Ultima class
#VACIA
#Esta class la vamos a utilizar a la hora de arrastrar y rellenar huecos
vacia = Vacia()
vacia_group = pygame.sprite.Group()
vacia_group.add(vacia)


pieza_select_class = Vacia


text_turno_w = font.render('Turno: Blancas', True, (0, 0, 0))
text_turno_b = font.render('Turno:Negras', True, (0, 0, 0))
text_win_w = font.render('Han ganado Blancas', True, (0, 0, 0))
text_win_b = font.render('Han ganado Negras', True, (0, 0, 0))



#Poner vacias en todas las casillas fin ficha
for i in tablero_grid:
    if piezas_positions[tablero_grid[i]] == "":
        piezas_positions.update({tablero_grid[i]:"vacia"})

#Test
#print(piezas_positions)

turno_w = True
win = False

#MAIN
while True:
    
    for event in pygame.event.get():
        ficha_comida = None
        pieza_select_main = None

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Grid mas cercano
            closest_x_up = closest_value(event.pos[0], tablero_cords_x)
            closest_y_up = closest_value(event.pos[1], tablero_cords_y)

            #Buscar que ficha esta en el grid seleccionado
            pieza_select = piezas_positions[tablero_grid[(closest_x_up, closest_y_up)]]

            #Guardar el grupo en el que la ficha este seleccionada
            exec(f'pieza_select_class = {pieza_select}_group')
            
            
        
        elif event.type == pygame.MOUSEBUTTONUP:
            #Poner la casilla anterior en vacia
            piezas_positions.update({tablero_grid[(closest_x_up, closest_y_up)]:"vacia"})
            #Volver a poner en el mouse a Vacia
            pieza_select_class = vacia_group
            closest_x_down = closest_value(event.pos[0], tablero_cords_x)
            closest_y_down = closest_value(event.pos[1], tablero_cords_y)

            mov_x = closest_x_up - closest_x_down
            mov_y = closest_y_up - closest_y_down
            

            #Movimiento ficha
            if pieza_select.startswith("king_"):
                #Restriccion movimiento
                if mov_x < -50 or mov_x > 50 or mov_y < -50 or mov_y > 50:
                    closest_x_down, closest_y_down = closest_x_up, closest_y_up

            elif pieza_select.startswith("queen_"):
                if mov_x != 0 and mov_y != 0 and abs(mov_x) != abs(mov_y):
                    closest_x_down, closest_y_down = closest_x_up, closest_y_up
            
            elif pieza_select.startswith("torre_"):
                if mov_x != 0 and mov_y != 0:
                    closest_x_down, closest_y_down = closest_x_up, closest_y_up

            elif pieza_select.startswith("alfil_"):
                if abs(mov_x) != abs(mov_y):
                    closest_x_down, closest_y_down = closest_x_up, closest_y_up
                
            elif pieza_select.startswith("horse_"):
                moves_horse = {(100, 50): True, (100,-50): True, (-100, 50):True, (-100,-50): True,
                (50,100):True, (50,-100):True, (-50,100):True, (-50,-100):True}
                
                try:moves_horse[(mov_x, mov_y)]
                except:closest_x_down, closest_y_down = closest_x_up, closest_y_up

            #Peones
            elif pieza_select.startswith("peon_") and pieza_select.endswith("w"):
                #Comer
                hay_pieza = check_for_piece([(closest_x_down, closest_y_down)])
                if hay_pieza:
                    if abs(mov_x) == 50 and mov_y == 50:
                        pass
                    else:closest_x_down, closest_y_down = closest_x_up, closest_y_up
                

                #Movimiento inicial
                elif not hay_pieza and closest_y_up == 400 and mov_y == 100:
                    pass
                #Movimientos secundarios
                else:
                    if not hay_pieza and mov_x != 0:
                        closest_x_down, closest_y_down = closest_x_up, closest_y_up
                    elif not hay_pieza and mov_y == -50 or mov_y > 50:
                        closest_x_down, closest_y_down = closest_x_up, closest_y_up

            elif pieza_select.startswith("peon_") and pieza_select.endswith("b"):
                #Comer
                hay_pieza = check_for_piece([(closest_x_down, closest_y_down)])
                if hay_pieza:
                    if abs(mov_x) == 50 and mov_y == -50:
                        pass
                    else:closest_x_down, closest_y_down = closest_x_up, closest_y_up

                #Movimiento inicial
                elif not hay_pieza and closest_y_up == 150 and mov_y == -100:
                    pass
                #Movimientos secundarios
                else:
                    if not hay_pieza and mov_x != 0:
                        closest_x_down, closest_y_down = closest_x_up, closest_y_up
                    elif not hay_pieza and mov_y != -50 :
                        closest_x_down, closest_y_down = closest_x_up, closest_y_up

                    

            


            #Ficha comida = posicion a la que movemos la ficha select
            ficha_comida = piezas_positions[tablero_grid[(closest_x_down, closest_y_down)]]

            #Comprobar si la ficha a comer es del mismo color
            if pieza_select[-1] == ficha_comida[-1]:
                closest_x_down, closest_y_down = closest_x_up, closest_y_up
                ficha_comida = piezas_positions[tablero_grid[(closest_x_down, closest_y_down)]]

            #Actualizar los valores mov
            mov_x = closest_x_up - closest_x_down
            mov_y = closest_y_up - closest_y_down

            #Comprobar si en el recorrido hay otra ficha 
            recorrido = []

            reco_y_up = closest_y_up
            reco_y_down = closest_y_down

            reco_x_up = closest_x_up
            reco_x_down = closest_x_down
            
            if int(abs(reco_y_up-reco_y_down)/50-1) > 0:
                for i in range(int(abs(reco_y_up-reco_y_down)/50-1)):
                    if reco_y_down > reco_y_up:
                        reco_pos_y = reco_y_down - 50*(i+1)
            
                    elif reco_y_down < reco_y_up:
                        reco_pos_y = reco_y_down + 50*(i+1)

                    if reco_x_down > reco_x_up:
                        reco_pos_x = reco_x_down - 50*(i+1)

                    elif reco_x_down < reco_x_up:
                        reco_pos_x = reco_x_down + 50*(i+1)

                    if reco_x_down == reco_x_up:
                        reco_pos_x = reco_x_down

                    elif reco_y_down == reco_y_up:
                        reco_pos_y = reco_y_down
                    
                    recorrido.append((reco_pos_x, reco_pos_y))
            else:
                for i in range(int(abs(reco_x_up-reco_x_down)/50-1)):
                    
                    if reco_y_down > reco_y_up:
                        reco_pos_y = reco_y_down - 50*(i+1)
                
                    elif reco_y_down < reco_y_up:
                        reco_pos_y = reco_y_down + 50*(i+1)

                    if reco_x_down > reco_x_up:
                        reco_pos_x = reco_x_up + 50*(i+1)

                    elif reco_x_down < reco_x_up:
                        reco_pos_x = reco_x_up - 50*(i+1)

                    if reco_x_down == reco_x_up:
                        reco_pos_x = reco_x_down

                    elif reco_y_down == reco_y_up:
                        reco_pos_y = reco_y_down
                
                    recorrido.append((reco_pos_x, reco_pos_y))
            if check_for_piece(recorrido):
                if not pieza_select.startswith("horse_"):
                    print("Ficha en el recorrido")
                    closest_x_down, closest_y_down = closest_x_up, closest_y_up
                    ficha_comida = piezas_positions[tablero_grid[(closest_x_down, closest_y_down)]]
                
            
            


            #Comprobar por ficha comida despues de haber comporbado turnos
            ficha_comida = piezas_positions[tablero_grid[(closest_x_down, closest_y_down)]]

            if pieza_select[-1] == ficha_comida[-1]:
                closest_x_down, closest_y_down = closest_x_up, closest_y_up
                ficha_comida = piezas_positions[tablero_grid[(closest_x_down, closest_y_down)]]



            #Comprobar jaque
            piezas_next = dict(piezas_positions)
            piezas_next.update({tablero_grid[(closest_x_down, closest_y_down)]:pieza_select})
            
            for i in piezas_next:
                if piezas_next[i].startswith("king"):
                    if check_jaque(i, piezas_next[i], turno_w):
                        print("NO NO No")
                        closest_x_down, closest_y_down = closest_x_up, closest_y_up


            #Sistema Turnos
            if turno_w and pieza_select.endswith("w") :
                if closest_y_up != closest_y_down or closest_x_up != closest_x_down:
                    if ficha_comida.endswith("b") or ficha_comida == "vacia":
                        turno_w = False
                    else:closest_x_down, closest_y_down = closest_x_up, closest_y_up; ficha_comida = "vacia"

            elif not turno_w and pieza_select.endswith("b"):
                if closest_y_up != closest_y_down or closest_x_up != closest_x_down:
                    if ficha_comida.endswith("w") or ficha_comida == "vacia":
                        turno_w = True
                    else:closest_x_down, closest_y_down = closest_x_up, closest_y_up; ficha_comida = "vacia"
            else:
                print("No es el turno!")
                closest_x_down, closest_y_down = closest_x_up, closest_y_up; ficha_comida = "vacia"


            #Mover ficha
            if pieza_select != "vacia":
                piezas_positions.update({tablero_grid[(closest_x_down, closest_y_down)]:pieza_select})
                exec(f"{pieza_select}_group.update((closest_x_down, closest_y_down))")
                print(f"{pieza_select} {tablero_grid[(closest_x_down, closest_y_down)]}, come {ficha_comida} {tablero_grid[(closest_x_down, closest_y_down)]}")
                #Ganar al comer un rey
                
                if ficha_comida.startswith("king_"):
                    win = True

            



        #ficha_vacia_main usado en el siguiente apartado
        try:pieza_select_main = pieza_select
        except:pass
        #Comer si la ficha no esta vacia y la ficha que come no es "vacia"
        if ficha_comida != None and ficha_comida != "vacia" and pieza_select_main != "vacia":
            exec(f"{ficha_comida}.kill()")
            exec(f"piezas_group.remove({ficha_comida}_group)")
            

            
            
            
            
        
    pygame.display.flip()
    #Meter la imagen background en la ventana screen
    screen.blit(background, (0,0))

    #Ficha comida


    #Pintamos el grupo
    tablero_group.draw(screen)
    piezas_group.draw(screen)
    
    if turno_w:screen.blit(text_turno_w, dest=(0,0))
    else:screen.blit(text_turno_b, dest=(0,0))
    
    if win and ficha_comida=="king_b":screen.blit(text_win_w, (screen_width/2,screen_height/2))
    elif win and ficha_comida == "king_w":screen.blit(text_win_b, (screen_width/2,screen_height/2))

    #Mover fichas seleccionadas
    try:pieza_select_class.update(pygame.mouse.get_pos())
    except:pass

    clock.tick(60)
    #print(clock.get_fps())