from math import *
from kandinsky import *
from time import sleep
from ion import *

HEIGHT = 222
WIDTH = 320
PI = 3.141592653589
STEP = 0.2

#! CORRECTION DES TEXTURES INVERSEE
#! BETTER CODE ARRANGEMENT

distance = lambda x1, y1, x2, y2: sqrt((x1 - x2)**2 + (y1 - y2)**2)

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class Texture():
    def __init__(s, size, content):
        s.size = size
        s.RGB = [[(161,20,29),(160,20,29),(157,23,32),(136,31,38),(156,106,109),(255,251,251),(255,253,253),(255,255,255),(255,255,255),(255,253,253),(255,249,251),(255,229,232),(176,69,75),(157,23,32),(160,20,29),(161,20,29)],
                [(160,20,29),(155,24,32),(143,28,35),(166,84,88),(255,243,244),(255,251,251),(255,254,253),(255,254,255),(255,253,253),(255,251,251),(255,243,244),(156,81,86),(143,28,35),(157,23,32),(160,20,29),(161,20,29)],
                [(157,23,32),(143,28,35),(164,92,96),(255,243,244),(255,250,251),(255,254,253),(255,255,255),(255,254,253),(255,250,251),(255,234,237),(166,84,88),(143,28,35),(155,24,32),(160,20,29),(161,20,29),(161,20,29)],
                [(136,31,38),(158,71,77),(255,243,244),(255,251,251),(255,254,253),(255,254,255),(255,254,253),(255,250,251),(255,243,244),(156,81,86),(143,28,35),(157,23,32),(160,20,29),(160,20,29),(155,24,32),(152,25,34)],
                [(146,94,98),(255,242,246),(255,251,251),(255,254,253),(255,254,255),(255,254,253),(255,251,251),(255,243,244),(166,84,88),(143,28,35),(155,24,32),(160,20,29),(161,20,29),(155,24,32),(140,29,36),(197,93,100)],
                [(255,250,251),(255,251,251),(255,254,253),(255,254,255),(255,254,253),(255,249,251),(255,243,244),(162,90,94),(143,28,35),(157,23,32),(160,20,29),(160,20,29),(155,24,32),(143,28,35),(151,66,73),(255,229,232)],
                [(255,253,253),(255,254,253),(255,254,255),(255,254,253),(255,251,251),(255,242,246),(174,92,98),(143,28,35),(155,24,32),(160,20,29),(161,20,29),(157,23,32),(143,28,35),(166,84,88),(255,234,237),(255,249,251)],
                [(255,255,255),(255,254,255),(255,254,253),(255,249,251),(255,242,246),(164,92,96),(143,28,35),(157,23,32),(160,20,29),(160,20,29),(155,24,32),(143,28,35),(151,66,73),(255,234,237),(255,249,251),(255,254,255)],
                [(255,255,255),(255,254,253),(255,251,251),(255,243,244),(174,92,98),(143,28,35),(155,24,32),(160,20,29),(160,20,29),(155,24,32),(143,28,35),(166,84,88),(255,234,237),(255,249,251),(255,253,253),(255,255,255)],
                [(255,253,253),(255,250,251),(255,243,244),(172,101,107),(143,28,35),(157,23,32),(160,20,29),(160,20,29),(155,24,32),(143,28,35),(158,71,77),(255,229,232),(255,249,251),(255,255,255),(255,255,255),(255,255,255)],
                [(255,249,251),(255,242,246),(180,98,104),(140,29,36),(152,25,34),(160,20,29),(161,20,29),(157,23,32),(143,28,35),(158,71,77),(255,234,237),(255,249,251),(255,253,253),(255,255,255),(255,255,255),(255,255,255)],
                [(255,234,237),(172,101,107),(140,29,36),(157,23,32),(160,20,29),(160,20,29),(157,23,32),(143,28,35),(158,71,77),(255,229,232),(255,249,251),(255,254,255),(255,255,255),(255,253,253),(255,250,251),(255,249,251)],
                [(207,106,112),(140,29,36),(152,25,34),(160,20,29),(161,20,29),(157,23,32),(144,27,35),(144,55,61),(255,234,237),(255,249,251),(255,253,253),(255,255,255),(255,255,255),(255,250,251),(255,234,237),(163,101,106)],
                [(155,24,32),(157,23,32),(160,20,29),(160,20,29),(157,23,32),(144,27,35),(158,71,77),(255,229,232),(255,249,251),(255,254,255),(255,255,255),(255,253,253),(255,250,251),(255,243,244),(180,98,104),(136,31,38)],
                [(157,23,32),(160,20,29),(161,20,29),(157,23,32),(144,27,35),(144,55,61),(255,229,232),(255,249,251),(255,253,253),(255,255,255),(255,255,255),(255,250,251),(255,242,246),(180,98,104),(140,29,36),(152,25,34)],
                [(160,20,29),(160,20,29),(161,20,29),(155,24,32),(176,69,75),(255,222,226),(255,249,251),(255,254,255),(255,255,255),(255,255,255),(255,255,255),(255,249,251),(163,101,106),(136,31,38),(152,25,34),(161,20,29)]]

    def load(s, content):
        '''Chargement des textures'''
        for _ in range(s.size):
            col = []
            for x in range(s.size):
                a = content[x].split(',')
                col.append((int(a[0]),int(a[1]),int(a[2])))
            s.RGB.append(col)
    
    #! A TRAVAILLER
    def resize(s, new_size, x):
        '''Redimension de l'image'''
        scale = ceil(new_size/s.size)
        if new_size < s.size: return [(10,10,10) for _ in range(new_size)]
        if s.size * scale > HEIGHT: scale = HEIGHT/s.size
        resized_line = []
        for i in s.RGB[x]:
            for _ in range(scale):
                resized_line.append(i)
        return resized_line
    #! A TRAVAILLER

