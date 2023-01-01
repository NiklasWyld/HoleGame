import random
import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

pygame.init()
pygame.display.set_caption('Hole Game')
screen = pygame.display.set_mode([1000, 800])
running = True
x, y = 500, 400
speed_x, speed_y = 0, 0
size = 15
speed = 5

colors = ['red', 'blue', 'green', 'yellow', 'purple']
points = []
points_final = []

play_button_img = pygame.image.load('Button.png').convert_alpha()

play_button = Button(420, 300, play_button_img, 0.3)

state = 'menu'

def draw_text(font_size: int, text: str, surface, color: str, x_t: int, y_t: int):
    pygame.font.init()
    font = pygame.font.SysFont('Arial', font_size)
    text = font.render(text, False, color)
    surface.blit(text, (x_t, y_t))

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_y = -speed
            if event.key == pygame.K_s:
                speed_y = speed
            if event.key == pygame.K_a:
                speed_x = -speed
            if event.key == pygame.K_d:
                speed_x = speed
            if event.key == pygame.K_ESCAPE:
                state = 'menu'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed_x = 0
            if event.key == pygame.K_d:
                speed_x = 0
            if event.key == pygame.K_w:
                speed_y = 0
            if event.key == pygame.K_s:
                speed_y = 0

    if state == 'game':
        screen.fill('white')

        x += speed_x
        y += speed_y

        player = pygame.draw.ellipse(screen, 'black', (x, y, size, size))
        pointm = (screen, random.choice(colors), (random.randint(10, 930), random.randint(10, 730), 15, 15))

        points_final.clear()

        if len(points) <= 9:
            points.append(pointm)

        for point in points:
            if point != pointm:
                points_final.append(pygame.draw.ellipse(point[0], point[1], point[2]))

        for i in range(len(points_final) - 1):
            point = points_final[i]
            if point.colliderect(player):
                points.pop(i)
                points_final.remove(point)
                size += 2
                speed += 0.2
                if len(points_final) <= 10:
                    break

        pygame.display.flip()
    elif state == 'menu':
        screen.fill('white')

        draw_text(100, 'Hole Game', screen, 'black', 250, 50)

        if play_button.draw(screen):
            state = 'game'

        pygame.display.flip()
    else:
        running = False

    clock.tick(30)

pygame.quit()