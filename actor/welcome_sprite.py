# @Time:            2023/7/11 14:42
# @User:            风前絮
# @Site:            cloudfall.top
# @File:            walk_soldier
# @Software:        PyCharm
# @Author:          KazeMae
# @Email:           xiaochunfeng.x@foxmail.com

import pygame

from actor.actor import DirWalkByAImage, WalkDir
from scene.images import ActionByMulti


class WalkSoldier(pygame.sprite.Sprite):
    hp = 100
    name = '某军'
    pos_x = 100
    pos_y = 350
    image_width = 50
    image_height = 100

    walk_action = None
    rect = ()

    def __init__(self, walk_path: str, pos_x, pos_y, name, hp):
        super(WalkSoldier, self).__init__()
        self.walk_action = DirWalkByAImage(walk_path,
                                           self.image_width, self.image_height, True)
        self.walk_action.set_dir(WalkDir.down)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name
        self.hp = hp
        self.rect = pygame.Rect(self.pos_x - 5, self.pos_y - 10, self.image_width - 10, self.image_height - 20)

    # 0 下 1 左  2 右 3 上
    def run(self, key: int):
        if key == pygame.K_DOWN:
            self.walk_action.set_dir(WalkDir.down)
            self.pos_y += 10
        elif key == pygame.K_UP:
            self.walk_action.set_dir(WalkDir.up)
            self.pos_y += -10
        elif key == pygame.K_LEFT:
            self.walk_action.set_dir(WalkDir.left)
            self.pos_x += -10
        elif key == pygame.K_RIGHT:
            self.walk_action.set_dir(WalkDir.right)
            self.pos_x += 10

    def draw(self, surface: pygame.Surface):
        """
        绘制
        :param surface:
        :return:
        """
        current_image = self.walk_action.get_image()
        surface.blit(current_image, (self.pos_x, self.pos_y))


class WelcomeSprite(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        初始化多张图片组成的精灵
        :param x: 精灵坐标x
        :param y: 精灵坐标y
        """
        super(WelcomeSprite, self).__init__()
        self.action = ActionByMulti("./resources/images/welcome/%d-1.png", 9, True)

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
