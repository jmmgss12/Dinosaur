from pygame import *
from random import randint
init()

H = 500
W = 700
window = display.set_mode((W, H))
display.set_caption('Динозаврик')
back = transform.scale(image.load("desert.jpg"), (W, H))
lost = 0

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Dino(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.jump_p = 20
        self.jump_h = 0
        self.jumped = False
        self.gravity = 1
        self.y_o = player_y
        self.ground = True

    def update(self):
        if self.jumped:
            self.rect_y -= self.jump_h
            self.jump_h -= self.gravity

class Cactus(GameSprite):
    def update(self):
        self.rect.x -= self.speed



dino = Dino('Dino1.png', 50, 250, 120, 150, 0)
cactuses = sprite.Group()
for i in range(1):
    cactus = Cactus('Cactus.png', 700, 250, 120, 150, randint(1, 3))
    cactuses.add(cactus)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        window.blit(back, (0, 0))
        dino.update()
        dino.reset()
        cactus.update()
        cactus.reset()

    display.update()
    clock.tick(60)

    


