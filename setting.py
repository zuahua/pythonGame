class Settings():
    """Fight Warriors的设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_corlor = 230,230,230
        # 玩家的速度
        self.player_speed_factor = 0.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200,0,0)
        # 限制屏幕上子弹个数
        self.bullets_allowed = 3