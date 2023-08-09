# @Time:            2023/7/11 14:42
# @User:            风前絮
# @Site:            cloudfall.top
# @File:            welcome
# @Software:        PyCharm
# @Author:          KazeMae
# @Email:           xiaochunfeng.x@foxmail.com


import pygame

from scene.images import ActionByMulti


class WelcomeSprite(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        初始化多张图片组成的精灵
        :param x: 精灵坐标x
        :param y: 精灵坐标y
        """
        super(WelcomeSprite, self).__init__()
        self.action = ActionByMulti("../resources/images/welcome/%d-1.png", 9, True)

        self.pos_x = x
        self.pos_y = y

    def draw(self, surface):
        """
        精灵绘制
        :param surface: 绘制surface
        :return:
        """
        current_img = self.action.get_image()
        surface.blit(current_img, (self.pos_x, self.pos_y))

    def run(self):
        """
        精灵运动,主动运动
        :return:
        """
        if self.pos_x < 1000:
            self.pos_x += 4

# def welcome_images():
#     """
#     生成欢迎页面动画数组
#     :return: 图片数组
#     """
#     animation_frames = []
#     for i in range(1, 10):
#         # 路径文件名
#         image_file_path = "../resources/images/welcome/{}-1.png".format(i)
#         # print(image_file_path)
#         # 图片加载
#         image = pygame.image.load(image_file_path)
#         image = pygame.transform.scale(image, (240, 240))
#         # 放入数组
#         animation_frames.append(image)
#     return animation_frames
#
#
# def show_welcome_animation():
#     """
#     显示欢迎时的人物
#     :return:
#     """
#     pygame.init()
#     clock = pygame.time.Clock()
#     # 设置图标和名称
#     icon = pygame.image.load("../resources/images/welcome/welcome.jpg")
#     pygame.display.set_icon(icon)
#     pygame.display.set_caption("地道战  Welcome")
#     # 获取屏幕分辨率并创建全屏窗口
#     screen_info = pygame.display.Info()
#     screen_width = screen_info.current_w
#     screen_height = screen_info.current_h
#     screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
#     # 加载图片文件并调整其大小以适应屏幕
#     background = pygame.image.load("../resources/images/welcome/welcome.jpg").convert()
#     background = pygame.transform.scale(background, (screen_width, screen_height))
#     # 获取角色图片数组
#     animation_frames = welcome_images()
#
#     # 游戏主程序
#     running = True
#     animation_idx = 0
#     while running:
#         # 游戏循环
#         for event in pygame.event.get():
#             # 关闭事件，进行退出处理
#             if event.type == pygame.QUIT:
#                 running = False
#         # 绘制图片到显示窗口
#         screen.blit(background, (0, 0))
#         # 显示角色在（200，200）的位置
#         screen.blit(animation_frames[animation_idx], (200, 200))
#         # 通过时钟对象指定循环频率
#         clock.tick(20)
#         # 调用flip方法更新显示,也可以使用update方法
#         pygame.display.update()
#         # 图片显示序号变量循环处理
#         animation_idx = (animation_idx + 1) % len(animation_frames)
#         # print(animation_idx)


# if __name__ == '__main__':
#     show_welcome_animation()

# def welcome_page():
#     pygame.init()
#     clock = pygame.time.Clock()
#
#     # 设置图标和名称
#     icon = pygame.image.load("../resources/images/mine/mine.png")
#     pygame.display.set_icon(icon)
#     pygame.display.set_caption("地道战  demo")
#
#     # 获取屏幕分辨率并创建全屏窗口
#     screen_info = pygame.display.Info()
#     screen_width = screen_info.current_w
#     screen_height = screen_info.current_h
#     screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
#
#     # 加载背景图片并调整其大小以适应屏幕
#     background = pygame.image.load("../resources/images/welcome/welcome.jpg")
#     background = pygame.transform.scale(background, (screen_width, screen_height))
#
#     # 加载人物的每一帧图片
#     frame1 = pygame.image.load("../resources/images/welcome/1-1.png")
#     frame2 = pygame.image.load("../resources/images/welcome/2-1.png")
#     frame3 = pygame.image.load("../resources/images/welcome/3-1.png")
#     frame4 = pygame.image.load("../resources/images/welcome/4-1.png")
#     frame5 = pygame.image.load("../resources/images/welcome/5-1.png")
#     frame6 = pygame.image.load("../resources/images/welcome/6-1.png")
#     frame7 = pygame.image.load("../resources/images/welcome/7-1.png")
#     frame8 = pygame.image.load("../resources/images/welcome/8-1.png")
#     frame9 = pygame.image.load("../resources/images/welcome/9-1.png")
#
#     # 将每一帧图片调整为相同大小
#     frame1 = pygame.transform.scale(frame1, (240, 240))
#     frame2 = pygame.transform.scale(frame2, (240, 240))
#     frame3 = pygame.transform.scale(frame3, (240, 240))
#     frame4 = pygame.transform.scale(frame4, (240, 240))
#     frame5 = pygame.transform.scale(frame5, (240, 240))
#     frame6 = pygame.transform.scale(frame6, (240, 240))
#     frame7 = pygame.transform.scale(frame7, (240, 240))
#     frame8 = pygame.transform.scale(frame8, (240, 240))
#     frame9 = pygame.transform.scale(frame9, (240, 240))
#
#     # 创建人物动画列表
#     animation_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9]
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
