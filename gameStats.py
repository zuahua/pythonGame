class GameStats():
    """跟踪游戏统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.active_game = False
        # 最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行时可能出现的统计变化信息"""
        self.player_left = self.ai_settings.player_limit
        self.score = 0
        self.level = 1
