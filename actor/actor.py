# @Time:            2023/7/11 14:42
# @User:            风前絮
# @Site:            cloudfall.top
# @File:            action_role
# @Software:        PyCharm
# @Author:          KazeMae
# @Email:           xiaochunfeng.x@foxmail.com

import enum

import pygame


class WalkDir(enum.IntEnum):
    down = 0
    left = 1
    right = 2
    up = 3


class DirWalkByAImage:
    """
    一张图 4*4人物 下 左 右 上
    """
    image_count = 16
    image_col = 4
    image_width = 49
    image_height = 74
    walk_dir = WalkDir.down

    def __init__(self, path_name: str, image_width: int, image_height: int, is_loop: bool):
        """
        初始化
        :param path_name: 图片路径
        :param image_width: 单张图片宽度
        :param image_height: 单张图片高度
        :param is_loop: 是否循环
        """
        self.path_name = path_name
        self.image_index = 0
        self.action_images = []  # 四个方向的图片数组
        self.image_height = image_height
        self.image_width = image_width

        self.is_loop = is_loop
        print(path_name)
        self.image = pygame.image.load(path_name)  # .convert()
        mid = []
        for i in range(0, self.image_count):
            row = int(i / self.image_col)
            col = i % self.image_col
            # print(row, col)
            if col == 0:
                self.action_images.append(mid)
                mid.clear()

            rect = (col * self.image_width,
                    row * self.image_height,
                    self.image_width,
                    self.image_height)
            # print(rect)
            image = self.image.subsurface(rect)
            mid.append(image)

    def get_image(self) -> pygame.Surface:
        """
        获取当前显示图片
        :return:
        """
        current_image = self.action_images[self.walk_dir][self.image_index]
        self.image_index += 1
        if self.image_index >= self.image_col:
            if self.is_loop:
                self.image_index = 0
            else:
                self.image_index = self.image_col - 1
        return current_image

    def set_dir(self, dir: WalkDir):
        """
        设置方向
        :param dir:  方向
        :return:
        """
        self.walk_dir = dir

    def is_end(self) -> bool:
        """
        是否播放完毕
        :return:
        """
        if self.is_loop:
            return False
        else:
            if self.image_index >= self.image_col - 1:
                return True
            else:
                return False


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
        :param x:
        :param y:
        :return:
        """
        current_image = self.walk_action.get_image()
        surface.blit(current_image, (self.pos_x, self.pos_y))


class ShootDir(enum.IntEnum):
    not_shoot = 0
    left_down = 1
    right_down = 2
    left_up = 3
    right_up = 4
    up = 5
    down = 6


class DirShootByAImage(DirWalkByAImage):
    """
    一张图 4*4人物  左蹲射击， 右蹲射击，左站射击，右站射击
    """
    image_count = 16
    image_col = 4
    image_width = 49
    image_height = 74
    shoot_dir = ShootDir.left_up

    @staticmethod
    def __init_shoot(up_image_path, down_image_path):  # 和视频有点差异，请自行理解并选择函数设计
        """
        初始化射击图片
        :param up_image_path:
        :param down_image_path:
        :return:
        """

        DirShootByAImage.up_shoot_image = pygame.image.load(up_image_path).convert_alpha()
        DirShootByAImage.down_shoot_image = pygame.image.load(down_image_path).convert_alpha()

    def __init__(self, path_name: str, image_width: int, image_height: int, is_loop: bool):
        super(DirShootByAImage, self).__init__(path_name, image_width, image_height, is_loop)
        self.__init_shoot("./resources/images/shoot/up_shoot.png",
                          "./resources/images/shoot/down_shoot.png")

    def get_image(self) -> pygame.Surface:
        """
        获取射击图片
        :return:
        """
        if self.shoot_dir == ShootDir.not_shoot:
            return None
        if self.shoot_dir < ShootDir.up:
            current_img = self.action_images[self.shoot_dir - 1][self.image_index]
            self.image_index += 1
            if self.image_index >= self.image_col:
                if self.is_loop:
                    self.image_index = 0
                else:
                    self.image_index = self.image_col - 1
        elif self.shoot_dir == ShootDir.up:
            current_img = DirShootByAImage.up_shoot_image
        else:
            current_img = DirShootByAImage.down_shoot_image
        return current_img

    def set_dir(self, dir: ShootDir):
        """
        获取射击方向
        :param dir:
        :return:
        """
        self.shoot_dir = dir


class ShootSoldier(WalkSoldier):
    shoot_image_width = 100
    shoot_image_height = 100

    def __init__(self, work_path: str, shoot_action: str, pos_x, pos_y, name, hp):
        super(ShootSoldier, self).__init__(work_path, pos_x, pos_y, name, hp)
        self.shoot_action = DirShootByAImage(shoot_action,
                                             self.shoot_image_width, self.shoot_image_height, True)

        self.shoot_action.set_dir(ShootDir.not_shoot)

    # 0 下 1 左  2 右 3 上
    def run(self, key: int):
        self.shoot_action.set_dir(ShootDir.not_shoot)
        super(ShootSoldier, self).run(key)
        if key == pygame.K_q:
            self.shoot_action.set_dir(ShootDir.left_up)
        elif key == pygame.K_a:
            self.shoot_action.set_dir(ShootDir.left_down)
        elif key == pygame.K_e:
            self.shoot_action.set_dir(ShootDir.right_up)
        elif key == pygame.K_d:
            self.shoot_action.set_dir(ShootDir.right_down)
        elif key == pygame.K_w:
            self.walk_action.set_dir(WalkDir.up)
            self.shoot_action.set_dir(ShootDir.up)
        elif key == pygame.K_s:
            self.walk_action.set_dir(WalkDir.down)
            self.shoot_action.set_dir(ShootDir.down)

    def draw(self, surface: pygame.Surface):
        """
        绘制
        :param surface:
        :param x:
        :param y:
        :return:
        """
        if self.shoot_action.shoot_dir == ShootDir.not_shoot:
            super(ShootSoldier, self).draw(surface)
        elif self.shoot_action.shoot_dir == ShootDir.down:
            current_image = self.shoot_action.get_image()
            surface.blit(current_image, (self.pos_x, self.pos_y))
            current_image = self.walk_action.get_image()
            surface.blit(current_image, (self.pos_x, self.pos_y))
        elif self.shoot_action.shoot_dir == ShootDir.up:
            current_image = self.shoot_action.get_image()
            surface.blit(current_image, (self.pos_x, self.pos_y - 60))
            current_image = self.walk_action.get_image()
            surface.blit(current_image, (self.pos_x, self.pos_y))
        else:
            current_image = self.shoot_action.get_image()
            surface.blit(current_image, (self.pos_x, self.pos_y))


class RedArmyShootSoldier(ShootSoldier):
    def __init__(self, x, y):
        super(RedArmyShootSoldier, self).__init__("./resources/images/chinese/red_army/red_army1.png",
                                                  "./resources/images/chinese/red_army/red_army1-1.png",
                                                  x, y, "红军", 100)


class XiaoTie(pygame.sprite.Sprite):
    hp = 100
    name = '小铁'
    pos_x = 1001
    pos_y = 350
    image_width = 50
    image_height = 74
    current_status = "boy"
    boy_base_action = None
    army_base_action = None
    dir = WalkDir.down

    def __init__(self, x, y):
        super(XiaoTie, self).__init__()
        self.boy_base_action = DirWalkByAImage("./resources/images/chinese/militia/boy1.png",
                                               self.image_width, self.image_height, True)
        self.army_base_action = DirWalkByAImage("./resources/images/chinese/red_army/boy1.png",
                                                self.image_width, self.image_height, True)

        self.boy_base_action.set_dir(self.dir)
        self.army_base_action.set_dir(self.dir)
        self.current_action = self.boy_base_action
        self.pos_x = x
        self.pos_y = y

    # 0 下 1 左  2 右 3 上
    def run(self, key: int):

        if key == pygame.K_DOWN:
            self.dir = WalkDir.down
            self.pos_y += 10

        elif key == pygame.K_UP:
            self.dir = WalkDir.up
            self.pos_y += -10

        elif key == pygame.K_LEFT:
            self.dir = WalkDir.left
            self.pos_x += -10

        elif key == pygame.K_RIGHT:
            self.dir = WalkDir.right
            self.pos_x += 10

        self.boy_base_action.set_dir(self.dir)
        self.army_base_action.set_dir(self.dir)

        # 0 下 1 左  2 上 3 右

    def set_status(self, status: str):
        self.current_status = status
        if self.current_status == "boy":
            self.current_action = self.boy_base_action
        else:
            self.current_action = self.army_base_action

        #     def draw(self, surface: pygame.Surface):
        #        """
        #        未处理窗口移动时
        #        """
        #        current_image = self.current_action.get_image()
        #        surface.blit(current_image, (self.pos_x, self.pos_y))
        #        pygame.draw.rect(surface, pygame.Color(255, 255, 0),
        #                         (self.pos_x + 15, self.pos_y + 60,
        #                          20, 10), 1)

    def draw(self, surface: pygame.Surface, x: int, y: int):
        """
        加未处理窗口移动时
        """
        current_image = self.current_action.get_image()
        surface.blit(current_image, (self.pos_x - x, self.pos_y - y))
        pygame.draw.rect(surface, pygame.Color(255, 255, 0),
                         (self.pos_x - x + 15, self.pos_y - y + 60,
                          20, 10), 1)
