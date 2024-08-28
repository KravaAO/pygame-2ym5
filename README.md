![img.png](img%2Fimg.png)

# Space shooter

В цій гілці ми реалізували клас Ворога:

Клас ворога є спадкоємцем базового класу GameSprite

```
class Enemy(GameSprite):
    def update(self): # метод яки відповідає за пересування ворогів
        global lost # вказуємо, що працюємо з глобальною змінною пропущених
        self.rect.y += self.speed # збільшуємо кординату y, щоб наші вороги пересувалися в низ

        if self.rect.y >= 500: # перевірка чи виходить ворог за нижню межу екрана
            self.speed = random.randint(1, 5) # встановлюємо нову швидкість для ворога 
            self.rect.x = random.randint(20, 460) # встановлюємо нову пизицію ворога по х кординаті
            self.rect.y = -40 # встановлюємо нову позицію по у, а саме над ігровим екраном
            lost += 1 # додаємо пропущеного монстра
```

