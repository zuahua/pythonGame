class Settings():
    """Fight Warriors的设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = 230,230,230

        # 玩家设置
        self.player_limit = 3


        # 子弹设置

        self.bullet_width = 300
        self.bullet_height = 4
        self.bullet_color = 254, 254, 0
        # 限制屏幕上子弹个数
        self.bullets_allowed = 3

        # 敌人设置

        # 敌人下移速度
        self.fleet_drop_speed = 20


        # 以什么样的方式加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # 敌人点数提高速度
        self.score_scale = 1.1



    def initialize_dynamic_settings(self):
        """初始化随游戏进行的动态设置"""
        # 玩家的速度
        self.player_speed_factor = 0.5
        # 子弹速度
        self.bullet_speed_factor = 3
        # 敌人右移动速度
        self.enemy_speed_factor = 0.3
        # 设置敌人移动方向,1为右，-1为左
        self.fleet_direction = 1
        # 击毁敌人的分数
        self.enemy_points = 50

    def increase_speed(self):
        """提高速度设置/和敌人点数"""
        self.player_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.enemy_speed_factor *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)
