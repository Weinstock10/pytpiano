import math
import random
import pygame
import os
import time

class whitekey(object):
    def __init__(self, name, pos, sample, color = (255, 255, 255)):
        self.name = name
        self.color = color
        self.pos = pos
        self.sample = sample
        
    def draw(self, surface, eyes = False):
        pygame.draw.rect(surface, self.color, self.pos)
        
    def getnote(self):
        return self.sample
    
    def getpos(self):
        return self.pos
        
        
class blackkey(object):
    def __init__(self, name, pos, sample, color = (0, 0, 0)):
        self.name = name
        self.color = color
        self.pos = pos
        self.sample = sample
        
    def draw(self, surface, eyes = False):
        pygame.draw.rect(surface, self.color, self.pos)
        
    def getnote(self):
        return self.sample
        
    def getpos(self):
        return self.pos



class keys(object):
    def __init__(self):
        self.keyboard = []
        
    def addkey(self, key):
        self.keyboard.append(key)
#        print(self)
        
    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            yellow =  [False for i in range(18)]
            if event.type == pygame.KEYDOWN:
                keypress = pygame.key.get_pressed()
                for pressed in keypress:
                    if keypress[pygame.K_a]:
#                        print(str(C4.getnote()) + "\n")
                        yellow[0] = True
                        redrawWindow(window, yellow)
                        os.system(str(C4.getnote()))
                        break
                    elif keypress[pygame.K_w]:
#                        print(str(Dfl4.getnote()) + "\n")
                        yellow[1] = True
                        redrawWindow(window, yellow)
                        os.system(str(Dfl4.getnote()))
                        break
                    elif keypress[pygame.K_s]:
#                        print(str(D4.getnote()) + "\n")
                        yellow[2] = True
                        redrawWindow(window, yellow)
                        os.system(str(D4.getnote()))
                        break
                    elif keypress[pygame.K_e]:
#                        print(str(Efl4.getnote()) + "\n")
                        yellow[3] = True
                        redrawWindow(window, yellow)
                        os.system(str(Efl4.getnote()))
                        break
                    elif keypress[pygame.K_d]:
#                        print(str(E4.getnote()) + "\n")
                        yellow[4] = True
                        redrawWindow(window, yellow)
                        os.system(str(E4.getnote()))
                        break
                    elif keypress[pygame.K_f]:
#                        print(str(F4.getnote()) + "\n")
                        yellow[5] = True
                        redrawWindow(window, yellow)
                        os.system(str(F4.getnote()))
                        break
                    elif keypress[pygame.K_g]:
#                        print(str(G4.getnote()) + "\n")
                        yellow[6] = True
                        redrawWindow(window, yellow)
                        os.system(str(G4.getnote()))
                        break
                    elif keypress[pygame.K_t]:
#                        print(str(Gfl4.getnote()) + "\n")
                        yellow[7] = True
                        redrawWindow(window, yellow)
                        os.system(str(Gfl4.getnote()))
                        break
                    elif keypress[pygame.K_h]:
#                        print(str(A5.getnote()) + "\n")
                        yellow[8] = True
                        redrawWindow(window, yellow)
                        os.system(str(A5.getnote()))
                        break
                    elif keypress[pygame.K_y]:
#                        print(str(Afl5.getnote()) + "\n")
                        yellow[9] = True
                        redrawWindow(window, yellow)
                        os.system(str(Afl5.getnote()))
                        break
                    elif keypress[pygame.K_j]:
#                        print(str(B5.getnote()) + "\n")
                        yellow[10] = True
                        redrawWindow(window, yellow)
                        os.system(str(B5.getnote()))
                        break
                    elif keypress[pygame.K_u]:
#                        print(str(Bfl5.getnote()) + "\n")
                        yellow[11] = True
                        redrawWindow(window, yellow)
                        os.system(str(Bfl5.getnote()))
                        break
                    elif keypress[pygame.K_k]:
#                        print(str(C5.getnote()) + "\n")
                        yellow[12] = True
                        redrawWindow(window, yellow)
                        os.system(str(C5.getnote()))
                        break
                    elif keypress[pygame.K_l]:
#                        print(str(D5.getnote()) + "\n")
                        yellow[13] = True
                        redrawWindow(window, yellow)
                        os.system(str(D5.getnote()))
                        break
                    elif keypress[pygame.K_o]:
#                        print(str(Dfl5.getnote()) + "\n")
                        yellow[14] = True
                        redrawWindow(window, yellow)
                        os.system(str(Dfl5.getnote()))
                        break
                    elif keypress[pygame.K_SEMICOLON]:
