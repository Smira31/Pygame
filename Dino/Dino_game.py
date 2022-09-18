import pygame

pygame.init()
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(" Run, Dino, ruuun !!!")

class Cactus:
    def __int__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        self.speed = speed

    def move(self):
        global cactus_x, cactus_y, cactus_width, cactus_height

        if self.x >= - self.width:
            pygame.draw.rect(display, (244, 121, 31), (self.x, self.y, self.width, self.height))
            self.x -= 4
        else:
            self.x = display_width - 50

user_width = 60
user_height = 100
user_x = display_width // 3
user_y = display_height - user_height - 100
jump_counter = 30

cactus_width = 20
cactus_height = 70
cactus_x = display_width -50
cactus_y = display_height - cactus_height - 100

clock = pygame.time.Clock()

make_jump = False

def run_game():
    global make_jump
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()

        display.fill((255, 255, 255))
        draw_array(cactus_arr)

        pygame.draw.rect(display, (247,240,22), (user_x, user_y, user_width, user_height))

        pygame.display.update()
        clock.tick(60)

def jump():
    global user_y, jump_counter, make_jump
    if jump_counter >= -30:
        user_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False

def create_cactus_arr(array):
    array.append(Cactus(display_width + 20, display_height - 170, 20, 70, 4))
    array.append(Cactus(display_width + 300, display_height - 150, 30, 50, 4))
    array.append(Cactus(display_width + 600, display_height - 180, 25, 80, 4))

def draw_array(array):
    for cactus in array:
        cactus.move()





run_game()