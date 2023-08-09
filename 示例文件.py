import pygame


def shi_li():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("咕咕咕咕咕")
    screen = pygame.display.set_mode((640, 236), 0, 32)
    background = pygame.image.load("地道战示意图.jpg").convert()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(background, (0, 0))
        clock.tick(144)
        pygame.display.flip()


shi_li()