#                        print(str(E5.getnote()) + "\n")
                        yellow[15] = True
                        redrawWindow(window, yellow)
                        os.system(str(E5.getnote()))
                        break
                    elif keypress[pygame.K_p]:
#                        print(str(Efl5.getnote()) + "\n")
                        yellow[16] = True
                        redrawWindow(window, yellow)
                        os.system(str(Efl5.getnote()))
                        break
                    elif keypress[pygame.K_QUOTE]:
#                        print(str(F5.getnote()) + "\n")
                        yellow[17] = True
                        redrawWindow(window, yellow)
                        os.system(str(F5.getnote()))
                        break
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    C4Rec = C4.getpos()
                    C4Rec = pygame.Rect(C4Rec)
                    D4Rec = D4.getpos()
                    D4Rec = pygame.Rect(D4Rec)
                    E4Rec = E4.getpos()
                    E4Rec = pygame.Rect(E4Rec)
                    F4Rec = F4.getpos()
                    F4Rec = pygame.Rect(F4Rec)
                    G4Rec = G4.getpos()
                    G4Rec = pygame.Rect(G4Rec)
                    A5Rec = A5.getpos()
                    A5Rec = pygame.Rect(A5Rec)
                    B5Rec = B5.getpos()
                    B5Rec = pygame.Rect(B5Rec)
                    C5Rec = C5.getpos()
                    C5Rec = pygame.Rect(C5Rec)
                    D5Rec = D5.getpos()
                    D5Rec = pygame.Rect(D5Rec)
                    E5Rec = E5.getpos()
                    E5Rec = pygame.Rect(E5Rec)
                    F5Rec = F5.getpos()
                    F5Rec = pygame.Rect(F5Rec)
                    Dfl4Rec = Dfl4.getpos()
                    Dfl4Rec = pygame.Rect(Dfl4Rec)
                    Efl4Rec = Efl4.getpos()
                    Efl4Rec = pygame.Rect(Efl4Rec)
                    Gfl4Rec = Gfl4.getpos()
                    Gfl4Rec = pygame.Rect(Gfl4Rec)
                    Afl5Rec = Afl5.getpos()
                    Afl5Rec = pygame.Rect(Afl5Rec)
                    Bfl5Rec = Bfl5.getpos()
                    Bfl5Rec = pygame.Rect(Bfl5Rec)
                    Dfl5Rec = Dfl5.getpos()
                    Dfl5Rec = pygame.Rect(Dfl5Rec)
                    Efl5Rec = Efl5.getpos()
                    Efl5Rec = pygame.Rect(Efl5Rec)

                    y = pygame.mouse.get_pos()
                    if Dfl4Rec.collidepoint(y):
                        yellow[1] = True
                        redrawWindow(window, yellow)
                        os.system(str(Dfl4.getnote()))
#                        print("Dfl4 Pressed")
                    elif Efl4Rec.collidepoint(y):
                        yellow[3] = True
                        redrawWindow(window, yellow)
                        os.system(str(Efl4.getnote()))
#                        print("Efl4 Pressed")
                    elif Gfl4Rec.collidepoint(y):
                        yellow[7] = True
                        redrawWindow(window, yellow)
                        os.system(str(Gfl4.getnote()))
#                        print("Gfl4 Pressed")
                    elif Afl5Rec.collidepoint(y):
                        yellow[9] = True
                        redrawWindow(window, yellow)
                        os.system(str(Afl5.getnote()))
#                        print("Afl5 Pressed")
                    elif Bfl5Rec.collidepoint(y):
                        yellow[11] = True
                        redrawWindow(window, yellow)
                        os.system(str(Bfl5.getnote()))
#                        print("Bfl5 Pressed")
                    elif Dfl5Rec.collidepoint(y):
                        yellow[14] = True
                        redrawWindow(window, yellow)
                        os.system(str(Dfl5.getnote()))
#                        print("Dfl5 Pressed")
                    elif Efl5Rec.collidepoint(y):
                        yellow[16] = True
                        redrawWindow(window, yellow)
                        os.system(str(Efl5.getnote()))
#                        print("Efl5 Pressed")
                    elif C4Rec.collidepoint(y):
                        yellow[0] = True
                        redrawWindow(window, yellow)
                        os.system(str(C4.getnote()))
#                        print("C4 Pressed")
                    elif D4Rec.collidepoint(y):
                        yellow[2] = True
                        redrawWindow(window, yellow)
                        os.system(str(D4.getnote()))
#                        print("D4 Pressed")
                    elif E4Rec.collidepoint(y):
                        yellow[4] = True
                        redrawWindow(window, yellow)
                        os.system(str(E4.getnote()))
