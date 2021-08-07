import pygame
from bee import Bee
from cloud import Cloud

pygame.init()

fps = 60
clock = pygame.time.Clock()

screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

bg_image = pygame.image.load('graphics/background.png').convert()

bee_img = pygame.image.load('graphics/bee.png').convert_alpha()
bee = Bee(bee_img)

cloud_img = pygame.image.load('graphics/cloud.png').convert_alpha()
cloud1 = Cloud(cloud_img, 50)
cloud2 = Cloud(cloud_img, 100)
cloud3 = Cloud(cloud_img, 150)

bee_group = pygame.sprite.Group(bee)
cloud_group = pygame.sprite.Group(cloud1, cloud2, cloud3)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

    cloud_group.update()


    screen.blit(bg_image, (0,0))
    bee_group.draw(screen)
    cloud_group.draw(screen)

    pygame.display.update()
    clock.tick()



