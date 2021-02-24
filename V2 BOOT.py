import pygame
import time
pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)
green = (0, 255, 0)
bluee = (0, 0, 128)
black = (0, 0, 0)




def imgdisplay(type, x, y):
    win.blit(type, (x, y))
    pygame.display.update()

def imagedisplaytransform(type, x, y, width, height):
    win.blit(pygame.transform.scale(type, (width, height)), (x, y))
    pygame.display.update()


# SOUNDS
clicksound = pygame.mixer.Sound('click.wav')
boom = pygame.mixer.Sound('flash1.wav')
splash = pygame.mixer.Sound('splash.wav')
beep1 = pygame.mixer.Sound('beep-3.wav')
beep2 = pygame.mixer.Sound('sound80.wav')

music = pygame.mixer.music.load('das boot.mp3')
pygame.mixer.music.play(-1)

matrix1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# button
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, black)
            #centrowanie
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #pos to pozycja myszy
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False





win = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
pygame.display.set_caption('DAS BOOT!')
clock= pygame.time.Clock()
run = True
fullscreen = True
b1 = pygame.image.load('1b.png')
b2 = pygame.image.load('2b.png')
b3 = pygame.image.load('3b.png')
b4 = pygame.image.load('4b.png')
r1 = pygame.image.load('1r.png')
r2 = pygame.image.load('2r.png')
r3 = pygame.image.load('3r.png')
r4 = pygame.image.load('4r.png')
pic = pygame.image.load("bgship.jpg")
blue = pygame.image.load('blue.png')
red = pygame.image.load('red.png')
greencross = pygame.image.load('greencross.png')
blackcross = pygame.image.load('blackcross.png')
crosshair = pygame.image.load('crosshair.png')
bluewin = pygame.image.load('bluewin.png')
redwin = pygame.image.load('redwin.png')
dasboot = pygame.image.load('dasboot.png')
win.blit(pygame.transform.scale(pic, (1366, 768)), (0, 0))
pygame.display.flip()


def blueboard():
    win.blit(pygame.transform.scale(pic, (1366, 768)), (0, 0))
    win.blit(pygame.transform.scale(blue, (1450, 800)), (0, 0))
    pygame.display.flip()


def matrixset():
    global matrix1
    global matrix2
    #BLUE
    if boatcounter == 1:
        matrix1[updown*10 + rightleft] = 4
        matrix1[updown*10 + 10 + rightleft] = 4
        matrix1[updown * 10 + 20 + rightleft] = 4
        matrix1[updown * 10 + 30 + rightleft] = 4
    if boatcounter == 2:
        matrix1[updown * 10 + rightleft] = 3
        matrix1[updown * 10 + 10 + rightleft] = 3
        matrix1[updown * 10 + 20 + rightleft] = 3
    if boatcounter == 3:
        matrix1[updown * 10 + rightleft] = 2
        matrix1[updown * 10 + 10 + rightleft] = 2
    if boatcounter == 4:
        matrix1[updown * 10 + rightleft] = 1

    #RED
    if boatcounter == 5:
        matrix2[updown * 10 + rightleft] = 4
        matrix2[updown * 10 + 10 + rightleft] = 4
        matrix2[updown * 10 + 20 + rightleft] = 4
        matrix2[updown * 10 + 30 + rightleft] = 4
    if boatcounter == 6:
        matrix2[updown * 10 + rightleft] = 3
        matrix2[updown * 10 + 10 + rightleft] = 3
        matrix2[updown * 10 + 20 + rightleft] = 3
    if boatcounter == 7:
        matrix2[updown * 10 + rightleft] = 2
        matrix2[updown * 10 + 10 + rightleft] = 2
    if boatcounter == 8:
        matrix2[updown * 10 + rightleft] = 1


def redboard():
    win.blit(pygame.transform.scale(pic, (1366, 768)), (0, 0))
    win.blit(pygame.transform.scale(red, (1450, 800)), (0, 0))
    pygame.display.flip()

