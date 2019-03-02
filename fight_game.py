# -*- coding:utf-8 -*-
import sys
import pygame
from setting import Settings
from player import Player
import game_function as gf
from pygame.sprite import Group
from enemy import Enemy
from gameStats import GameStats
from button import  Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()

    # 使用Settings类
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Fight Warriors")
    # 创建Play按钮
    play_button = Button(ai_settings, "Play", screen)

    # 创建游戏玩家
    player = Player(screen, ai_settings)

    # 创建存储子弹的编组
    bullets = Group()


    # 创建敌人编组
    enemies = Group()
    # 创建敌人群
    gf.creat_fleet(ai_settings, screen, enemies, player)

    # 实例化游戏统计信息
    stats = GameStats(ai_settings)
    # 创建分数实例
    score_board = Scoreboard(ai_settings, screen, stats)

    # 开始游戏主循环
    while True:
        gf.check_event(player, ai_settings, screen, bullets, stats, play_button, enemies,
                       score_board)
        if stats.active_game:
            player.update()
            gf.update_bullets(bullets, enemies, ai_settings, screen, player, stats, score_board)
            gf.update_enemies(enemies, ai_settings, player, stats, screen, bullets, score_board)
        gf.update_screen(ai_settings, screen, player, bullets, enemies, play_button, stats,
                         score_board)





run_game()


