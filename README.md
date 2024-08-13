![img.png](img%2Fimg.png)

# Space shooter

Тут початок проєкта "Космічного шутера"
### підключаення звукового драйвера

````
pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
````

<li>pygame.mixer.init() - ініціалізує модуль для роботи зі звуком.</li>
<li>pygame.mixer.music.load('space.ogg') - завантажує музичний файл.</li>
<li>pygame.mixer.music.set_volume(0.3) - встановлює гучність музики на 30%.</li>
<li>pygame.mixer.music.play() - запускає відтворення музики.</li><br>

### реалізація класа спрайтів 
````
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
````
Цей клас представляє базовий спрайт у грі.

<li>__init__ - це конструктор класу, який ініціалізує зображення спрайта, його розміри, позицію та швидкість.</li>
<li>self.image - завантажує та масштабує зображення спрайта до потрібних розмірів.</li>
<li>self.rect - отримує прямокутник (область) для спрайта, що допомагає відслідковувати його позицію.</li>
<li>reset - метод, що малює спрайт на екрані у його поточній позиції.</li>

### реалізація класа гравця
````
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x <= 620:
            self.rect.x += self.speed
````

Цей клас успадковує всі властивості GameSprite, але додає власний метод update, який відповідає за рух гравця вліво та вправо.

update - метод, що відповідає за обробку натискань клавіш A та D. Якщо натиснута клавіша A і гравець не знаходиться на лівій межі екрану, він переміщується ліворуч. Якщо натиснута клавіша D і гравець не виходить за праву межу екрану, він переміщується праворуч.
### Реалізація ігрового цикла 
````
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.blit(background, (0, 0))
    player.reset()
    player.update()
    pygame.display.update()
    clock.tick(60)
````

Цей блок коду реалізує основний ігровий цикл, який продовжується, поки game має значення True.

<li>for event in pygame.event.get() - перевіряє всі події, що відбулися у грі (наприклад, натискання клавіш, закриття вікна).</li>
<li>if event.type == pygame.QUIT - перевіряє, чи гравець не закрив вікно, і якщо так, завершити гру.</li>
<li>window.blit(background, (0, 0)) - відображає фон на екрані.</li>
<li>player.reset() - відображає гравця на екрані.</li>
<li>player.update() - оновлює позицію гравця відповідно до натискань клавіш.</li>
<li>pygame.display.update() - оновлює екран для відображення нових кадрів.</li>
<li>clock.tick(60) - обмежує частоту кадрів до 60 на секунду.</li>