def crosses():

    global whosturn
    if whosturn == blue:
        for v in range(0, len(crosseslist), 2):
            imagedisplaytransform(greencross, crosseslist[v], crosseslist[v + 1], 60, 60)
        for v in range(0, len(crosseslist3), 2):
            imagedisplaytransform(blackcross, crosseslist3[v], crosseslist3[v + 1], 60, 60)
    if whosturn == red:
        for v in range(0, len(crosseslist2), 2):
            imagedisplaytransform(greencross, crosseslist2[v], crosseslist2[v + 1], 60, 60)
        for v in range(0, len(crosseslist4), 2):
            imagedisplaytransform(blackcross, crosseslist4[v], crosseslist4[v + 1], 60, 60)


#STARTING PLACE OF SHIPS
b4x = 168; b4y = 80; b3x = 166; b3y = 80; b2x = 166; b2y = 80; b1x = 166; b1y = 80; r4x = 168; r4y = 80; r3x = 166; r3y = 80; r2x = 166; r2y = 80; r1x = 166; r1y = 80
crossx = 165
crossy = 80
#MOVING RIGHT-----------------
def moveboatR():
    global b4x
    global b4y
    global b3x
    global b3y
    global b2y
    global b2x
    global b1x
    global b1y
    global r4x
    global r4y
    global r3x
    global r3y
    global r2y
    global r2x
    global r1x
    global r1y
    global boatcounter

    #BLUE
    if boatcounter == 1:
        b4x = b4x + 116
        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 2:
        b3x = b3x + 116
        blueboard()
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 3:
        b2x = b2x + 116
        blueboard()
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 4:
        b1x = b1x + 116
        blueboard()
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    #RED
    if boatcounter == 5:
        r4x = r4x + 116
        redboard()
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 6:
        r3x = r3x + 116
        redboard()
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 7:
        r2x = r2x + 116
        redboard()
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 8:
        r1x = r1x + 116
        redboard()
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()

#MOVING LEFT------------------
def moveboatL():
    global b4x
    global b4y
    global b3x
    global b3y
    global b2y
    global b2x
    global b1x
    global b1y
    global r4x
    global r4y
    global r3x
    global r3y
    global r2y
    global r2x
    global r1x
    global r1y
    global boatcounter


    if boatcounter == 1:
        b4x = b4x - 116
        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 2:
        b3x = b3x - 116
        blueboard()
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 3:
        b2x = b2x - 116
        blueboard()
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 4:
        b1x = b1x - 116
        blueboard()
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    # RED
    if boatcounter == 5:
        r4x = r4x - 116
        redboard()
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 6:
        r3x = r3x - 116
        redboard()
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 7:
        r2x = r2x - 116
        redboard()
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 8:
        r1x = r1x - 116
        redboard()
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()

#MOVING DOWN-------------------
def moveboatD():
    global b4x
    global b4y
    global b3x
    global b3y
    global b2y
    global b2x
    global b1x
    global b1y
    global r4x
    global r4y
    global r3x
    global r3y
    global r2y
    global r2x
    global r1x
    global r1y
    global boatcounter

    if boatcounter == 1:
        b4y = b4y + 65
        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 2:
        b3y = b3y + 65
        blueboard()
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 3:
        b2y = b2y + 65
        blueboard()
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 4:
        b1y = b1y + 65
        blueboard()
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    # RED
    if boatcounter == 5:
        r4y = r4y + 65
        redboard()
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 6:
        r3y = r3y + 65
        redboard()
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 7:
        r2y = r2y + 65
        redboard()
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 8:
        r1y = r1y + 65
        redboard()
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()

#MOVING UP--------------------
def moveboatU():
    global b4x
    global b4y
    global b3x
    global b3y
    global b2y
    global b2x
    global b1x
    global b1y
    global r4x
    global r4y
    global r3x
    global r3y
    global r2y
    global r2x
    global r1x
    global r1y
    global boatcounter

    if boatcounter == 1:
        b4y = b4y - 65
        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 2:
        b3y = b3y - 65
        blueboard()
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 3:
        b2y = b2y - 65
        blueboard()
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 4:
        b1y = b1y - 65
        blueboard()
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        pygame.display.flip()
    # RED
    if boatcounter == 5:
        r4y = r4y - 65
        redboard()
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 6:
        r3y = r3y - 65
        redboard()
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 7:
        r2y = r2y - 65
        redboard()
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()
    if boatcounter == 8:
        r1y = r1y - 65
        redboard()
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        pygame.display.flip()

