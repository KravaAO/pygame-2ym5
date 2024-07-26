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


win_width = 700
win_height = 500

player = GameSprite("hero.png", 5, win_height - 80, 4)
enemy = GameSprite("cyborg.png", win_width - 80, 280, 2)
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

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        window.blit(background, (0, 0))
        player.reset()
        enemy.reset()
        final.reset()
        display.update()
        clock.tick(FPS)