#                        print("E4 Pressed")
                    elif F4Rec.collidepoint(y):
                        yellow[5] = True
                        redrawWindow(window, yellow)
                        os.system(str(F4.getnote()))
#                        print("F4 Pressed")
                    elif G4Rec.collidepoint(y):
                        yellow[6] = True
                        redrawWindow(window, yellow)
                        os.system(str(G4.getnote()))
#                        print("G4 Pressed")
                    elif A5Rec.collidepoint(y):
                        yellow[8] = True
                        redrawWindow(window, yellow)
                        os.system(str(A5.getnote()))
#                        print("A5 Pressed")
                    elif B5Rec.collidepoint(y):
                        yellow[10] = True
                        redrawWindow(window, yellow)
                        os.system(str(B5.getnote()))
#                        print("B5 Pressed")
                    elif C5Rec.collidepoint(y):
                        yellow[12] = True
                        redrawWindow(window, yellow)
                        os.system(str(C5.getnote()))
#                        print("C5 Pressed")
                    elif D5Rec.collidepoint(y):
                        yellow[13] = True
                        redrawWindow(window, yellow)
                        os.system(str(D5.getnote()))
#                        print("D5 Pressed")
                    elif E5Rec.collidepoint(y):
                        yellow[15] = True
                        redrawWindow(window, yellow)
                        os.system(str(E5.getnote()))
#                        print("E5 Pressed")
                    elif F5Rec.collidepoint(y):
                        yellow[17] = True
                        redrawWindow(window, yellow)
                        os.system(str(F5.getnote()))
#                        print("F5 Pressed")

    
def redrawWindow(surface, yellow):
    surface.fill((0, 0, 0))
    colorPlay = (255, 0, 0)
    if yellow[0] == True:
        C4Rec = C4.getpos()
        C4Rec = pygame.Rect(C4Rec)
        pygame.draw.rect(surface, colorPlay, C4Rec)
        
    else:
        C4.draw(surface)
        
    if yellow[2] == True:
        D4Rec = D4.getpos()
        D4Rec = pygame.Rect(D4Rec)
        pygame.draw.rect(surface, colorPlay, D4Rec)
        
    else:
        D4.draw(surface)
        
    if yellow[1] == True:
        Dfl4Rec = Dfl4.getpos()
        Dfl4Rec = pygame.Rect(Dfl4Rec)
        pygame.draw.rect(surface, colorPlay, Dfl4Rec)
        
    else:
        Dfl4.draw(surface)
        

    if yellow[4] == True:
        E4Rec = E4.getpos()
        E4Rec = pygame.Rect(E4Rec)
        pygame.draw.rect(surface, colorPlay, E4Rec)
        
    else:
        E4.draw(surface)
        
    if yellow[5] == True:
        F4Rec = F4.getpos()
        F4Rec = pygame.Rect(F4Rec)
        pygame.draw.rect(surface, colorPlay, F4Rec)
        
    else:
        F4.draw(surface)
        
    if yellow[6] == True:
        G4Rec = G4.getpos()
        G4Rec = pygame.Rect(G4Rec)
        pygame.draw.rect(surface, colorPlay, G4Rec)
        
    else:
        G4.draw(surface)
        
    if yellow[8] == True:
        A5Rec = A5.getpos()
        A5Rec = pygame.Rect(A5Rec)
        pygame.draw.rect(surface, colorPlay, A5Rec)
        
    else:
        A5.draw(surface)
        
    if yellow[10] == True:
        B5Rec = B5.getpos()
        B5Rec = pygame.Rect(B5Rec)
        pygame.draw.rect(surface, colorPlay, B5Rec)
        
    else:
        B5.draw(surface)
        
    if yellow[12] == True:
        C5Rec = C5.getpos()
        C5Rec = pygame.Rect(C5Rec)
        pygame.draw.rect(surface, colorPlay, C5Rec)
        
    else:
        C5.draw(surface)
        
    if yellow[13] == True:
        D5Rec = D5.getpos()
        D5Rec = pygame.Rect(D5Rec)
        pygame.draw.rect(surface, colorPlay, D5Rec)
        
    else:
        D5.draw(surface)
        
    if yellow[15] == True:
        E5Rec = E5.getpos()
        E5Rec = pygame.Rect(E5Rec)
        pygame.draw.rect(surface, colorPlay, E5Rec)
        
    else:
        E5.draw(surface)
        
    if yellow[17] == True:
        F5Rec = F5.getpos()
        F5Rec = pygame.Rect(F5Rec)
        pygame.draw.rect(surface, colorPlay, F5Rec)
        
    else:
        F5.draw(surface)
        
    if yellow[3] == True:
        Efl4Rec = Efl4.getpos()
        Efl4Rec = pygame.Rect(Efl4Rec)
        pygame.draw.rect(surface, colorPlay, Efl4Rec)
        
    else:
        Efl4.draw(surface)
        
    if yellow[7] == True:
        Gfl4Rec = Gfl4.getpos()
        Gfl4Rec = pygame.Rect(Gfl4Rec)
        pygame.draw.rect(surface, colorPlay, Gfl4Rec)
        
    else:
        Gfl4.draw(surface)
        
    if yellow[9] == True:
        Afl5Rec = Afl5.getpos()
        Afl5Rec = pygame.Rect(Afl5Rec)
        pygame.draw.rect(surface, colorPlay, Afl5Rec)
        
    else:
        Afl5.draw(surface)
        
    if yellow[11] == True:
        Bfl5Rec = Bfl5.getpos()
        Bfl5Rec = pygame.Rect(Bfl5Rec)
        pygame.draw.rect(surface, colorPlay, Bfl5Rec)
        
    else:
        Bfl5.draw(surface)
        
    if yellow[14] == True:
        Dfl5Rec = Dfl5.getpos()
        Dfl5Rec = pygame.Rect(Dfl5Rec)
        pygame.draw.rect(surface, colorPlay, Dfl5Rec)
        
    else:
        Dfl5.draw(surface)
        
    if yellow[16] == True:
        Efl5Rec = Efl5.getpos()
        Efl5Rec = pygame.Rect(Efl5Rec)
        pygame.draw.rect(surface, colorPlay, Efl5Rec)
        
    else:
        Efl5.draw(surface)
    
    pygame.display.update()

    