#MOVE CROSSHIAR-------
def movecrosshairR():
    if whosturn == blue:
        blueboard()
    elif whosturn == red:
        redboard()

    global crossx
    global crossy
    crossx = crossx + 116
    imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
def movecrosshairL():
        if whosturn == blue:
            blueboard()
        elif whosturn == red:
            redboard()
        global crossx
        global crossy
        crossx = crossx - 116
        imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
def movecrosshairU():
    if whosturn == blue:
        blueboard()
    elif whosturn == red:
        redboard()
    global crossx
    global crossy
    crossy = crossy - 65
    imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
def movecrosshairD():
    if whosturn == blue:
        blueboard()
    elif whosturn == red:
        redboard()
    global crossx
    global crossy
    crossy = crossy + 65
    imagedisplaytransform(crosshair, crossx, crossy, 60, 60)

def hit():
    global whosturn
    global updown2
    global rightleft2
    global crossx
    global crossy

    if whosturn == blue:
        print('strzal niebieskiego: ', matrix2[updown2 * 10 + rightleft2])
        if matrix2[updown2*10 + rightleft2] != 0:
            matrix2[updown2*10 + rightleft2] = 0
            boom.play()
            crosseslist.append(crossx)
            crosseslist.append(crossy)

        elif matrix2[updown2*10 + rightleft2] == 0:
            splash.play()
            whosturn = red
            crosseslist3.append(crossx)
            crosseslist3.append(crossy)
            crossx = 165
            crossy = 80
            imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
            rightleft2 = 0
            updown2 = 0
            redboard()
            imagedisplaytransform(crosshair, crossx, crossy, 60, 60)

    elif whosturn == red:
        print('strzal czerwonego: ', matrix1[updown2 * 10 + rightleft2])
        if matrix1[updown2 * 10 + rightleft2] != 0:
            matrix1[updown2 * 10 + rightleft2] = 0
            boom.play()
            crosseslist2.append(crossx)
            crosseslist2.append(crossy)

        elif matrix1[updown2 * 10 + rightleft2] == 0:
            splash.play()
            whosturn = blue
            crosseslist4.append(crossx)
            crosseslist4.append(crossy)
            crossx = 165
            crossy = 80
            imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
            rightleft2 = 0
            updown2 = 0
            blueboard()
            imagedisplaytransform(crosshair, crossx, crossy, 60, 60)

imagedisplaytransform(dasboot, -40, 90, 800, 310)

space = 1
boatcounter = 1
whosturn = blue
rightleft = 0
updown = 0
rightleft2 = 0
updown2 = 0
crosseslist = []
crosseslist2 = []
crosseslist3 = []
crosseslist4 = []
x = 1

### MAIN LOOP ###
while run:
    clock.tick(25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_F9]:
        if fullscreen == False:
            win = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
            fullscreen = True
        elif fullscreen == True:
                win = pygame.display.set_mode((1366, 768), pygame.RESIZABLE)
                fullscreen = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()


#BLUE PLAUER CHOOSING
    if keys[pygame.K_SPACE] and space == 1:

        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        space = 0

#MOVING RIGHT
    if event.type == pygame.KEYDOWN and boatcounter == 1:
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        if event.key == pygame.K_RIGHT and rightleft < 9:
             moveboatR()
             rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN :
            matrixset()
            boatcounter = boatcounter + 1
            rightleft = 0
            updown = 0
            beep2.play()
            pygame.time.wait(100)


    if event.type == pygame.KEYDOWN and boatcounter == 2:
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        if event.key == pygame.K_RIGHT and rightleft < 9:
             moveboatR()
             rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 3:
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        if event.key == pygame.K_RIGHT and rightleft < 9:
             moveboatR()
             rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 4:
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        if event.key == pygame.K_RIGHT and rightleft < 9:
             moveboatR()
             rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

