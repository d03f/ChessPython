from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import pygame, sys
import numpy as np

colors = {"blanco":(255,255,255), "negro":(0,0,0), "gris":(30,30,30), "marron": (122,80,57)}

piezas = ("king1_", "queen1_", "torre1_","torre2_", "alfil1_","alfil2_", "horse1_", "horse2_")
piezas_color = "wb"

piezas_init_position = {
"torre1_w": (100, 100), "horse1_w": (150, 100), "alfil1_w": (200, 100), "queen1_w": (250, 100),
"king1_w": (300, 100), "alfil2_w": (350, 100), "horse2_w": (400, 100), "torre2_w": (450, 100),

"torre1_b": (100, 450), "horse1_b": (150, 450), "alfil1_b": (200, 450), "queen1_b": (250, 450),
"king1_b": (300, 450), "alfil2_b": (350, 450), "horse2_b": (400, 450), "torre2_b": (450, 450)
}

tablero_x = "87654321"
tablero_y = "abcdefgh"

tablero_grid = {}

tablero_cords_x = []
tablero_cords_y = []




fichas_positions = {}



#Valor más proximo a una lista de valores
def closest_value(value, list):
  array = np.asarray(list)
  i = (np.abs(array - value)).argmin()
  return array[i]

def check_for_piece(positions):
    x = 0
    for a in positions:
        cord = tablero_grid[a]
        ficha = fichas_positions[cord]
        if ficha != "vacia":x = 1
    return x == 1
        

#CLASES

class Tablero(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class Piezas():
#Usada a la hora de arrastrar y rellenar huecos
    class Vacia(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images/pieces.png")
            self.rect = self.image.get_rect()
        def move(self, pos):
            pass
        
    class king(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.image.load(f"images/pieces/king_{color}.png")
            self.rect = self.image.get_rect()
        def update(self, pos):
            self.rect.center = pos
        def move(self):
            self.rect.center = pygame.mouse.get_pos()
        
    class queen(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.image.load(f"images/pieces/queen_{color}.png")
            self.rect = self.image.get_rect()
        def update(self, pos):
            self.rect.center = pos
        def move(self):
            self.rect.center = pygame.mouse.get_pos()

    class torre(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.image.load(f"images/pieces/torre_{color}.png")
            self.rect = self.image.get_rect()
        def update(self, pos):
            self.rect.center = pos
        def move(self):
            self.rect.center = pygame.mouse.get_pos()
        
    class alfil(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.image.load(f"images/pieces/alfil_{color}.png")
            self.rect = self.image.get_rect()
        def update(self, pos):
            self.rect.center = pos
        def move(self):
            self.rect.center = pygame.mouse.get_pos()
        
    class horse(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.image.load(f"images/pieces/horse_{color}.png")
            self.rect = self.image.get_rect()
        def update(self, pos):
            self.rect.center = pos
        def move(self):
            self.rect.center = pygame.mouse.get_pos()

    class peon(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.image.load(f"images/pieces/peon_{color}.png")
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

        fichas_positions.update({f"{tablero_y[b]}{tablero_x[a]}":""})



#PIEZAS
piezas_group = piezas_group = pygame.sprite.Group()


#Creacio y posicion piezas
#Listar las piezas
for p in piezas:
    #2 colores por pieza
    for c in piezas_color:
        exec(f"{p}{c} = Piezas.{p[:-2]}('{c}')")
        exec(f"{p}{c}_group = pygame.sprite.Group()")
        exec(f"{p}{c}_group.add({p}{c})")
        exec(f"piezas_group.add({p}{c}_group)")

        
        exec(f"{p}{c}_group.update(({piezas_init_position[f'{p}{c}'][0]}, {piezas_init_position[f'{p}{c}'][1]}))")
        ficha_cord = tablero_cords_x

        print(fichas_positions.update({piezas_init_position[f"{p}{c}"]:f"{p}{c}"}))





#Ultima class
#VACIA
#Esta class la vamos a utilizar a la hora de arrastrar y rellenar huecos
vacia = Piezas.Vacia()
vacia_group = pygame.sprite.Group()
vacia_group.add(vacia)


pieza_select_class = vacia


#print(tablero_grid)




#Poner vacias en todas las casillas fin ficha
for i in tablero_grid:
    if fichas_positions[tablero_grid[i]] == "":
        fichas_positions.update({tablero_grid[i]:"vacia"})

#Test
print(fichas_positions)

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
            pieza_select = fichas_positions[tablero_grid[(closest_x_up, closest_y_up)]]
            
            print(turno_w)

            #Guardar el grupo en el que la ficha este seleccionada
            exec(f'pieza_select_class = {pieza_select}_group')
            
            
        
        elif event.type == pygame.MOUSEBUTTONUP:
            #Poner la casilla anterior en vacia
            fichas_positions.update({tablero_grid[(closest_x_up, closest_y_up)]:"vacia"})
            #Volver a poner en el mouse a Vacia
            pieza_select_class = vacia_group
            closest_x_down = closest_value(event.pos[0], tablero_cords_x)
            closest_y_down = closest_value(event.pos[1], tablero_cords_y)

            mov_x = closest_x_up - closest_x_down
            mov_y = closest_y_up - closest_y_down

      
            
            
            
        
    pygame.display.flip()
    #Meter la imagen background en la ventana screen
    screen.blit(background, (0,0))

    #Ficha comida


    #Pintamos el grupo
    tablero_group.draw(screen)
    piezas_group.draw(screen)

    #Mover fichas seleccionadas
    try:pieza_select_class.update(pygame.mouse.get_pos())
    except:pass

    #print(clock.get_fps())