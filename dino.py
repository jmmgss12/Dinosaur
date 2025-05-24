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
font.init()
font1 = font.SysFont('Arial', 36)
score = 0


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
        self.jump_h = self.jump_p
        self.jumped = False
        self.gravity = 1
        self.y_o = player_y
        self.ground = True

    def update(self):
        if self.jumped:
            self.rect.y -= self.jump_h # исправил self.rect_y
            self.jump_h -= self.gravity

            if self.rect.y >= self.y_o:
                self.rect.y = self.y_o
                self.jumped = False
                self.jump_h = self.jump_p
                self.ground = True # исправил 0 на True
            
        keys = key.get_pressed()
        if keys[K_SPACE] and self.rect.y == self.y_o: # исправил y_o
            self.jump() # исправил self.jumped()
                

    def jump(self):
        if not self.jumped and self.ground:
            self.jumped = True
            self.ground = False


class Cactus(GameSprite):
        def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
            super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)

        def update(self):
            self.rect.x -= self.speed
            if self.rect.x < -self.rect.width:  # создаем кактус с правой стороны
                self.rect.x = W + randint(50, 200)


            # screen_width = window.display.get_surface().get_width()
            # if self.rect.right < 0:
            #     self.rect.left = screen_width 
            # elif self.rect.left > screen_width:
            #     self.rect.right = 0

        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
                    
                


dino = Dino('Dino1.png', 50, 300, 80, 100, 0)
cactuses = sprite.Group()
cactus = Cactus('Cactus.png', 600, 320, 50, 80, 5)
cactuses.add(cactus)


game = True
finish = False


def restart_game():
    global finish, score
    dino.rect.y = dino.y_o
    dino.jumped = False
    dino.ground = True
    dino.jump_h = dino.jump_p

    cactus.rect.x = 600  # начальная позиция кактуса
    score = 0
    finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish and e.type == KEYDOWN and e.key == K_SPACE:
            restart_game()
    
    if not finish:
        window.blit(back, (0, 0))
        dino.update()
        dino.reset()
        cactus.update()
        cactus.reset()

        # Проверка на столкновение
        if sprite.collide_rect(dino, cactus):
            finish = True

        # Подсчет очков
        score += 1
        score_text = font1.render(f'Очки: {score}', True, (0, 0, 0))
        window.blit(score_text, (10, 10))
    
    else:
        # Экран поражения
        lose_text = font1.render('Ты проиграл! Нажми ПРОБЕЛ', True, (255, 0, 0))
        window.blit(lose_text, (W // 2 - 200, H // 2 - 20))



        # window.blit(cactus, (player_x, player_y))

    display.update()
    clock.tick(60)
