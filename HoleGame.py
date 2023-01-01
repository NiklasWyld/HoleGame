import random
import pygame

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

        pygame.display.flip()
    else:
        running = False

    clock.tick(30)

pygame.quit()