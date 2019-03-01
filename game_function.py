import sys
import pygame
from bullet import Bullet
from enemy import Enemy

def check_event(player, ai_settings, screen, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, player, ai_settings, bullets, screen)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, player, bullets)






def update_screen(ai_settings, screen, player, bullets, enemies):
    """更新屏幕图像"""
    # 背景颜色
    screen.fill(ai_settings.bg_corlor)
    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制游戏玩家
    player.blitme()
    # 绘制敌人
    enemies.draw(screen)
    # 让绘制的屏幕可见
    pygame.display.flip()

def check_keydown_event(event, player, ai_settings, bullets, screen):
    """响应按键"""
    # 左右移动
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = True
    # 空格开火
    elif event.key == pygame.K_SPACE:
        fire_bullets(player, bullets, ai_settings, screen)
    # 按esc退出游戏
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_event(event, player, bullets):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        player.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.moving_left = False


def update_bullets(bullets):
    """更新子弹位置，并删除消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(player, bullets, ai_settings, screen):
    """如果未达到限制，创建子弹"""
    # 创建子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, player, screen)
        bullets.add(new_bullet)


def creat_fleet(ai_settings, screen, enemies):
    """创建一群敌人"""
    # 创建一个敌人并计算一行能容纳的数量
    enemy = Enemy(screen, ai_settings)
    # 敌人的宽度
    enemy_width = enemy.rect.width
    available_space_x = ai_settings.screen_width - (2 * enemy_width)
    number_enemy_x = int(available_space_x / (2 * enemy_width))

    # 创建一行敌人
    for enemy_number in range(number_enemy_x):
        # 创建一个敌人并将其加入当前行
        enemy = Enemy(screen, ai_settings)
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        enemy.rect.x = enemy.x
        enemies.add(enemy)
