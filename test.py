import pygame

# 1. Initialisierung
pygame.init()

pygame.display.set_caption("Mein erstes Pygame")
clock = pygame.time.Clock()

# Farben und Startposition
window = pygame.display.set_mode((1200, 1000))
rect = pygame.Rect(0, 0, 25, 25)
rect1 = pygame.Rect(0, 0, 25, 25)
x, y = 100, 100
speed = 5

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


    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()


    # 3. Zeichnen
    #screen.fill(WHITE) # Hintergrund leeren
    pygame.draw.rect(window, "red", rect) # Spieler zeichnen
    pygame.draw.rect(window, "blue", rect1)
    pygame.display.flip() # Bildschirm aktualisieren
    clock.tick(60) # Begrenzung auf 60 FPS

pygame.quit()