#MOVING LEFT
    if event.type == pygame.KEYDOWN and boatcounter == 1:
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        if event.key == pygame.K_LEFT and rightleft > 0:
                moveboatL()
                rightleft = rightleft -1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 2:
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        if event.key == pygame.K_LEFT and rightleft > 0:
                moveboatL()
                rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 3:
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        if event.key == pygame.K_LEFT and rightleft > 0:
                moveboatL()
                rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 4:
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        if event.key == pygame.K_LEFT and rightleft > 0:
                moveboatL()
                rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)

#MOVING DOWN
    if event.type == pygame.KEYDOWN and boatcounter == 1:
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        if event.key == pygame.K_DOWN and updown < 6:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 2:
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        if event.key == pygame.K_DOWN and updown < 7:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 3:
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        if event.key == pygame.K_DOWN and updown < 8:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 4:
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        if event.key == pygame.K_DOWN and updown < 9:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

#MOVING UP
    if event.type == pygame.KEYDOWN and boatcounter == 1:
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
            #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 2:
        imagedisplaytransform(b3, b3x, b3y, 60, 200)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 3:
        imagedisplaytransform(b2, b2x, b2y, 60, 110)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 4:
        imagedisplaytransform(b1, b1x, b1y, 60, 60)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)




#RED PLAYEr CHOOSING
    if boatcounter == 5 and x ==1:
        redboard()
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        x = 0

#MOVING RIGHT RED
    if event.type == pygame.KEYDOWN and boatcounter == 5:
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        if event.key == pygame.K_RIGHT and rightleft < 9:
            moveboatR()
            rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 6:
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        if event.key == pygame.K_RIGHT and rightleft < 9:
            moveboatR()
            rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 7:
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        if event.key == pygame.K_RIGHT and rightleft < 9:
            moveboatR()
            rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 8:
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        if event.key == pygame.K_RIGHT and rightleft < 9:
            moveboatR()
            rightleft = rightleft + 1
        #beep1.play()
        pygame.time.wait(100)


#MOVING LEFT red
    if event.type == pygame.KEYDOWN and boatcounter == 5:
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        if event.key == pygame.K_LEFT and rightleft > 0:
            moveboatL()
            rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 6:
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        if event.key == pygame.K_LEFT and rightleft > 0:
            moveboatL()
            rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 7:
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        if event.key == pygame.K_LEFT and rightleft > 0:
            moveboatL()
            rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 8:
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        if event.key == pygame.K_LEFT and rightleft > 0:
            moveboatL()
            rightleft = rightleft - 1
        #beep1.play()
        pygame.time.wait(100)


#MOVING DOWN red
    if event.type == pygame.KEYDOWN and boatcounter == 5:
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        if event.key == pygame.K_DOWN and updown < 6:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 6:
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        if event.key == pygame.K_DOWN and updown < 7:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 7:
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        if event.key == pygame.K_DOWN and updown < 8:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 8:
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        if event.key == pygame.K_DOWN and updown < 9:
            moveboatD()
            updown = updown + 1
        #beep1.play()
        pygame.time.wait(100)


