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
        self.bullet_speed_factor = 2
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (254, 254, 0)
        # 限制屏幕上子弹个数
        self.bullets_allowed = 3
        # 敌人设置
        # 敌人右移动速度
        self.enemy_speed_factor = 0.3
        # 敌人下移速度
        self.fleet_drop_speed = 2
        # 设置敌人移动方向,1为右，-1为左
        self.fleet_direction = 1


