from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = False

    def update(self):
        if not self.direction:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= 470:
            self.direction = True
        if self.rect.x > 700 - 80:
            self.direction = False


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, x, y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height

        self.surf = Surface((self.width, self.height))
        self.surf.fill((color_1, color_2, color_3))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.surf, (self.rect.x, self.rect.y))

w1 = Wall(0, 255, 0, 450, 90, 10, 500)
w2 = Wall(0, 255, 0, 380, 90, 70, 10)

win_width = 700
win_height = 500

player = Player("hero.png", 5, win_height - 80, 4)
enemy = Enemy("cyborg.png", win_width - 80, 280, 2)
final = GameSprite("treasure.png", win_width - 120, win_height - 80, 0)

window = display.set_mode((win_width, win_height))

display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render('U WIN!', True, (250, 215, 0))
lose = font.render('U lose', True, (250, 0, 0))

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    if not finish:
        player.reset()
        enemy.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        player.update()
        enemy.update()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (250, 250))

    if sprite.collide_rect(player, enemy):
        finish = True
        window.blit(lose, (250, 250))

    if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2):
        finish = True
        window.blit(lose, (250, 250))


    display.update()
    clock.tick(FPS)