#MOVING UP red
    if event.type == pygame.KEYDOWN and boatcounter == 5:
        imagedisplaytransform(r4, r4x, r4y, 60, 250)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 6:
        imagedisplaytransform(r3, r3x, r3y, 60, 200)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 7:
        imagedisplaytransform(r2, r2x, r2y, 60, 110)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)

    if event.type == pygame.KEYDOWN and boatcounter == 8:
        imagedisplaytransform(r1, r1x, r1y, 60, 60)
        if event.key == pygame.K_UP and updown > 0:
            moveboatU()
            updown = updown - 1
        #beep1.play()
        pygame.time.wait(100)



    # zmiana mapy po ustawieniu statkow
    if whosturn == blue and boatcounter == 9:
        blueboard()
        imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
        crosses()
    if whosturn == red and boatcounter == 9:
        redboard()
        imagedisplaytransform(crosshair, crossx, crossy, 60, 60)
        crosses()

      #celownik w prawo
    if event.type == pygame.KEYDOWN and boatcounter > 8:
        if event.key == pygame.K_RIGHT and rightleft2 < 9:
            movecrosshairR()
            rightleft2 = rightleft2 + 1
            crosses()
            pygame.time.wait(100)
    #celownik w lewo
    if event.type == pygame.KEYDOWN and boatcounter > 8:
        if event.key == pygame.K_LEFT and rightleft2 > 0:
            movecrosshairL()
            rightleft2 = rightleft2 - 1
            crosses()
            pygame.time.wait(100)
    #celownik w dol
    if event.type == pygame.KEYDOWN and boatcounter > 8:
        if event.key == pygame.K_DOWN and updown2 < 9:
            movecrosshairD()
            updown2 = updown2 + 1
            crosses()
            pygame.time.wait(100)
    #celownik w gore
    if event.type == pygame.KEYDOWN and boatcounter > 8:
        if event.key == pygame.K_UP and updown2 > 0:
            movecrosshairU()
            updown2 = updown2 - 1
            crosses()
            pygame.time.wait(100)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and boatcounter > 9:
            print('RIGHTLEFT: ', rightleft2)
            print('UPDOWN: ', updown2)
            hit()
            crosses()

            pygame.time.wait(200)



    #jesli wszystkie statki zestrzelone to restart
    if all(values == 0 for values in matrix1) and boatcounter > 8:
        print('RED WON')
        imagedisplaytransform(redwin, 539, 234, 290, 300)
        pygame.time.wait(3000)
        matrix2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        space = 1
        boatcounter = 1
        whosturn = blue
        rightleft = 0
        updown = 0
        rightleft2 = 0
        updown2 = 0
        b4x = 168;
        b4y = 80;
        b3x = 166;
        b3y = 80;
        b2x = 166;
        b2y = 80;
        b1x = 166;
        b1y = 80;
        r4x = 168;
        r4y = 80;
        r3x = 166;
        r3y = 80;
        r2x = 166;
        r2y = 80;
        r1x = 166;
        r1y = 80
        crossx = 165
        crossy = 80
        crosseslist = []
        crosseslist2 = []
        crosseslist3 = []
        crosseslist4 = []
        x = 1

    elif all(values == 0 for values in matrix2) and boatcounter > 8:
        print('BLUE WON')
        imagedisplaytransform(bluewin, 539, 234, 290, 300)
        pygame.time.wait(3000)
        matrix1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        blueboard()
        imagedisplaytransform(b4, b4x, b4y, 60, 250)
        space = 1
        boatcounter = 1
        whosturn = blue
        rightleft = 0
        updown = 0
        rightleft2 = 0
        updown2 = 0
        b4x = 168;
        b4y = 80;
        b3x = 166;
        b3y = 80;
        b2x = 166;
        b2y = 80;
        b1x = 166;
        b1y = 80;
        r4x = 168;
        r4y = 80;
        r3x = 166;
        r3y = 80;
        r2x = 166;
        r2y = 80;
        r1x = 166;
        r1y = 80
        crossx = 165
        crossy = 80
        crosseslist = []
        crosseslist2 = []
        crosseslist3 = []
        crosseslist4 = []
        x = 1

    #GAME RESET?
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:

            matrix2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            matrix1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            blueboard()
            imagedisplaytransform(b4, 168, 80, 60, 250)
            space = 1
            boatcounter = 1
            whosturn = blue
            rightleft = 0
            updown = 0
            rightleft2 = 0
            updown2 = 0
            b4x = 168;
            b4y = 80;
            b3x = 166;
            b3y = 80;
            b2x = 166;
            b2y = 80;
            b1x = 166;
            b1y = 80;
            r4x = 168;
            r4y = 80;
            r3x = 166;
            r3y = 80;
            r2x = 166;
            r2y = 80;
            r1x = 166;
            r1y = 80
            crossx = 165
            crossy = 80
            crosseslist = []
            crosseslist2 = []
            crosseslist3 = []
            crosseslist4 = []
            x = 1
pygame.quit()
