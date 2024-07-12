import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch up')
clock = pygame.time.Clock()

bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (700, 500))
sprite1 = pygame.transform.scale(pygame.image.load('hero.png'), (50, 50))
sprite2 = pygame.transform.scale(pygame.image.load('cyborg.png'), (50, 50))

x_h = 50
y_h = 350
x_c = 400

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    kyes = pygame.key.get_pressed()
    if kyes[pygame.K_RIGHT] and x_h < WIDTH - 50:
        x_h += 5
    elif kyes[pygame.K_LEFT] and x_h > 5:
        x_h -= 5
    # elif kyes[pygame.K_UP] and y_h > 0: # пересування гравця у гору
    #    y_h -= 5

    if kyes[pygame.K_a]:
        x_c -= 5
    elif kyes[pygame.K_d]:
        x_c += 5

    window.blit(bg, (0, 0))
    window.blit(sprite1, (x_h, y_h))
    window.blit(sprite2, (x_c, 350))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
