import pygame
import numpy as np
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
# 1. Initialisierung
pygame.init()

pygame.display.set_caption("Mein erstes Pygame")
clock = pygame.time.Clock()

# Farben und Startposition
window = pygame.display.set_mode((1200, 1000))
rect = pygame.Rect(0, 0, 25, 25)
rect1 = pygame.Rect(0, 0, 25, 25)
bomb = pygame.Rect(0, 0, 50, 50)
x, y = 100, 100
speed = 5

def zähle_pixel(window):

    color_array = pygame.PixelArray(window)
    np_pixels = np.array(color_array)
    red_int  = window.map_rgb((255, 0, 0)) 
    blue_int = window.map_rgb((0, 0, 255))
    red_count  = np.count_nonzero(np_pixels == red_int)
    blue_count = np.count_nonzero(np_pixels == blue_int)

    del color_array

    return red_count, blue_count


# 2. Game Loop (Hauptschleife)
running = True
while running:
    # Event-Abfrage (z.B. Fenster schließen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tastatureingaben prüfen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  rect.x -= speed
    if keys[pygame.K_RIGHT]: rect.x += speed
    if keys[pygame.K_UP]:    rect.y -= speed
    if keys[pygame.K_DOWN]:  rect.y += speed


    if keys[pygame.K_a]:  rect1.x -= speed
    if keys[pygame.K_d]:  rect1.x += speed
    if keys[pygame.K_w]:  rect1.y -= speed
    if keys[pygame.K_s]:  rect1.y += speed
    if keys[pygame.K_SPACE]:    
        bomb.x = rect1.x
        pygame.draw.rect(window, "blue", bomb)




    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()
    rect1.centerx = rect1.centerx % window.get_width()
    rect1.centery = rect1.centery % window.get_height()





    # 3. Zeichnen
    #screen.fill(WHITE) # Hintergrund leeren
    pygame.draw.rect(window, "red", rect) # Spieler zeichnen
    pygame.draw.rect(window, "blue", rect1)
    pygame.display.flip() # Bildschirm aktualisieren
    

    
    # 1. Die Farben in das interne Format des Windows umwandeln

    if keys:
        
        red_count, blue_count = zähle_pixel(window)
        rounded_red = round(red_count / 1200000 * 100, 0)
        rounded_blue = round(blue_count / 1200000 * 100, 0)
       
       

    # 2. Pixel zählen (erfordert import numpy as np)

    # 3. WICHTIG: PixelArray löschen, um das Surface wieder freizugeben
    # 3. Text-Oberflächen (Surfaces) erstellen
    text_red = my_font.render(f"Rot: {rounded_red}%", True, (255, 255, 255))
    text_blue = my_font.render(f"Blau: {rounded_blue}%", True, (255, 255, 255))

    oberer_balken = pygame.Rect(0, 0, 200, 100)


    pygame.draw.rect(window, (0, 0, 0), oberer_balken) # Falls Hintergrund schwar
    window.blit(text_red, (10, 10))   # Position oben links
    window.blit(text_blue, (10, 50))  # Etwas tiefer darunter




    clock.tick(60)

    

pygame.quit()
