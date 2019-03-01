import pygame

class Player():
    """玩家"""
    def __init__(self, screen, ai_settings):
        """"初始化玩家并设置玩家位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载游戏图像并获取其外接矩形
        self.image = pygame.image.load(r'images\gamePlayer1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 玩家初始位置设置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在玩家center属性中存储小数值
        self.center = float(self.rect.centerx)

        # 玩家移动的属性
        self.moving_right = False
        self.moving_left = False





    def blitme(self):
        """在指定位置绘制玩家"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新玩家移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.player_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.player_speed_factor

        # 根据center值更新rect
        self.rect.centerx = self.center
