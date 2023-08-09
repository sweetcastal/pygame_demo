import pygame
from pytmx import load_pygame, TiledObjectGroup

from actor.actor import RedArmyShootSoldier
from actor.actor import XiaoTie
from actor.japanese_soldier import JapaneseWalkSoldier
from game.game import SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT


def create_sprite(tiled_map_data, obstacle_group, japanese_group, prizes_group):
    jian_jun = None
    tie_tou = None
    for group in tiled_map_data.objectgroups:
        if isinstance(group, TiledObjectGroup):
            if group.name == '日本人':
                for obj in group:
                    japanese = JapaneseWalkSoldier(obj.x, obj.y)
                    japanese_group.add(japanese)
            elif group.name == '奖品':
                for obj in group:
                    prizes = pygame.sprite.Sprite()
                    prizes.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    prizes_group.add(prizes)
            elif group.name == '障碍物':
                for obj in group:
                    obs = pygame.sprite.Sprite()
                    obs.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    obstacle_group.add(obs)
            elif group.name == '解放军':
                for obj in group:
                    if obj.name == '建军':
                        jian_jun = RedArmyShootSoldier(obj.x, obj.y)
                    if obj.name == '铁头':
                        tie_tou = RedArmyShootSoldier(obj.x, obj.y)
            elif group.name == '小铁':
                for obj in group:
                    if obj.name == '小铁':
                        xiao_tie = XiaoTie(obj.x, obj.y)
    return jian_jun, tie_tou, xiao_tie


def boundary(x, y):
    view_x = x - SCREEN_HALF_WIDTH
    view_y = y - SCREEN_HALF_HEIGHT
    if view_x < 0:
        view_x = 0

    if view_y < 0:
        view_y = 0

    if view_x >= 2800 - SCREEN_WIDTH:
        view_x = 2800 - SCREEN_WIDTH - 1
    if view_y >= 1200 - SCREEN_HEIGHT:
        view_y = 1200 - SCREEN_HEIGHT - 1
    return view_x, view_y


def step9_screen_view():
    """
    step9: 视窗移动
    :return:
    """
    # 初始化pygame
    pygame.init()
    # 获取游戏时钟
    clock = pygame.time.Clock()
    # 创建游戏的窗口 1280 * 720 根据要显示图片的大小设置
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    background = pygame.image.load("./resources/tmx/tunnel_map.png")
    tiled_map_data = load_pygame("resources/tmx/tunnel_map_1.tmx")

    obstacle_group = pygame.sprite.Group()
    japanese_group = pygame.sprite.Group()
    prizes_group = pygame.sprite.Group()
    jian_jun, tie_tou, xiao_tie = create_sprite(tiled_map_data, obstacle_group, japanese_group, prizes_group)

    while True:
        # 游戏循环
        for event in pygame.event.get():
            # 关闭事件，进行退出处理
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                xiao_tie.run(event.key)

        view_x, view_y = boundary(xiao_tie.pos_x, xiao_tie.pos_y)
        # 绘制图片到显示窗口
        sub_view = background.subsurface((view_x, view_y, SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(sub_view, (0, 0))
        xiao_tie.draw(screen, view_x, view_y)

        # 通过时钟对象指定循环频率
        clock.tick(20)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.flip()


if __name__ == '__main__':
    step9_screen_view()
