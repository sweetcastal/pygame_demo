# @Time:            2023/7/11 15:12
# @User:            风前絮
# @Site:            cloudfall.top
# @File:            images
# @Software:        PyCharm
# @Author:          KazeMae
# @Email:           xiaochunfeng.x@foxmail.com
import pygame


class ActionByMulti:
    def __init__(self, path_expression: str, image_count: int, is_loop: bool):
        """
        初始化
        :param path_expression: 图片路径
        :param image_count: 图片数量
        :param is_loop: 是否循环
        """
        self.image_index = 0
        self.action_images = []
        self.image_count = image_count
        self.is_loop = is_loop

        for i in range(0, image_count):
            img_path = str.format(path_expression % (i + 1))
            self.action_images.append(pygame.image.load(img_path))

    def get_image(self) -> pygame.Surface:
        """
        获取当前显示图片
        :return:
        """
        current_img = self.action_images[self.image_index]
        if self.image_index + 1 >= self.image_count:
            if self.is_loop:
                self.image_index = 0
        else:
            self.image_index += 1
        return current_img

    def is_end(self) -> bool:
        """
        图片是否绘制结束
        :return: True
        """
        if self.is_loop:
            return False
        else:
            if self.image_index >= self.image_count - 1:
                return True
            else:
                return False
