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
        self.jump_h = 10
        self.jumped = False
        self.gravity = 1
        self.y_o = player_y
        self.ground = True

    def update(self):
        if self.jumped:
            self.rect_y -= self.jump_h
            self.jump_h -= self.gravity

            if self.rect.y >= self.y_o:
                self.rect.y = self.y_o
                self.jumped = False
                self.jump_h = 0
                self.ground = 0
            
            keys = key.get_pressed()
            if keys[K_SPACE] and self.rect.y == y_o:
                self.jumped()
                

    def jump(self):
        if not self.jumped and self.ground:
            self.jumped = True
            self.ground = False


class Cactus(GameSprite):
        def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
            super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)

        def update(self):
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.y = 250
                self.rect.x = 500


            # screen_width = window.display.get_surface().get_width()
            # if self.rect.right < 0:
            #     self.rect.left = screen_width 
            # elif self.rect.left > screen_width:
            #     self.rect.right = 0

        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
                    
                


dino = Dino('Dino1.png', 50, 250, 120, 150, 0)
cactuses = sprite.Group()
cactus = Cactus('Cactus.png', 50, 250, 120, 150, 5)
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

        # window.blit(cactus, (player_x, player_y))

    display.update()
    clock.tick(60)

    


