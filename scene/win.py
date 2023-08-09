# @Time:            2023/7/11 14:42
# @User:            风前絮
# @Site:            cloudfall.top
# @File:            win
# @Software:        PyCharm
# @Author:          KazeMae
# @Email:           xiaochunfeng.x@foxmail.com


import pygame


def win_images():
    """
    生成胜利页面动画数组
    :return: 图片数组
    """
    animation_frames = []
    for i in range(1, 8):
        # 路径文件名
        image_file_path = "../resources/images/win/w_{}.png".format(i)
        # print(image_file_path)
        # 图片加载
        image = pygame.image.load(image_file_path)
        image = pygame.transform.scale(image, (335, 335))
        # 放入数组
        animation_frames.append(image)
    return animation_frames


def show_win_animation():
    """
    显示胜利时人物
    :return:
    """
    pygame.init()
    clock = pygame.time.Clock()
    # 设置图标和名称
    icon = pygame.image.load("../resources/images/mine/mine.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("地道战  Win")
    # 获取屏幕分辨率并创建全屏窗口
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    # 加载图片文件并调整其大小以适应屏幕
    background = pygame.image.load("../resources/images/win/win.jpg").convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))
    # 获取角色图片数组
    animation_frames = win_images()

    # 游戏主程序
    running = True
    animation_idx = 0
    while running:
        # 游戏循环
        for event in pygame.event.get():
            # 关闭事件，进行退出处理
            if event.type == pygame.QUIT:
                running = False
        # 绘制图片到显示窗口
        screen.blit(background, (0, 0))
        # 显示角色在（200，200）的位置
        screen.blit(animation_frames[animation_idx], (200, 200))
        # 通过时钟对象指定循环频率
        clock.tick(20)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.update()
        # 图片显示序号变量循环处理
        animation_idx = (animation_idx + 1) % len(animation_frames)
        # print(animation_idx)


if __name__ == '__main__':
    show_win_animation()

# def win_page():
#     pygame.init()
#     clock = pygame.time.Clock()
#
#     # 设置图标和名称
#     icon = pygame.image.load("./resources/images/mine/mine.png")
#     pygame.display.set_icon(icon)
#     pygame.display.set_caption("地道战  Win")
#
#     # 获取屏幕分辨率并创建全屏窗口
#     screen_info = pygame.display.Info()
#     screen_width = screen_info.current_w
#     screen_height = screen_info.current_h
#     screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
#
#     # 加载背景图片并调整其大小以适应屏幕
#     background = pygame.image.load("./resources/images/win/win.jpg")
#     background = pygame.transform.scale(background, (screen_width, screen_height))
#
#     # 加载人物的每一帧图片
#     frame1 = pygame.image.load("./resources/images/win/w_1.png")
#     frame2 = pygame.image.load("./resources/images/win/w_2.png")
#     frame3 = pygame.image.load("./resources/images/win/w_3.png")
#     frame4 = pygame.image.load("./resources/images/win/w_4.png")
#     frame5 = pygame.image.load("./resources/images/win/w_5.png")
#     frame6 = pygame.image.load("./resources/images/win/w_6.png")
#     frame7 = pygame.image.load("./resources/images/win/w_7.png")
#
#     # 将每一帧图片调整为相同大小
#     frame1 = pygame.transform.scale(frame1, (335, 335))
#     frame2 = pygame.transform.scale(frame2, (335, 335))
#     frame3 = pygame.transform.scale(frame3, (335, 335))
#     frame4 = pygame.transform.scale(frame4, (335, 335))
#     frame5 = pygame.transform.scale(frame5, (335, 335))
#     frame6 = pygame.transform.scale(frame6, (335, 335))
#     frame7 = pygame.transform.scale(frame7, (335, 335))
#
#     # 创建人物动画列表
#     animation_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7]
#
#     # 设置动画帧率
#     animation_index = 0
#     animation_speed = 0.1  # 切换动画帧的速度（每秒切换次数）
#     animation_timer = 0.0
#
#     # 游戏主程序
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()
#         screen.blit(background, (0, 0))
#
#         # 更新动画帧
#         animation_timer += clock.tick(60) / 1000.0
#         if animation_timer >= animation_speed:
#             animation_index = (animation_index + 1) % len(animation_frames)
#             animation_timer = 0.0
#
#         # 绘制当前动画帧
#         current_frame = animation_frames[animation_index]
#         screen.blit(current_frame, (200, 200))
#
#         pygame.display.update()
#
