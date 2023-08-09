# @Time:            2023/7/11 15:15
# @User:            风前絮
# @Site:            cloudfall.top
# @File:            welcome_page
# @Software:        PyCharm
# @Author:          KazeMae
# @Email:           xiaochunfeng.x@foxmail.com
import pygame
from pygame import QUIT

from scene.welcome import WelcomeSprite


def step3_show_actor_by_class():
    """
    step2: 重构图片显示样例
    :return:
    """
    # 初始化pygame
    pygame.init()
    # 获取游戏时钟
    clock = pygame.time.Clock()
    # 获取屏幕分辨率并创建全屏窗口
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    # 加载图片文件并调整其大小以适应屏幕
    background = pygame.image.load("../resources/images/welcome/welcome.jpg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))

    # 精灵
    xiao_tie = WelcomeSprite(50, 300)

    while True:
        # 游戏循环
        for event in pygame.event.get():
            # 关闭事件，进行退出处理
            if event.type == QUIT:
                exit()
        # 绘制图片到显示窗口
        screen.blit(background, (0, 0))
        # 显示角色在（200，200）的位置
        xiao_tie.draw(screen)
        # 通过时钟对象指定循环频率
        clock.tick(20)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.flip()
        # 小铁运动
        xiao_tie.run()


if __name__ == '__main__':
    """
    通过main函数调用step3_show_actor_by_class
    """
    step3_show_actor_by_class()
