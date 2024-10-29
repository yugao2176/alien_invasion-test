import pygame
from pygame.sprite import Sprite

# 繼承自 Sprite 類別
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # 繼承 Sprite 的初始化函數
        super().__init__()
        # 抓取視窗物件
        self.screen = screen
        # 抓取遊戲設置物件
        self.ai_settings = ai_settings
        # 讀取圖片檔並產生影像物件
        self.image = pygame.image.load('images/UFO/ufo_04.png')
        # 將影像物件縮小至 0.1 倍
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.1), int(self.image.get_height() * 0.1)))
        # 根據影像物件產生長方形物件
        self.rect = self.image.get_rect()
        # 指定外星人的起始位置
        self.rect.x = 2 * self.rect.width
        self.rect.y = 2 * self.rect.height
        # 設定外星人在水平方向上的精確位置(浮點數)
        self.x = float(self.rect.x)

    def blitme(self):
        # 在視窗上根據長方形的位置畫出外星人
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        # 更新位置
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        # 確認是否碰到螢幕邊緣
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

