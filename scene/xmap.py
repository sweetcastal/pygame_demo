import pygame
from pytmx import load_pygame, TiledObjectGroup

from actor.welcome_sprite import WelcomeSprite
from welcome import WelcomeSprite


def step7_show_tmx_png():
    """
    step7-2: 优化显示
    :return:
    """
    # 初始化pygame
    pygame.init()
    # 获取游戏时钟
    clock = pygame.time.Clock()
    # 创建游戏的窗口 1280 * 720 根据要显示图片的大小设置
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    background = pygame.image.load("./resources/tmx/tunnel_map.png")
    tiled_map_data = load_pygame("./resources/tmx/tunnel_map_1.tmx")
    xiao_tie = None
    for group in tiled_map_data.objectgroups:
        if isinstance(group, TiledObjectGroup):
            if group.name == '日本人':
                for obj in group:
                    print(obj.x, obj.y, obj.width, obj.height)
            elif group.name == '奖品':
                for obj in group:
                    print(obj.x, obj.y, obj.width, obj.height)
            elif group.name == '障碍物':
                for obj in group:
                    print(obj.x, obj.y, obj.width, obj.height)
            elif group.name == '小铁':
                for obj in group:
                    if obj.name == '小铁':
                        print(obj.x, obj.y, obj.width, obj.height)
                        xiao_tie = WelcomeSprite(obj.x, obj.y)

    while True:
        # 游戏循环
        for event in pygame.event.get():
            # 关闭事件，进行退出处理
            if event.type == pygame.QUIT:
                exit()
        # 绘制图片到显示窗口
        screen.blit(background, (0, 0))
        xiao_tie.draw(screen)
        # 通过时钟对象指定循环频率
        clock.tick(20)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.flip()


if __name__ == '__main__':
    """
    通过main函数调用step7_show_tmx_png
    """
    step7_show_tmx_png()