class Engine():
    def __init__(s, map):
        s.FOV = 60
        s.RAYCAST_PRECIS = 0.02 # Precision du raycasting
        s.map = map
        s.posx, s.posy = 1.1, 1.1
        s.rot = PI/6
        s.res = {}

    def refresh(s):
        '''Rafraichissement de l'écran'''

        fill_rect(0,0,WIDTH,HEIGHT,(100,100,100))

    #! A TRAVAILLER
    def draw(s, dist, screen_x, offset_x, texture):
        '''Dessine une ligne vertical sur l'écran'''

        h = HEIGHT/dist # Calcul de la hauteur de la ligne

        # Coordonné y du début de ligne
        line_start = (HEIGHT-h)//2
        if line_start < 0: line_start = 0
        # Coordonné y de fin de ligne
        line_end = (HEIGHT-h)//2+int(h)
        if line_end > HEIGHT: line_end = HEIGHT

        # Effet d'ombre
        shade = 1 # Aucune ombre

        n = 0
        text = texture.resize(h, offset_x)
        for w in range(line_start, line_end):
            n += 1
            set_pixel(int(screen_x), int(w), (text[n][0]*shade, text[n][1]*shade, text[n][2]*shade))
    #! A TRAVAILLER

    def draw_ray(s, rot):
        '''Calcul d'un rayon'''

        ray_x, ray_y = s.posx, s.posy # Position de départ du rayon
        prev_x = s.posx
        new_y, new_x = s.RAYCAST_PRECIS*sin(rot), s.RAYCAST_PRECIS*cos(rot)

        # Incrémentation de la position du rayon dans sa direction
        while True:
            ray_x, ray_y = ray_x+new_x, ray_y+new_y
            if s.map[int(ray_x)][int(ray_y)] != 0:
                # Calcul de la longueur du rayon s'il touche un mur
                dist = distance(s.posx, s.posy, ray_x, ray_y) * cos(rot - s.rot - radians(s.FOV/2))
                texture = s.res[str(s.map[int(ray_x)][int(ray_y)])] # Obtension de la texture du mur touché
                break
            else: prev_x = int(ray_x)
        
        # Axe sur lequel le rayon touche le mur
        if abs(int(ray_x) - prev_x) == 1: side = 1 # Mur touché sur l'axe x
        else: side = 0 # Mur touché sur l'axe y
        
        return dist, side, texture, ray_x, ray_y

    def canMove(s, back=False):
        '''Vérifie si le joueur peut avancer ou reculer'''

        if not back: mid = radians(s.FOV/2)
        else: mid = radians(s.FOV/2 + 180)

        rot_mid = s.rot+radians(mid)
        dist, *_ = s.draw_ray(rot_mid)
        if dist > 4*STEP: return True
        else: return False

    def render(s):
        '''Génère le rendu 3D'''

        # Boucle de calcul de chaque rayon
        for i in range(WIDTH):
            rot_i = s.rot + radians(i*s.FOV/WIDTH)

            # Calcul du rayon
            dist, side, wall_text, ray_x, ray_y = s.draw_ray(rot_i)

            # Calcul de la colonne de la texture que touche le rayon
            if side == 0: offset_x = ray_x
            else: offset_x = ray_y
            offset_x = (offset_x - floor(offset_x)) * wall_text.size

            s.draw(dist, i, int(offset_x), wall_text)

###!   DEFAULT   !###
wall_t = Texture(16, "")
###!   DEFAULT   !###

game = Engine(map)
game.res['1'] = wall_t
while True:
    game.refresh()
    game.render()
    if keydown(KEY_LEFT):
        game.rot -= PI/12
    elif keydown(KEY_RIGHT):
        game.rot += PI/12
    elif keydown(KEY_UP):
        nx, ny = STEP*cos(game.rot+radians(game.FOV/2)), STEP*sin(game.rot+radians(game.FOV/2))
        if game.canMove():
            game.posx += nx; game.posy += ny
    elif keydown(KEY_DOWN):
        nx, ny = -STEP*cos(game.rot+radians(game.FOV/2)), -STEP*sin(game.rot+radians(game.FOV/2))
        if game.canMove(True):
            game.posx += nx; game.posy += ny