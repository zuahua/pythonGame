import pygame
from pygame.sprite import Sprite




class Enemy(Sprite):
    """创建一个敌人"""
    def __init__(self, screen, ai_settings):
        """初始化"""
        super(Enemy, self).__init__()
        self.screen = screen

        # 获取敌人图片
        self.image = pygame.image.load(r'images\S_Death02.bmp')
        # 获取矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 设置敌人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人准确位置
        self.x = float(self.rect.x)


    def blitme(self):
        """绘制敌人"""
        self.screen.blit(self.image, self.rect)