# -*- coding:utf-8 -*-
import sys
import pygame
from setting import Settings
from player import Player
import game_function as gf
from pygame.sprite import Group
from enemy import Enemy

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()

    # 使用Settings类
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Fight Warriors")

    # 创建游戏玩家
    player = Player(screen, ai_settings)

    # 创建存储子弹的编组
    bullets = Group()


    # 创建敌人编组
    enemies = Group()
    # 创建敌人群
    gf.creat_fleet(ai_settings, screen, enemies)

    # 开始游戏主循环
    while True:
        gf.check_event(player, ai_settings, screen, bullets)
        player.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, player, bullets, enemies)





run_game()