def main():
    global width, height, C4, D4, E4, F4, G4, A5, B5, C5, D5, E5, F5, Dfl4, Efl4, Gfl4, Afl5, Bfl5, Dfl5, Efl5, board, yellow, window
    width = 1025
    height = 500
    window = pygame.display.set_mode((width, height))
    flag = True
    yellow =  [False for i in range(19)]
    
    clock = pygame.time.Clock()

    C4 = whitekey("C4", (50, 10, 75, 400), "afplay audio/C4.wav&")
    D4 = whitekey("D4", (135, 10, 75, 400), "afplay audio/D4.wav&")
    E4 = whitekey("E4", (220, 10, 75, 400), "afplay audio/E4.wav&")
    F4 = whitekey("F4", (305, 10, 75, 400), "afplay audio/F4.wav&")
    G4 = whitekey("G4", (390, 10, 75, 400), "afplay audio/G4.wav&")
    A5 = whitekey("A5", (475, 10, 75, 400), "afplay audio/A5.wav&")
    B5 = whitekey("B5", (560, 10, 75, 400), "afplay audio/B5.wav&")
    C5 = whitekey("C5", (645, 10, 75, 400), "afplay audio/C5.wav&")
    D5 = whitekey("D5", (730, 10, 75, 400), "afplay audio/D5.wav&")
    E5 = whitekey("E5", (815, 10, 75, 400), "afplay audio/E5.wav&")
    F5 = whitekey("F5", (900, 10, 75, 400), "afplay audio/F5.wav&")
    
    Dfl4 = blackkey("Dfl4", (105, 10, 50, 300), "afplay audio/Dfl4.wav&")
    Efl4 = blackkey("Efl4", (190, 10, 50, 300), "afplay audio/Efl4.wav&")
    Gfl4 = blackkey("Gfl4", (360, 10, 50, 300), "afplay audio/Gfl4.wav&")
    Afl5 = blackkey("Afl5", (445, 10, 50, 300), "afplay audio/Afl5.wav&")
    Bfl5 = blackkey("Bfl5", (530, 10, 50, 300), "afplay audio/Bfl5.wav&")
    Dfl5 = blackkey("Dfl5", (700, 10, 50, 300), "afplay audio/Dfl5.wav&")
    Efl5 = blackkey("Efl5", (785, 10, 50, 300), "afplay audio/Efl5.wav&")
    
    board = keys()
    board.addkey(C4)
    board.addkey(D4)
    board.addkey(E4)
    board.addkey(F4)
    board.addkey(G4)
    board.addkey(A5)
    board.addkey(B5)
    board.addkey(C5)
    board.addkey(D5)
    board.addkey(E5)
    board.addkey(F5)
    board.addkey(Dfl4)
    board.addkey(Efl4)
    board.addkey(Gfl4)
    board.addkey(Afl5)
    board.addkey(Bfl5)
    board.addkey(Dfl5)
    board.addkey(Efl5)
    
    
    
    
    while flag:
        pygame.event.get()
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(window, yellow)
        board.play()
        
    
    
    
main()
