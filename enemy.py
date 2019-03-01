import pygame
from pygame.sprite import Sprite




class Enemy(Sprite):
    """创建一个敌人"""
    def __init__(self, screen, ai_settings):
        """初始化"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 获取敌人图片
        self.image = pygame.image.load(r'images\S_Death02.bmp')
        # 获取矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 设置敌人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储敌人准确位置
        self.x = float(self.rect.x)


    def blitme(self):
        """绘制敌人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向左或右移动敌人"""
        self.x += (self.ai_settings.enemy_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edge(self):
        """检查敌人是否到达屏幕边缘，到达边缘返回True"""
        screen_rect = self.screen.get_rect()
        if screen_rect.right <= self.rect.right:
            return True
        elif self.rect.left <= 0:
            return True

