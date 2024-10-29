import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, ship, bullets, stats, play_button,aliens,sb):
    # 抓取event，即輸入，鍵盤輸入、滑鼠輸入
    for event in pygame.event.get():
        # 如果偵測到視窗關閉
        if event.type == pygame.QUIT:
            # 程式結束運行
            sys.exit()
        # 確認按下鍵盤按鍵
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        # 確認放開鍵盤按鍵
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, sb)

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    # 如果按下方向鍵右
    if event.key == pygame.K_RIGHT:
        # 飛船向右移動
        ship.moving_right = True
    # 如果按下方向鍵左
    elif event.key == pygame.K_LEFT:
        # 飛船向左移動
        ship.moving_left = True
    # 如果按下方向鍵上
    elif event.key == pygame.K_UP:
        # 飛船向上移動
        ship.moving_up = True
    # 如果按下方向鍵下
    elif event.key == pygame.K_DOWN:
        # 飛船向下移動
        ship.moving_down = True
    # 如果按下按鍵z(發射子彈)
    elif event.key == pygame.K_z:
        # 發射子彈
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    # 如果放開方向鍵右
    if event.key == pygame.K_RIGHT:
        # 飛船停止向右移動
        ship.moving_right = False
    # 如果放開方向鍵左
    elif event.key == pygame.K_LEFT:
        # 飛船停止向左移動
        ship.moving_left = False
    # 如果放開方向鍵上
    elif event.key == pygame.K_UP:
        # 飛船停止向上移動
        ship.moving_up = False
    # 如果放開方向鍵下
    elif event.key == pygame.K_DOWN:
        # 飛船停止向下移動
        ship.moving_down = False

def update_bullets(bullets,aliens,ai_settings,screen,ship,stats, sb):
    # 更新子彈群組裡面所有子彈的位置
    bullets.update()
    # 從子彈群組的複本遍歷所有子彈
    for bullet in bullets.copy():
        # 若子彈在視窗外面
        if bullet.rect.bottom <= 0:
            # 從原始的子彈群組刪除該子彈
            bullets.remove(bullet)
    # 檢查碰撞
    check_aliens_bullets_collisions(bullets, aliens, ai_settings, screen, ship,stats, sb)


def update_screen(ai_settings, screen, ship, bullets, aliens,stats, play_button,sb):
    # 將視窗填滿背景顏色
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    # 將飛船影像、位置更新到視窗上面
    ship.blitme()
    # 遍歷子彈群組內的所有子彈
    for bullet in bullets:
        # 將子彈畫在視窗上
        bullet.draw_bullet()
    # 利用Group.draw()來將外星人群組畫在視窗物件上
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    # 翻新視窗畫面
    pygame.display.flip()

def get_number_aliens_x(ai_settings, screen):
    # 獲取外星人寬度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 計算水平方向可用空間
    available_space_x = ai_settings.screen_width - 1.5 * alien_width
    # 計算水平方向外星人數量
    number_alien_x = int(available_space_x / (1.5 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings, screen, ship_height):
    # 獲取外星人高度
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    # 計算垂直方向可用空間
    available_space_y = ai_settings.screen_height - (1.5 * alien_height) - ship_height
    # 計算垂直方向排數
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 分配外星人位置
    alien.x = alien_width + 1.5 * alien_number * alien_width
    alien.rect.x = alien.x
    alien_height = alien.rect.height
    alien.rect.y = alien_height + 1.5 * row_number * alien_height
    # 加入外星人群組
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    number_alien_x = get_number_aliens_x(ai_settings, screen)
    number_rows = get_number_rows(ai_settings, screen, ship.rect.height)
    # 創建一排排外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def check_fleet_edges(ai_settings, aliens):
    # 確認是否有外星人碰到邊界
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break
        
def change_fleet_direction(aliens, ai_settings):
    # 下移並改變方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed 
    ai_settings.fleet_direction *=-1
    
def check_aliens_bullets_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb):
    # 檢查碰撞並消滅子彈、外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        # 檢查每個子彈碰到的外星人數量
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_highest_score(stats, sb)
    
    if len(aliens) == 0:
        # 清空子彈並產生新的外星人群
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


    
def update_aliens(aliens, ai_settings,ship,stats,bullets, screen):
    # 更新所有外星人位置
    check_fleet_edges(ai_settings, aliens)
    check_aliens_bottom(stats, aliens, bullets, ai_settings, screen, ship)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hitted(stats, aliens, bullets, ai_settings, screen, ship)
        

# def ship_hitted(stats, aliens, bullets, ai_settings, screen, ship):
#     if stats.ships_left > 0:
#         print("你只剩下"+str(stats.ships_left)+"條命")
#         # 殘機數減一
#         stats.ships_left-=1
#         # 清空外星人及子彈
#         aliens.empty()
#         bullets.empty()
#         # 創建外星人並重置飛船位置
#         create_fleet(ai_settings, screen, aliens, ship)
#         ship.center_ship()
#         # 暫停
#         sleep(0.5)
#     else:
#         # 遊戲暫停
#         stats.game_active = False
#         pygame.mouse.set_visible (True)

def ship_hitted(stats, aliens, bullets, ai_settings, screen, ship):
    if stats.ships_left > 0:
        print("你只剩下" + str(stats.ships_left) + "條命")
        stats.ships_left -= 1
        bullets.empty()  # 清空子彈，但保持外星人不變
        ship.center_ship()  # 重置飛船位置
        sleep(0.5)  # 暫停一段時間
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # 顯示滑鼠光標


def check_aliens_bottom(stats, aliens, bullets, ai_settings, screen, ship):
    screen_rect = screen.get_rect()
    # 確認每個外星人的位置，是否有碰到螢幕底部
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 類似飛船被外星人碰到一樣處理
            ship_hitted(stats, aliens, bullets, ai_settings, screen, ship)
            break

def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置遊戲設置
        ai_settings.init_dynamic_settings()
        # 隱藏遊戲光標
        pygame.mouse.set_visible(False)
        # 重置遊戲統計信息
        stats.reset_stats()
        stats.game_active = True

        # 重置計分板圖像
        sb.prep_score()
        sb.prep_highest_score()

        # 清空外星人和子彈的列表
        aliens.empty()
        bullets.empty()

        # 創建一個新的外星人群，並將飛船放到屏幕底端中央
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


def check_highest_score(stats, sb):
    if stats.score > stats.highest_score:
        stats.highest_score = stats.score
        sb.prep_highest_score()



