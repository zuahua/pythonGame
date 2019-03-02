import sys
import pygame
from bullet import Bullet
from enemy import Enemy
from time import sleep

def check_event(player, ai_settings, screen, bullets, stats, play_button, enemies,
                score_board):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, player, ai_settings, bullets, screen)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, player, bullets)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, stats, play_button, enemies, bullets,
                              ai_settings, screen, player, score_board)






def update_screen(ai_settings, screen, player, bullets, enemies, play_button, stats,
                  score_board):
    """更新屏幕图像"""
    # 背景颜色
    screen.fill(ai_settings.bg_color)
    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制游戏玩家
    player.blitme()
    # 绘制敌人
    enemies.draw(screen)
    # 显示得分
    score_board.show_score()
    # 如果游戏处于非活动状态，就绘制按钮
    if not stats.active_game:
        play_button.draw_button()
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


def update_bullets(bullets, enemies, ai_settings, screen, player, stats, score_board):
    """更新子弹位置，并删除消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 子弹与敌人碰撞消失，敌人完全消灭后出现新的敌人群
    check_bullet_collision(bullets, enemies, ai_settings, screen, player, stats, score_board)



def fire_bullets(player, bullets, ai_settings, screen):
    """如果未达到限制，创建子弹"""
    # 创建子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, player, screen)
        bullets.add(new_bullet)


def creat_fleet(ai_settings, screen, enemies, player):
    """创建一群敌人"""
    # 创建一个敌人并计算一行能容纳的数量
    enemy = Enemy(screen, ai_settings)
    enemy_width = enemy.rect.width
    number_enemy_x = get_number_enemy_x(ai_settings, enemy_width)
    number_rows = get_number_row(ai_settings, enemy.rect.height, player.rect.height)
    # 创建一群敌人
    for row_number in range(number_rows):
        for enemy_number in range(number_enemy_x):
            creat_enemy(ai_settings, screen, enemies, enemy_number, row_number)


def get_number_enemy_x(ai_settings, enemy_width):
    """获取一行能容纳的敌人数"""
    available_space_x = ai_settings.screen_width - (2 * enemy_width)
    number_enemy_x = int(available_space_x / (2 * enemy_width))
    return number_enemy_x


def creat_enemy(ai_settings, screen, enemies, enemy_number, number_row):
    """创建一个敌人并将其放在当前行"""
    enemy = Enemy(screen, ai_settings)
    # 敌人的宽度
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * number_row
    enemies.add(enemy)


def get_number_row(ai_settings, enemy_height, player_height):
    """计算屏幕能容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - 3 * enemy_height - player_height
    number_row = int(available_space_y / (2 * enemy_height))
    return number_row

def update_enemies(enemies, ai_settings, player, stats, screen, bullets, score_board):
    """检查是否有敌人位于边缘，更新所有敌人位置"""
    check_fleet_edges(enemies, ai_settings)
    enemies.update()
    # 检查敌人与玩家的碰撞
    if pygame.sprite.spritecollideany(player, enemies):
        player_hit(ai_settings, stats, screen, player, enemies, bullets, score_board)
    # 检查是否有敌人到达屏幕底端
    check_enemy_bottom(ai_settings, screen, stats, player, enemies, bullets, score_board)
def check_fleet_edges(enemies, ai_settings):
    """有敌人到达边缘采取措施"""
    for enemy in enemies.sprites():
        if enemy.check_edge():
            change_fleet_direction(enemies, ai_settings)
            break


def change_fleet_direction(enemies, ai_settings):
    """将整群敌人下移并改变敌人移动方向"""
    for enemy in enemies.sprites():
        enemy.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_bullet_collision(bullets, enemies, ai_settings, screen, player, stats, score_board):
    """响应子弹和敌人的碰撞"""
    # 检查是否有子弹击中了敌人
    # 如果有，就删除子弹与相应敌人
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    # 击毁敌人更新分数
    if collisions:
        for enemy in collisions.values():
            stats.score += ai_settings.enemy_points * len(enemy)
            score_board.prep_score()
    # 检查最高分数
    check_high_score(stats, score_board)
    # 在敌人被消灭完时再生成敌人,并加快游戏节奏,提高玩家等级
    if len(enemies) == 0:
        # 提高玩家等级
        stats.level += 1
        score_board.prep_level()

        # 清空子弹
        bullets.empty()
        # 加快游戏节奏
        ai_settings.increase_speed()
        creat_fleet(ai_settings, screen, enemies, player)


def player_hit(ai_settings, stats, screen, player, enemies, bullets, score_board):
    """响应被敌人撞到的玩家"""
    # 将player_left减一
    stats.player_left -= 1
    if stats.player_left > 0:
        # 清空敌人列表和子弹列表
        enemies.empty()
        bullets.empty()

        # 更新玩家可用数
        score_board.prep_players()

        # 创建一群新的敌人并将玩家放在底端中央
        creat_fleet(ai_settings, screen, enemies, player)
        player.center_player()

        # 暂停
        sleep(0.5)
    else:
        stats.active_game = False
        # 游戏结束又显示光标
        pygame.mouse.set_visible(True)


def check_enemy_bottom(ai_settings, screen, stats, player, enemies, bullets, score_board):
    """检查是否有敌人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            # 像敌人与玩家碰撞一样处理
            player_hit(ai_settings, stats, screen, player, enemies, bullets, score_board)
            break

def check_play_button(mouse_x, mouse_y, stats, play_button, enemies, bullets,
                      ai_settings, screen, player, score_board):
    """在玩家单机Play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.active_game:
        # 重置游戏节奏
        ai_settings.initialize_dynamic_settings()
        # 开始游戏，隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.active_game = True
        # 重置记分牌图像
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()
        score_board.prep_players()

        # 清空敌人和子弹
        enemies.empty()
        bullets.empty()

        # 重新创建一群敌人
        creat_fleet(ai_settings, screen, enemies, player)
        # 使玩家居中
        player.center_player()


def check_high_score(stats, score_board):
    """检查最高分数是否达到并重绘最高分数"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()