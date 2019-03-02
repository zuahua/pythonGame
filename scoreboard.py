import pygame.font
from pygame.sprite import Group
from player import Player

class Scoreboard():
    """显示得分的类"""
    def __init__(self, ai_settings, screen, stats):
        """初始化得分属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        # 得分文本属性信息
        self.text_color = (40,40,40)
        self.font = pygame.font.SysFont(None, 30)
        # 分数图像与最高得分图像、等级显示、渲染玩家剩余次数图
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_players()

    def prep_score(self):
        """将得分转换为一幅渲染图像"""
        # 圆整分数，使其为10的整数倍
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 得分图像位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """将最高得分渲染为图像"""
        self.text_high_score = str(self.stats.high_score)
        self.image_high_score = self.font.render(self.text_high_score, True,
                                                 self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.image_high_score.get_rect()
        # 位置:屏幕顶部中央
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """(在玩家分数下显示等级)创建等级文本渲染图像"""
        self.text_level = str(self.stats.level)
        self.image_level = self.font.render(self.text_level, True, self.text_color,
                                            self.ai_settings.bg_color)
        self.level_rect = self.image_level.get_rect()
        # 位置:玩家分数下
        self.level_rect.top = self.score_rect.bottom + 10
        self.level_rect.right = self.score_rect.right

    def prep_players(self):
        """创建玩家的编组"""
        self.players = Group()
        for player_number in range(self.stats.player_left):
            player = Player(self.screen, self.ai_settings)
            player.rect.x = 10 + player_number * player.rect.width
            player.rect.y = 10
            self.players.add(player)

    def show_score(self):
        """显示得分和最高得分、玩家等级"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.image_high_score, self.high_score_rect)
        self.screen.blit(self.image_level, self.level_rect)
        # 绘制玩家个数
        self.players.draw(self.screen)